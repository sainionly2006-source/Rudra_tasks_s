# Task 8 — Error Handling and Logging

## Objective
Raise clear, recoverable `SensorDataError` exceptions and write processing events as JSON Lines to a local log.

## Behaviour
- Valid records can be processed without stopping the batch.
- Invalid records return a clear error message.
- Log records contain UTC time, event name, and contextual details.
- `demo.py` demonstrates both accepted and rejected messages.

## Run
From `RudraEdge_Software_Package`, run:
`python -m src.demo`
Inspect the generated `sensor_processing.log` file.
