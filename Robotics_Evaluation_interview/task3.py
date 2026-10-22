"""Task 3: Example input validation used by the pytest fuzzing tests."""
import math


def validate_sensor(value, minimum=0, maximum=15):
    if value is None:
        raise ValueError("Sensor value cannot be None")
    if not isinstance(value, (int, float)):
        raise TypeError("Sensor value must be numeric")
    if not math.isfinite(value):
        raise ValueError("Sensor value must be finite")
    if not minimum <= value <= maximum:
        raise ValueError("Sensor value outside allowed range")
    return True


def validate_array(data, expected_length=4):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Sensor data must be a list or tuple")
    if len(data) != expected_length:
        raise ValueError(f"Expected {expected_length} values, received {len(data)}")
    for value in data:
        validate_sensor(value)
    return True
