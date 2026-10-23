"""Parsing and validation for synthetic sensor messages."""
import json
import math
from datetime import datetime

ALLOWED_STATUSES = {"ok", "warning", "error"}
REQUIRED_FIELDS = {"timestamp", "sensor_id", "value", "unit", "status"}

class SensorDataError(ValueError):
    """Raised when a sensor message cannot be parsed or validated."""

def validate_message(message):
    if not isinstance(message, dict):
        raise SensorDataError("Message must be a JSON object")
    missing = REQUIRED_FIELDS - message.keys()
    extra = message.keys() - REQUIRED_FIELDS
    if missing:
        raise SensorDataError(f"Missing required field(s): {', '.join(sorted(missing))}")
    if extra:
        raise SensorDataError(f"Unexpected field(s): {', '.join(sorted(extra))}")
    for field in ("timestamp", "sensor_id", "unit"):
        if not isinstance(message[field], str) or not message[field].strip():
            raise SensorDataError(f"'{field}' must be a non-empty string")
    try:
        # Accept ISO-8601 timestamps; a trailing Z is normalized for older Python versions.
        datetime.fromisoformat(message["timestamp"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise SensorDataError("'timestamp' must be a valid ISO-8601 timestamp") from exc
    value = message["value"]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise SensorDataError("'value' must be a number")
    if not math.isfinite(value):
        raise SensorDataError("'value' must be finite")
    if message["status"] not in ALLOWED_STATUSES:
        raise SensorDataError(f"'status' must be one of {sorted(ALLOWED_STATUSES)}")
    return message

def parse_sensor_message(raw):
    if isinstance(raw, bytes):
        try:
            raw = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise SensorDataError("Input bytes must be UTF-8") from exc
    if not isinstance(raw, str):
        raise SensorDataError("Input must be a JSON string or UTF-8 bytes")
    try:
        message = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SensorDataError(f"Malformed JSON at line {exc.lineno}, column {exc.colno}") from exc
    return validate_message(message)

def parse_sensor_lines(text):
    """Parse newline-separated JSON messages; skip blank lines and report bad lines."""
    results, errors = [], []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            results.append(parse_sensor_message(line))
        except SensorDataError as exc:
            errors.append({"line": line_number, "error": str(exc), "raw": line})
    return results, errors
