"""Tests for software-only I2C recovery simulation."""
from task4 import simulate_i2c_recovery


def test_simulated_recovery_completes_under_50ms():
    status, elapsed_ms = simulate_i2c_recovery()
    assert status == "PASS"
    assert elapsed_ms < 50
