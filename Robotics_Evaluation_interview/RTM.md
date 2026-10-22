# Requirements Traceability Matrix (RTM)

**Project:** RE-T1 (SPECTRA) — Robotics & Embedded Systems  
**Requirement reference from question paper:** `REA-REQ-ROB-05`

| Requirement ID | Requirement | Test path | Status |
|---|---|---|---|
| REA-REQ-ROB-05-01 | Detect timing drift greater than 2 ms in a 50 Hz loop | `test_task1.py` | BLOCKED — drift-injection test still needed |
| REA-REQ-ROB-05-02 | Process frames through a thread-safe queue and check thread shutdown | `test_task1.py`, `task1.py` | BLOCKED — full frame-count test needed |
| REA-REQ-ROB-05-03 | Inject repeatable Gaussian sensor noise | `task2.py` | BLOCKED — review output |
| REA-REQ-ROB-05-04 | Enter failsafe after more than 3 consecutive invalid frames | `test_task2.py` | BLOCKED — run test suite |
| REA-REQ-ROB-05-05 | Check floating-point tolerance below 1e-6 | `test_task2.py` | BLOCKED — run test suite |
| REA-REQ-ROB-05-06 | Test 16 combinations, boundaries, None and truncated arrays | `test_task3.py` | BLOCKED — run test suite |
| REA-REQ-ROB-05-07 | Simulate I2C recovery under 50 ms without hard reset | `test_task4.py` | BLOCKED — software simulation only |
| REA-REQ-ROB-05-08 | ROS 2 bridge integration | Not implemented | BLOCKED — interface/message requirements not supplied |

## Status meanings
- **PASS:** Test was run and the requirement passed.
- **FAIL:** Test was run and the requirement failed.
- **BLOCKED:** Not yet verified or dependent on missing hardware/interface details.

Do not mark an item PASS until the relevant test has actually been run and reviewed.

**Limitation:** `task4.py` simulates recovery timing in software. It does not recover a physical I2C bus or prove hardware timing. The ROS 2 bridge is not implemented because the question paper does not specify its interface or message format.
