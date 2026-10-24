# Task 7 — Data Validation Tests

## Objective
Test missing fields, unexpected fields, malformed JSON, invalid timestamps, invalid values, and invalid statuses.

## Test approach
Tests use Python's built-in `unittest`; no external test framework is required.

## Run
From `RudraEdge_Software_Package`, run:
`python -m unittest tests.test_sensor_parser -v`
Expected result: all tests pass.
