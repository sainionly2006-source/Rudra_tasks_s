# M04 - Synthetic Data Validator
# Task 2.2 - Reads a synthetic sensor-data sample (.jsonl) and validates
# fields/types against the schema in M05_Synthetic_Sensor_Schema.json.
#
# Usage:  python src/synthetic_data_validator.py data/synthetic_samples.jsonl
from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime

EXPECTED_FIELDS = {
    "timestamp": str,   # ISO-8601 string
    "sensor_id": str,
    "value": (int, float),
    "unit": str,
    "status": str,      # one of: OK, WARN, ERROR
}
VALID_STATUSES = {"OK", "WARN", "ERROR"}
VALUE_MIN, VALUE_MAX = -273.15, 1000.0


def validate_record(rec, line_no):
    """Return a list of validation error messages for one record."""
    errors = []
    if not isinstance(rec, dict):
        return ["line %d: record is not a JSON object" % line_no]

    for field in EXPECTED_FIELDS:
        if field not in rec:
            errors.append("line %d: missing field '%s'" % (line_no, field))

    for field, ftype in EXPECTED_FIELDS.items():
        if field in rec and not isinstance(rec[field], ftype):
            errors.append("line %d: field '%s' expected %s, got %s"
                          % (line_no, field, ftype.__name__,
                             type(rec[field]).__name__))

    if "timestamp" in rec and isinstance(rec["timestamp"], str):
        try:
            datetime.fromisoformat(rec["timestamp"].replace("Z", "+00:00"))
        except ValueError:
            errors.append("line %d: malformed timestamp '%s'"
                          % (line_no, rec["timestamp"]))

    if "status" in rec and rec.get("status") not in VALID_STATUSES:
        errors.append("line %d: invalid status '%s' (allowed: %s)"
                      % (line_no, rec.get("status"), sorted(VALID_STATUSES)))

    if "value" in rec and isinstance(rec["value"], (int, float)):
        if not (VALUE_MIN <= rec["value"] <= VALUE_MAX):
            errors.append("line %d: value %s out of range"
                          % (line_no, rec["value"]))

    return errors


def validate_file(path):
    """Validate a .jsonl synthetic-data file. Returns (valid, invalid) counts."""
    valid = invalid = 0
    with Path(path).open("r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                invalid += 1
                print("line %d: malformed JSON message" % i)
                continue
            errs = validate_record(rec, i)
            if errs:
                invalid += 1
                for e in errs:
                    print(e)
            else:
                valid += 1
    print("")
    print("Summary: %d valid, %d invalid records" % (valid, invalid))
    return valid, invalid


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python synthetic_data_validator.py <samples.jsonl>")
    validate_file(sys.argv[1])
