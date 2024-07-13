# Robert Pearce
# 06/24/2024

import numpy as np
import matplotlib.pyplot as plt


def initial_velocity(v, theta):
    """
    Calculate initial horizontal and vertical velocities.
    
    Parameters:
    v (float): Initial speed of the projectile.
    theta (float): Launch angle of the projectile.
    
    Returns:
    tuple: Horizontal and vertical velocities.
    """
    # Convert angle to radians (numpy uses rad).
    theta_rad = np.radians(theta)
    # Calculate the initial horizontal velocity.
    vX = v * np.cos(theta_rad)  # v_x = v * cos(theta)
    # Calculate the initial vertical velocity.
    vY = v * np.sin(theta_rad)  # v_y = v * sin(theta)

    return vX, vY


def total_time(vY, g):
    """
    Calculate total time of flight.
    
    Parameters:
    v_y (float): Vertical velocity.
    g (float): Gravity.
    
    Returns:
    float: Total time of flight.
    """
    # time = (2 * v0 * sin(theta)) / |g|
    T = (2 * vY) / g

    return T


def max_height(vY, g):
    """
    Calculate the maximum height of the projectile.
    
    Parameters:
    v_y (float): Vertical velocity.
    g (float): Gravity.
    
    Returns:
    float: Maximum height.
    """
    # max height = (v_y^2) / (2 * g)
    maxH = (vY ** 2) / (2 * g)

    return maxH


def total_range(vX, T):
    """
    Calculate the range of the projectile.
    
    Parameters:
    v_x (float): Horizontal velocity.
    T (float): Total time of flight.
    
    Returns:
    float: Range of the projectile.
    """
    # range = v_x * t
    range = vX * T

    return range


def trajectory(v_x, v_y, g, interval=1000):
    """
    Calculate the x and y coordinates of the projectile over time.
    
    Parameters:
    v_x (float): Horizontal velocity.
    v_y (float): Vertical velocity.
    g (float): Gravity.
    interval (int): Number of time intervals for the calculation.
    
    Returns:
    tuple: Arrays of x and y coordinates.
    """
    T = total_time(v_y, g)
    t = np.linspace(0, T, num=interval)
    x = v_x * t
    y = v_y * t - 0.5 * g * t**2
    return x, y


def get_user_input():
    """
    Prompt the user for initial velocity and launch angle, ensuring valid input.
    It checks that the initial velocity is non-negative and the launch angle is between 0 and 90 degrees.
    
    Returns:
    tuple: Initial velocity and launch angle as floats.
    """
    # Prompt user until correct input is given.
    while True:
        try:
            # Prompt user for the initial velocity.
            initialV = float(input("Enter the initial velocity (m/s): "))
            # Prompt the user for the launch angle.
            launchAngle = float(input("Enter the launch angle (degrees): "))

            # Check if the initial velocity is valid.
            if initialV < 0:
                # Print error message.
                raise ValueError("Initial velocity cannot be negative.")
            # Check if the launch angle is valid.
            if not (0 <= launchAngle <= 90):
                # Print error message.
                raise ValueError("Launch angle must be between 0 and 90 degrees.")
            
            # If user input was correct.
            return initialV, launchAngle
        # Catch and handle ValueError Exceptions.
        except ValueError as error:
            # Print error message.
            print(f"Invalid input: {error}. Please try again.")


def print_solution(v_x, v_y, time, height, range):
    """
    Format and print answers to terminal.
    
    Parameters:
    v_x (float): Horizontal velocity.
    v_y (float): Vertical velocity.
    time (float): Total time of flight.
    height (float): Maximum height.
    range (float): Range of the projectile.
    """
    # Print results to terminal.
    print(f"Initial horizontal velocity: {v_x:.2f} m/s")
    print(f"Initial vertical velocity: {v_y:.2f} m/s")
    print(f"Total time of flight: {time:.2f} seconds")
    print(f"Maximum height: {height:.2f} meters")
    print(f"Range: {range:.2f} meters")


def plot_trajectory(v_x, v_y, g):
    """
    Plot the trajectory of the projectile.
    
    Parameters:
    v (float): Initial speed of the projectile.
    theta (float): Launch angle of the projectile.
    """
    # Call to function to get horizontal and vertical coordinates.
    x, y = trajectory(v_x, v_y, g)

    # Create a new figure.
    plt.figure(figsize=(10, 5))

    # Plot the horizontal and vertical coordinates.
    plt.plot(x, y)
    # Add a title.
    plt.title('Projectile Motion')
    # Add the x and y labels.
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    # Show the grid.
    plt.grid(True)

    # Show the plot.
    plt.show()


def main():

    #---------------------------
    #    *** VARIABLES ***
    #---------------------------

    # Gravity Constant
    G = 9.81 # m/s^2

    # Variables for calculations.
    initialV = 0        # Initial velocity input.
    launchAngle = 0     # Launch angle input.

    horizontalV = 0     # Horizontal velocity (v_x).
    verticalV = 0       # Vertical velocity (v_y).
    totalTime = 0       # Total time of flight.
    maxHeight = 0       # Max height of projectile.
    range = 0           # Total range of projectile.

    #---------------------------
    #      *** INPUT ***
    #---------------------------

    # Print line and title to look pretty.
    print("-" * 50)

    # Get initial conditions from user.
    initialV, launchAngle = get_user_input()

    # Print line and title to look pretty.
    print("-" * 50)

    #---------------------------
    #   *** PROCESSING ***
    #---------------------------

    # Calculate initial velocity.
    horizontalV, verticalV = initial_velocity(initialV, launchAngle)

    # Calculate total time of flight.
    totalTime = total_time(verticalV, G)

    # Calculate the max height.
    maxHeight = max_height(verticalV, G)

    # Calculate range of projectile.
    range = total_range(horizontalV, totalTime)

    #---------------------------
    #     *** OUTPUT ***
    #---------------------------

    # Call to function to print solution.
    print_solution(horizontalV, verticalV, totalTime, maxHeight, range)

    # Print line and title to look pretty.
    print("-" * 50)

    # Call to function to plot the trajectory using matplotlib.
    plot_trajectory(horizontalV, verticalV, G)


# Call main function.
if __name__ == "__main__":
    main()

#---------------------------
#       *** EOF ***
#---------------------------
