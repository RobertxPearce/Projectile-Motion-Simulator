# Projectile-Motion-Simulator

## Description
A Python program that calculates and visualizes the trajectory, time of flight, maximum height, and range of a projectile launched at a specified angle and velocity.

## Built With
* Python
* Numpy
* Matplotlib
* Pytest

## Closer Look

## Video Demo

## Files
* projectileMotionSim.py
  * Program that computes and visualizes the trajectory of a projectile based on initial launch parameters.
  - `initial_velocity(v, theta)`: Computes the initial horizontal and vertical velocities.
  - `total_time(vY, g)`: Computes the total time of flight.
  - `max_height(vY, g)`: Computes the maximum height reached by the projectile.
  - `total_range(vX, T)`: Computes the total range of the projectile.
  - `main()`: The main function that integrates the input, processing, and output.
* test_projectileMotionSim.py
  * Program for unit tests to verify the projectile motion calculations.
  * Tested using known calculations in an example from "the Physics Classroom" lesson 2.
  - `test_initial_velocity()`: Tests the `initial_velocity` function.
  - `test_total_time()`: Tests the `total_time` function.
  - `test_max_height()`: Tests the `max_height` function.
  - `test_total_range()`: Tests the `total_range` function.

## Usage
To run the simulator, execute the `project.py` script. The user will be prompted to enter the initial velocity and launch angle, and the program will display the calculated results.

To run the tests, execute the following command in the terminal: python `projectileMotionSim.py`

## Resources
* https://openstax.org/books/college-physics-2e/pages/3-4-projectile-motion#:~:text=Projectile%20motion%20is%20the%20motion,path%20is%20called%20its%20trajectory.
* https://en.wikipedia.org/wiki/Projectile_motion
* https://www.physicsclassroom.com/class/vectors/Lesson-2/Horizontal-and-Vertical-Components-of-Velocity
