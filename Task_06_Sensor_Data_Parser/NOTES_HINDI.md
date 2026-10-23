# Task 6 — Sensor Data Parser

## Objective
Read synthetic sensor messages and convert valid JSON into normalized Python dictionaries.

## Main functions
- `parse_sensor_message(raw)`: parse one JSON string or UTF-8 byte sequence.
- `validate_message(message)`: validate required fields, types, timestamp, numeric value, and status.
- `parse_sensor_lines(text)`: process newline-separated messages and collect line-specific errors.

## Run
From `RudraEdge_Software_Package`, run:
`python -c "from src.sensor_parser import parse_sensor_message; print(parse_sensor_message('{\"timestamp\":\"2026-10-24T10:00:00Z\",\"sensor_id\":\"TEMP-001\",\"value\":24.5,\"unit\":\"C\",\"status\":\"ok\"}'))"`
# Task 6 — Sensor Data Parser

## Objective

The objective of this task is to develop a Python-based Sensor Data Parser that reads synthetic sensor messages, validates the data, and converts valid JSON messages into normalized Python dictionaries.

A Sensor Data Parser is useful in IoT systems, robotics, and embedded software, where sensors generate data such as temperature, humidity, pressure, and distance. Before using this data, the software must ensure that the message is correctly formatted and contains all the required information.

The parser supports individual JSON messages as strings or UTF-8 byte sequences. It also supports processing multiple newline-separated messages and collecting errors with their corresponding line numbers.

## Main Functions

### 1. `parse_sensor_message(raw)`

This function reads a single sensor message in JSON format and converts it into a Python dictionary.

Its main responsibilities are:

- Read the input as a JSON string or UTF-8 byte sequence.
- Decode the input if it is provided as bytes.
- Convert the JSON message into a Python dictionary.
- Validate the message before returning the result.
- Report an error if the message contains invalid JSON or incorrect data.

Example input:

```
'{"timestamp":"2026-10-24T10:00:00Z","sensor_id":"TEMP-001","value":24.5,"unit":"C","status":"ok"}'
```

Expected output:

```
{    'timestamp': '2026-10-24T10:00:00Z',    'sensor_id': 'TEMP-001',    'value': 24.5,    'unit': 'C',    'status': 'ok'}
```

### 2. `validate_message(message)`

This function checks whether a sensor message contains all the required fields and whether their values follow the expected rules.

The required fields are:

- Timestamp: Records the date and time when the sensor reading was generated.
- Sensor ID: Identifies the sensor, such as `TEMP-001`.
- Value: Contains the numerical sensor reading, such as `24.5`.
- Unit: Specifies the measurement unit, such as Celsius (`C`).
- Status: Indicates the condition of the sensor reading, such as `ok`.

The function checks for missing fields, incorrect data types, invalid timestamps, non-numeric sensor values, and unsupported status values. If the message does not satisfy the required rules, an appropriate error should be reported.

### 3. `parse_sensor_lines(text)`

This function processes multiple sensor messages separated by newline characters.

It reads each line individually, parses and validates the message, collects valid messages, and records errors for invalid messages.

For example, if a file contains five sensor messages and one message has invalid JSON, the parser can process the remaining messages and report the error with its line number.

This function is useful for processing sensor log files and data received from multiple devices.

## Working Procedure

1. Receive the sensor message as a JSON string or UTF-8 byte sequence.
2. Decode the message if it is provided as bytes.
3. Parse the JSON data into a Python dictionary.
4. Validate the required fields and their data types.
5. Check the timestamp, numerical value, and sensor status.
6. Return the normalized dictionary if the message is valid.
7. Report an error if the message is invalid.
8. For multiple messages, process each line separately and collect line-specific errors.

## Execution Command

Run the following command from the `RudraEdge_Software_Package` directory:

```
python -c "from src.sensor_parser import parse_sensor_message; print(parse_sensor_message('{\"timestamp\":\"2026-10-24T10:00:00Z\",\"sensor_id\":\"TEMP-001\",\"value\":24.5,\"unit\":\"C\",\"status\":\"ok\"}'))"
```

This command imports the `parse_sensor_message()` function from `src.sensor_parser`, passes a sample JSON sensor message to it, and prints the returned Python dictionary.

## Testing and Validation

The following test cases can be used to verify the parser:

1. Valid message: A message containing all required fields should be parsed successfully.
2. Missing field: A message without a required field should produce a validation error.
3. Invalid JSON: A message with incorrect JSON syntax should produce a parsing error.
4. Invalid sensor value: A string or other unsupported value should be rejected.
5. Invalid timestamp: A timestamp that does not follow the accepted format should be rejected.
6. Invalid status: A status outside the permitted values should produce an error.
7. Multiple messages: The parser should process newline-separated messages and collect errors with line numbers.
8. UTF-8 byte input: A valid JSON message provided as bytes should be decoded and processed correctly.

## Applications

The Sensor Data Parser has several practical applications:

- IoT systems: Processing data received from connected sensors.
- Robotics: Reading and validating sensor measurements used by robotic systems.
- Environmental monitoring: Processing temperature, humidity, and air-quality readings.
- Industrial automation: Validating sensor data generated by machines.
- Data logging: Preparing valid sensor readings for storage in files or databases.
- Error handling: Identifying invalid messages and helping developers locate data problems.

## Advantages

1. It improves the reliability of sensor data.
2. It detects missing fields and incorrectly formatted messages.
3. It converts JSON data into a Python-friendly format.
4. It supports both individual messages and multiple-line inputs.
5. It provides line-specific error information for easier debugging.
6. It helps prevent invalid sensor data from being processed by other software modules.

## Conclusion

The Sensor Data Parser is an important component of sensor-based software systems. It reads JSON messages, validates their structure and values, and converts valid messages into normalized Python dictionaries. The `parse_sensor_message()` function handles individual messages, `validate_message()` checks their correctness, and `parse_sensor_lines()` processes multiple messages while collecting errors. These functions improve data consistency, simplify error detection, and make sensor information easier to use in IoT, robotics, and embedded software applications.