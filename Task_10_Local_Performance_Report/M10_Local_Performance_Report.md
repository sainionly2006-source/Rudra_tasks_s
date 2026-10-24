"""Simple repeatable local processing-time benchmark; results are machine-dependent."""
import json
import time
from .sensor_parser import parse_sensor_message

SAMPLE = json.dumps({
    "timestamp": "2026-10-24T10:00:00Z",
    "sensor_id": "TEMP-001",
    "value": 24.5,
    "unit": "C",
    "status": "ok"
})

def run_benchmark(iterations=10000):
    start = time.perf_counter()
    for _ in range(iterations):
        parse_sensor_message(SAMPLE)
    elapsed = time.perf_counter() - start
    return {
        "iterations": iterations,
        "elapsed_seconds": round(elapsed, 6),
        "messages_per_second": round(iterations / elapsed, 2) if elapsed else None,
        "average_ms_per_message": round(elapsed * 1000 / iterations, 6)
    }

if __name__ == "__main__":
    print(json.dumps(run_benchmark(), indent=2))
