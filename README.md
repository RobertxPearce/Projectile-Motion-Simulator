# Projectile Motion Simulator

### Description
A Python program that calculates and visualizes the trajectory, time of flight, maximum height, and range of a projectile given a launch angle and initial velocity. The program makes use of fundamental physics equations to perform these calculations using the Numpy library for calculations and the Matplotlib library for a visualization of the trajectory. 

Also included are unit tests implemented using the Pytest framework. The unit tests use example problems from OpenStax's "University Physics Volume 1" to ensure accuracy and reliability.

### Built With
* Python 3.9
* Numpy
* Matplotlib
* Pytest

## Files
### projectileMotionSim.py
- Program that computes and visualizes the trajectory, time of flight, maximum height, and range of a projectile launched at a specified angle and initial velocity.
  - `initial_velocity(v, theta)`: Computes the initial horizontal and vertical velocities.
  - `total_time(vY, g)`: Computes the total time of flight.
  - `max_height(vY, g)`: Computes the maximum height reached by the projectile.
  - `total_range(vX, T)`: Computes the total range of the projectile.
  - `trajectory(v_x, v_y, g, interval=1000)`: Calculates the x and y coordinates of the projectile over time.
  - `get_user_input()`: Prompts the user for initial velocity and launch angle, ensuring valid input.
  - `print_solution(v_x, v_y, time, height, range)`: Formats and prints the answers to the terminal.
  - `plot_trajectory(v_x, v_y, g)`: Plots the trajectory of the projectile.
  - `main()`: The main function that combines the input, processing, and output.
### test_projectileMotionSim.py
- Tests for the key functions in projectileMotionSim.py using pytest. These tests verify the correctness of the calculations against known examples from the OpenStax "University Physics Volume 1" textbook.
  - `test_initial_velocity()`: Tests the `initial_velocity` function.
  - `test_total_time()`: Tests the `total_time` function.
  - `test_max_height()`: Tests the `max_height` function.

## Closer Look
![projectile-motion-sim](https://github.com/user-attachments/assets/40ffd9e5-2bce-493f-ad65-42ca2f071ac2)

### [Video Demo](https://youtu.be/kSCf7GNaRnU?si=JmcRXCaXSkn-ctGD)

## Usage
To run the simulator, execute `projectileMotionSim.py` in terminal. You will be prompted to enter the initial velocity and launch angle, and the program will display the calculated results and plot the trajectory.
```bash
python projectileMotionSim.py
```
```bash
pytest test_projectileMotionSim.py
```

## Resources
* https://openstax.org/books/university-physics-volume-1/pages/1-introduction
* https://openstax.org/books/college-physics-2e/pages/3-4-projectile-motion#:~:text=Projectile%20motion%20is%20the%20motion,path%20is%20called%20its%20trajectory.
* https://en.wikipedia.org/wiki/Projectile_motion
* https://www.physicsclassroom.com/class/vectors/Lesson-2/Horizontal-and-Vertical-Components-of-Velocity
