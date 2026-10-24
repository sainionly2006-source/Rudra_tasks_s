import json
import unittest
from src.sensor_parser import parse_sensor_message, parse_sensor_lines, SensorDataError

GOOD = {
    "timestamp": "2026-10-24T10:00:00Z",
    "sensor_id": "TEMP-001",
    "value": 24.5,
    "unit": "C",
    "status": "ok"
}

class SensorParserTests(unittest.TestCase):
    def test_valid_message(self):
        self.assertEqual(parse_sensor_message(json.dumps(GOOD))["sensor_id"], "TEMP-001")

    def test_utf8_bytes(self):
        self.assertEqual(parse_sensor_message(json.dumps(GOOD).encode())["value"], 24.5)

    def test_missing_field(self):
        data = dict(GOOD)
        del data["unit"]
        with self.assertRaisesRegex(SensorDataError, "Missing"):
            parse_sensor_message(json.dumps(data))

    def test_extra_field(self):
        data = dict(GOOD, unexpected=1)
        with self.assertRaisesRegex(SensorDataError, "Unexpected"):
            parse_sensor_message(json.dumps(data))

    def test_malformed_json(self):
        with self.assertRaisesRegex(SensorDataError, "Malformed JSON"):
            parse_sensor_message('{"timestamp":')

    def test_bad_timestamp(self):
        data = dict(GOOD, timestamp="not-a-date")
        with self.assertRaisesRegex(SensorDataError, "ISO-8601"):
            parse_sensor_message(json.dumps(data))

    def test_non_numeric_value(self):
        data = dict(GOOD, value="24.5")
        with self.assertRaisesRegex(SensorDataError, "must be a number"):
            parse_sensor_message(json.dumps(data))

    def test_non_finite_value(self):
        # Python's json module can decode NaN, but our validator must reject it.
        data = dict(GOOD, value=float("nan"))
        with self.assertRaisesRegex(SensorDataError, "finite"):
            parse_sensor_message(json.dumps(data))

    def test_invalid_status(self):
        data = dict(GOOD, status="unknown")
        with self.assertRaisesRegex(SensorDataError, "status"):
            parse_sensor_message(json.dumps(data))

    def test_blank_sensor_id(self):
        data = dict(GOOD, sensor_id=" ")
        with self.assertRaisesRegex(SensorDataError, "sensor_id"):
            parse_sensor_message(json.dumps(data))

    def test_line_parser_reports_bad_lines(self):
        text = json.dumps(GOOD) + "\n{bad json}\n"
        valid, errors = parse_sensor_lines(text)
        self.assertEqual(len(valid), 1)
        self.assertEqual(errors[0]["line"], 2)

if __name__ == "__main__":
    unittest.main()
