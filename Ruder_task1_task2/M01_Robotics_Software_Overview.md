# M01 - Robotics Software Overview
**Trainee:** Mohit Saini (TRAIN-003) | **Task Order Ref:** REA/2026/RE-T1/TRAIN-002-005 | **Date:** 22 October 2026

## Task 1.1 - Software Architecture Review and Robotics/Embedded Responsibilities

### 1. Purpose
Establish a local, simulation-oriented robotics software foundation with basic
synthetic-data processing and validation on non-physical hardware.

### 2. Architecture Overview
    [Synthetic Data Generator] --> [Sensor Data Parser] --> [Validated Output]
            |                        |
       Config (JSON)         [Validation & Error Checks] --> Logs / Events
                                   |
                              Test Suite (unit tests)

### 3. Module Roles and Responsibilities
| Module | Responsibility |
|---|---|
| Synthetic data generator | Produces sensor messages (timestamp, ID, units, status) per M05_Synthetic_Sensor_Schema.json |
| Sensor data parser (M06) | Loads synthetic messages, converts to normalized output |
| Validation layer (M07/M08) | Checks missing fields, invalid values, malformed messages, out-of-range data |
| Test suite (M09) | Unit tests for normal inputs, incomplete records, invalid types |
| Logging (M08) | Structured local logging of processing events |
| Packaging (M11) | Reproducible package of code, tests, data, config |

### 4. Key Constraints and Assumptions
- Simulation-only; no physical hardware or drivers required.
- Python 3.11+, standard library preferred; pandas optional.
- Deterministic seeds for reproducible synthetic data.

## Task 1.2 - Local Development Environment
(Summary; full detail in M02_Development_Environment_Report.md)

| Item | Detail |
|---|---|
| OS | Ubuntu 22.04 LTS (primary) / Windows 11 (secondary) |
| Python | 3.11.9 |
| Tools | VS Code, Git 2.43, pytest 8.x |
| Compatibility limits | No ARM32 targets; simulation-only runtimes |
