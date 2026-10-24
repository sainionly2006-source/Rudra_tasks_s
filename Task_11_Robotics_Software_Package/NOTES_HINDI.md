# Task 11 — Final Software Package

## Objective
Organize source code, schema, tests, logs generated at runtime, and documentation into a reproducible package.

## Contents
- `src/`: parser, schema, event logger, demo, benchmark
- `tests/`: unit tests
- `README.md`: setup and run instructions

## Run
Open a terminal in `RudraEdge_Software_Package` and run:
`python -m unittest discover -s tests -v`
Then:
`python -m src.demo`
Then:
`python -m src.benchmark`

## Packaging
The full package is included at the ZIP root under `RudraEdge_Software_Package`.
