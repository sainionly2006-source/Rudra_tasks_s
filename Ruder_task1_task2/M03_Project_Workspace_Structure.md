# M03 - Project Workspace Structure
**Trainee:** Mohit Saini (TRAIN-003) | **Task Order Ref:** REA/2026/RE-T1/TRAIN-002-005 | **Date:** 22 October 2026

## Task 2.1 - Clean Project Workspace for Source Code, Config, Tests, Logs

    robotics_sim_foundation/
    |-- README.md
    |-- requirements.txt
    |-- config/
    |   |-- sensor_config.json            # thresholds, sample sizes, seed
    |-- src/
    |   |-- __init__.py
    |   |-- data_generator.py             # synthetic sensor stream producer
    |   |-- sensor_parser.py              # M06: parser -> normalized output
    |   |-- validators.py                   # field/type/range validators
    |   |-- error_handler.py              # M08: error handling + structured logging
    |-- data/
    |   |-- synthetic_samples.jsonl       # generated sample input
    |   |-- normalized_output.jsonl         # parser output
    |-- tests/
    |   |-- __init__.py
    |   |-- test_parser_normal.py           # normal inputs
    |   |-- test_parser_incomplete.py       # missing-field records
    |   |-- test_parser_invalid.py          # invalid types / values
    |-- logs/
    |   |-- processing_events.log           # structured local logs
    |-- reports/
        |-- M10_Local_Performance_Report.md

### Folder Rules
- src/ - production code only; no test fixtures inside.
- config/ - all tunable parameters externalized; no hard-coded thresholds.
- data/ - synthetic data only (.jsonl), never commit over 1 MB.
- tests/ - mirrors src/ naming: test_<module>_<case>.py.
- logs/ - append-only, git-ignored for large runs.

## Naming and Versioning Convention
- Files: M0X_Snake_Case_Name.ext
- Git tags: train003-task1-v1.0, train003-task2-v1.0
