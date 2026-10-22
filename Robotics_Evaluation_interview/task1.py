"""Task 1: 50 Hz timing drift and thread-safe frame queue demonstration."""
import queue
import threading
import time

FREQUENCY_HZ = 50
PERIOD_SECONDS = 1.0 / FREQUENCY_HZ
DRIFT_LIMIT_SECONDS = 0.002
FRAME_COUNT = 100

frame_queue = queue.Queue(maxsize=100)
stop_event = threading.Event()
processed_frames = []


def consumer():
    """Consume frames until producer has stopped and the queue is empty."""
    while not stop_event.is_set() or not frame_queue.empty():
        try:
            frame_id, timestamp = frame_queue.get(timeout=0.1)
        except queue.Empty:
            continue
        processed_frames.append(frame_id)
        frame_queue.task_done()


def producer():
    """Schedule frames against a monotonic clock and report timing drift."""
    target_time = time.monotonic()
    for frame_id in range(FRAME_COUNT):
        target_time += PERIOD_SECONDS
        remaining = target_time - time.monotonic()
        if remaining > 0:
            time.sleep(remaining)

        actual_time = time.monotonic()
        drift = abs(actual_time - target_time)
        if drift > DRIFT_LIMIT_SECONDS:
            print(f"Frame {frame_id}: drift warning {drift * 1000:.3f} ms")

        try:
            frame_queue.put((frame_id, actual_time), timeout=0.1)
        except queue.Full:
            print(f"Frame {frame_id}: queue full; frame was not enqueued")

    stop_event.set()


def main():
    worker = threading.Thread(target=consumer, name="frame-consumer", daemon=False)
    worker.start()
    try:
        producer()
    finally:
        stop_event.set()
        worker.join(timeout=2.0)

    print(f"Frames generated: {FRAME_COUNT}")
    print(f"Frames processed: {len(processed_frames)}")
    print(f"Consumer thread alive after join: {worker.is_alive()}")
    if len(processed_frames) == FRAME_COUNT and not worker.is_alive():
        print("Queue processing check: PASS")
    else:
        print("Queue processing check: FAIL")


if __name__ == "__main__":
    main()
