# M02 - Development Environment Report
**Trainee:** Mohit Saini (TRAIN-003) | **Task Order Ref:** REA/2026/RE-T1/TRAIN-002-005 | **Date:** 22 October 2026

## Task 1.2 - Documented Dev Environment, Tool Versions, OS Details, Compatibility Limits

### 1. OS Details
- **Primary:** Ubuntu 22.04.4 LTS (x86_64), kernel 6.5
- **Secondary:** Windows 11 Pro 23H2 (cross-check environment)

### 2. Tool Versions
| Tool | Version | Purpose |
|---|---|---|
| Python | 3.11.9 | Runtime for all modules |
| pip | 24.0 | Package management |
| Git | 2.43.0 | Version control |
| VS Code | 1.94 | Editor / debugger |
| pytest | 8.1.1 | Unit test execution |
| pandas | 2.2.1 | Optional data normalization |
| pre-commit | 3.6 | Lint/format hooks |

### 3. Environment Setup
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python -m pytest tests/ -v

### 4. Compatibility Limits and Risks
| Limit / Risk | Impact | Mitigation |
|---|---|---|
| No physical sensors | Cannot validate real timing jitter | Use deterministic synthetic streams |
| pandas optional module | Extra dependency on some machines | Core parser uses stdlib only |
| Windows path handling | Path separator issues in logs | Use pathlib everywhere |
| Python below 3.10 unsupported | Type-hint syntax breaks | Pin minimum version in README |
