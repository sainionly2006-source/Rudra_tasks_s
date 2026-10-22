"""Tests for PID simulation, failsafe and floating-point tolerance."""
import pytest
from task2 import (
    FAIL_SAFE_STATE, NORMAL_STATE, pid_step, precision_check, run_simulation
)


def test_pid_step_returns_finite_output():
    output, integral, error = pid_step(10.0, 9.9, 1.0, 0.1, 0.05, 0.0, 0.0, 0.02)
    assert isinstance(output, float)
    assert integral != 0
    assert error > 0


def test_precision_check_passes_close_values():
    assert precision_check(1.0, 1.0000001)


def test_precision_check_rejects_values_outside_tolerance():
    assert not precision_check(1.0, 1.00001)


def test_failsafe_after_four_consecutive_invalid_frames():
    assert run_simulation([None, None, None, None, 10.0]) == FAIL_SAFE_STATE


def test_normal_state_for_valid_measurements():
    assert run_simulation([10.0, 10.1]) == NORMAL_STATE
