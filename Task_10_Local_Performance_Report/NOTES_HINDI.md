# Task 10 — Local Performance Report

## Objective
Measure local parsing throughput using a repeatable synthetic message.

## Measurement method
The benchmark uses `time.perf_counter()` and reports:
- number of iterations
- total elapsed seconds
- messages per second
- average milliseconds per message

## Run
From `RudraEdge_Software_Package`, run:
`python -m src.benchmark`

## Report your actual result
Copy the JSON printed by the command into the Results section below. Values depend on CPU, OS, Python version, and background load.

## Results
- Python version:
- Computer/OS:
- Iterations:
- Elapsed seconds:
- Messages per second:
- Average ms per message:

## Limitations
This is a local microbenchmark, not a real-time or hardware performance guarantee. Run it multiple times and report the typical result.
