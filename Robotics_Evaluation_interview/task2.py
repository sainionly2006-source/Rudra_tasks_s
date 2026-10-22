"""Task 2: Gaussian sensor-noise simulation, PID step, failsafe, precision check."""
import math
import random

random.seed(42)  # Fixed seed makes the demo repeatable.

NORMAL_STATE = "NORMAL_STATE"
FAIL_SAFE_STATE = "FAIL_SAFE_STATE"
TOLERANCE = 1e-6
MAX_CONSECUTIVE_ERRORS = 3


def inject_noise(value, standard_deviation=0.1):
    """Return a value with simulated Gaussian sensor noise."""
    return value + random.gauss(0.0, standard_deviation)


def pid_step(setpoint, measurement, kp, ki, kd, integral, previous_error, dt):
    """Compute one discrete PID output and return output, integral, error."""
    if dt <= 0:
        raise ValueError("dt must be greater than zero")
    error = setpoint - measurement
    new_integral = integral + error * dt
    derivative = (error - previous_error) / dt
    output = kp * error + ki * new_integral + kd * derivative
    return output, new_integral, error


def precision_check(expected, actual):
    """Check finite floating-point values with strict 1e-6 tolerance."""
    return (
        math.isfinite(expected)
        and math.isfinite(actual)
        and abs(expected - actual) < TOLERANCE
    )


def run_simulation(injected_measurements=None):
    """Run simulated frames. None/non-finite measurements count as errors."""
    setpoint = 10.0
    kp, ki, kd = 1.0, 0.1, 0.05
    integral = 0.0
    previous_error = 0.0
    dt = 0.02
    consecutive_errors = 0
    state = NORMAL_STATE

    if injected_measurements is None:
        measurements = [inject_noise(setpoint) for _ in range(20)]
    else:
        measurements = list(injected_measurements)

    for frame, measurement in enumerate(measurements):
        if measurement is None or not isinstance(measurement, (int, float)) or not math.isfinite(measurement):
            consecutive_errors += 1
            print(f"Frame {frame}: invalid sensor reading; consecutive errors={consecutive_errors}")
        else:
            output, integral, error = pid_step(
                setpoint, measurement, kp, ki, kd, integral, previous_error, dt
            )
            previous_error = error
            consecutive_errors = 0
            print(
                f"Frame={frame}, sensor={measurement:.6f}, "
                f"PID output={output:.6f}, state={state}"
            )

        # "Exceeds 3 frames" means activation after the fourth consecutive error.
        if consecutive_errors > MAX_CONSECUTIVE_ERRORS:
            state = FAIL_SAFE_STATE
            print(f"Frame {frame}: {state} activated")
            break

    return state


if __name__ == "__main__":
    print("=== Normal noisy sensor demonstration ===")
    run_simulation()
    print("\n=== Failsafe demonstration (four invalid frames) ===")
    run_simulation([None, None, None, None, 10.0])
    print("\nPrecision check:", precision_check(1.0, 1.0000001))
