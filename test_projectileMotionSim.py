# Robert Pearce
# 06/24/2024

import pytest
from projectileMotionSim import initial_velocity
from projectileMotionSim import total_time
from projectileMotionSim import max_height
from projectileMotionSim import total_range


def test_initial_velocity():
    """
    Example problem for initial velocity: OpenStax, University Physics Volume 1, Chapter 4.3, Example 4.7
    """
    _initial_velocity = 70.0  # Initial speed provided by problem.
    _launch_angle = 75.0      # Launch angle provided by problem.

    # Find the vertical velocity.
    vX, vY = initial_velocity(_initial_velocity, _launch_angle)

    # Check if the horizontal velocity matches the answer provided in textbook.
    assert pytest.approx(vX, 0.1) == 18.1

    # Check if the vertical velocity matches the answer provided in textbook.
    assert pytest.approx(vY, 0.1) == 67.6


def test_total_time():
    """
    Example problem for total time of flight: OpenStax, University Physics Volume 1, Chapter 4.3, Example 4.8
    """
    vY = 21.2   # Vertical velocity provided by problem.
    G = 9.81    # Gravity constant.

    # Call function to compute total time.
    _total_time = total_time(vY, G)

    # Check if total time matches the answer provided in textbook.
    assert pytest.approx(_total_time, 0.1) == 4.32


def test_max_height():
    """
    Example problem for maximum height: OpenStax, University Physics Volume 1, Chapter 4.3, Example 4.7
    """
    _initial_velocity = 70.0  # Initial speed provided by problem.
    _launch_angle = 75.0      # Launch angle provided by problem.
    G = 9.81                  # Gravity constant.

    # Find the vertical velocity.
    vX, vY = initial_velocity(_initial_velocity, _launch_angle)

    # Round answer to whole number for assert.
    _max_height = round(max_height(vY, G))

    # Check if max height function return value matches answer given by textbook.
    assert _max_height == 233


if __name__ == "__main__":
    pytest.main()