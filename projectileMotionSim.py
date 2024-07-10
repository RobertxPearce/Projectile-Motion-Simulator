# Robert Pearce
# 06/24/2024

import numpy as np

# Initial Velocity Function
# v : Initial speed of projectile.
# m : Launch angle of projectile.
def initialVelocity(v, theta):
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
def totalTime(vY, g):
    # time = (2 * v0 * sin(theta)) / |g|
    T = (2 * vY) / g

    return T


# Max Height Function
# vY : Vertical velocity.
# g : Gravity
def maxHeight():
    # max height = (v_y^2) / (2 * g)
    maxH = (vY ** 2) / (2 * g)

    return maxH

# Range Function


# Main function
def main():
    # Gravity Constant
    G = 9.81 # m/s^2


# Call main function.
if __name__ == "__main__":
    main()