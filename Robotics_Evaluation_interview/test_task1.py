"""Small tests for timing constants and queue availability."""
import queue
from task1 import FREQUENCY_HZ, PERIOD_SECONDS


def test_frequency_is_50_hz():
    assert FREQUENCY_HZ == 50


def test_period_is_20_ms():
    assert abs(PERIOD_SECONDS - 0.020) < 1e-12


def test_queue_is_thread_safe_queue_type():
    from task1 import frame_queue
    assert isinstance(frame_queue, queue.Queue)
