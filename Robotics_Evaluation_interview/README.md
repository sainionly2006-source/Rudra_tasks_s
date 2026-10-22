# Robotics Evaluation Starter Project

This project contains Python starter implementations for the four tasks in the supplied evaluation paper.

## Requirements
- Python 3.10 or later recommended
- pytest for automated tests

## Files
- `task1.py`: 50 Hz scheduling, timing-drift reporting, thread-safe queue and thread shutdown check
- `task2.py`: Gaussian sensor noise, discrete PID step, failsafe after four consecutive invalid frames, precision tolerance check
- `task3.py`: input validation functions
- `task4.py`: software-only I2C recovery timing simulation
- `test_task1.py` through `test_task4.py`: automated tests
- `test_task3.py`: 16-case parameterized matrix and invalid-input tests
- `RTM.md`: requirements traceability matrix

## Run the demonstrations
```bash
python task1.py
python task2.py
python task4.py
```

## Install pytest (while internet is available)
```bash
python -m pip install pytest
```

## Run all tests
```bash
python -m pytest -v
```

## Important limitations
This is a starter/demo project, not a certified or fully verified 100-mark submission. Task 1 demonstrates scheduling and queue processing but does not prove deadlock isolation under every condition. Task 3's 16-case matrix demonstrates parameterized combinations of four binary fields; adapt it to the actual application parameters. Task 4 is a software simulation only. A real ROS 2 bridge and hardware I2C recovery require further interface and hardware details.
