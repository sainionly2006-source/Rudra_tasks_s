# Task 5 — Synthetic Sensor Data Schema

## Objective
Define a consistent JSON structure for simulated robotics sensor messages. This task uses synthetic data only and does not require physical hardware.

## Required fields
- `timestamp`: a non-empty ISO-8601 date/time string, for example `2026-10-24T10:00:00Z`.
- `sensor_id`: a non-empty identifier for the sensor, for example `TEMP-001`.
- `value`: a numeric measurement, for example `24.5`.
- `unit`: a non-empty measurement unit, for example `C` or `kPa`.
- `status`: one of `ok`, `warning`, or `error`.

Unknown extra fields are not allowed by this schema.

## Example valid message
```json
{
  "timestamp": "2026-10-24T10:00:00Z",
  "sensor_id": "TEMP-001",
  "value": 24.5,
  "unit": "C",
  "status": "ok"
}
```

## How to verify on Windows
1. Open `M05_Synthetic_Sensor_Schema.json` in VS Code.
2. Confirm that the file is valid JSON and that all five required fields are present.
3. If you have already downloaded the complete RudraEdge package, open a terminal in `RudraEdge_Software_Package` and run:
   `python -m unittest discover -s tests -v`
4. Keep the actual terminal output or a screenshot as evidence. Do not claim a test passed unless you ran it.

## Git upload
Place this folder inside your existing `Rudra` project/repository, then commit and push the two files. See the Hindi instructions in the chat for the Git steps.
