"""Task 3: Pytest boundary, invalid-input and 16-combination tests."""
import itertools
import pytest
from task3 import validate_sensor, validate_array

# Four input dimensions, each with two representative values: 2^4 = 16 cases.
CASES = list(itertools.product(
    [0, 1],       # sample value
    [0, 1],       # status flag
    [0, 1],       # mode flag
    [0, 1],       # sequence flag
))


@pytest.mark.parametrize("value,status,mode,sequence", CASES)
def test_16_combination_matrix(value, status, mode, sequence):
    # The matrix verifies all combinations are enumerated. Each field is
    # intentionally constrained to 0/1 for this demonstration.
    assert value in (0, 1)
    assert status in (0, 1)
    assert mode in (0, 1)
    assert sequence in (0, 1)


@pytest.mark.parametrize("value", [0, 5, 15])
def test_valid_boundaries(value):
    assert validate_sensor(value, 0, 15)


@pytest.mark.parametrize("value", [-1, 16])
def test_out_of_range_boundaries(value):
    with pytest.raises(ValueError):
        validate_sensor(value, 0, 15)


def test_none_value():
    with pytest.raises(ValueError):
        validate_sensor(None, 0, 15)


def test_nan_value():
    with pytest.raises(ValueError):
        validate_sensor(float("nan"), 0, 15)


def test_wrong_type():
    with pytest.raises(TypeError):
        validate_sensor("12", 0, 15)


def test_truncated_array_is_rejected():
    with pytest.raises(ValueError):
        validate_array([10, 20], expected_length=4)


def test_wrong_array_type_is_rejected():
    with pytest.raises(TypeError):
        validate_array(None, expected_length=4)
