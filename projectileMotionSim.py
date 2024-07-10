# Robert Pearce
# 06/24/2024

import numpy as np


# Initial Velocity Function
# v : Initial speed of projectile.
# m : Launch angle of projectile.
def initial_velocity(v, theta):
    # Convert angle to radians (numpy uses rad).
    theta_rad = np.radians(theta)
    # Calculate the initial horizontal velocity.
    vX = v * np.cos(theta_rad) # v_x = v * cos(theta)
    # Calculate the initial vertical velocity.
    vY = v * np.sin(theta_rad) # v_y = v * sin(theta)

    return vX, vY


# Total Time of Whole Journey Function
# vY : Vertical velocity.
# g : Gravity
def total_time(vY, g):
    # time = (2 * v0 * sin(theta)) / |g|
    T = (2 * vY) / g

    return T


# Max Height Function
# vY : Vertical velocity.
# g : Gravity
def max_height(vY, g):
    # max height = (v_y^2) / (2 * g)
    maxH = (vY ** 2) / (2 * g)

    return maxH


# Range Function
# vX : Horizontal Velocity.
# T : Total time of flight.
def total_range(vX, T):
    # range = v_x * t
    range = vX * T

    return range

#---------------------------
# *** Main Entry Point ***
#---------------------------

# Main function
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
    initialV = float(input("Enter the initial velocity (m/s): "))
    launchAngle = float(input("Enter the launch angle (degrees): "))

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
    maxHeight = max_height(horizontalV, G)

    # Calculate range of projectile.
    range = total_range(verticalV, totalTime)

    #---------------------------
    #     *** OUTPUT ***
    #---------------------------

    # Print results to terminal.
    print(f"Initial horizontal velocity: {horizontalV:.2f} m/s")
    print(f"Initial vertical velocity: {verticalV:.2f} m/s")
    print(f"Total time of flight: {totalTime:.2f} seconds")
    print(f"Maximum height: {maxHeight:.2f} meters")
    print(f"Range: {range:.2f} meters")

    # Print line and title to look pretty.
    print("-" * 50)


# Call main function.
if __name__ == "__main__":
    main()

#---------------------------
#       *** EOF ***
#---------------------------
