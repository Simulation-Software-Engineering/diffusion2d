"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""

import numpy as np
import matplotlib.pyplot as plt

import output

def solve(dx=0.1, dy=0.1, D=4):
    """
    Solve the 2D diffusion equation for a heat transfer problem
    on a flat 10 mm plate and plot the results.

    Initial temperature of plate is 300 degrees and circular disk
    is at 700 degrees.

    Parameters
    dx: mesh intervals in x direction in mm. Default value is 0.1
    dy: mesh intervals in y direction in mm. Default value is 0.1
    D:  Thermal diffusivity of steel in mm^2/s. Default value is 4
    """

    # plate size, mm
    w = h = 10.
    
    # Initial cold temperature of square domain
    T_cold = 300

    # Initial hot temperature of circular disc at the center
    T_hot = 700

    # Number of discrete mesh points in X and Y directions
    nx, ny = int(w / dx), int(h / dy)

    # Computing a stable time step
    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    print("dt = {}".format(dt))

    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    # Initial conditions - circle of radius r centred at (cx,cy) (mm)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot


    def do_timestep(u_nm1, u, D, dt, dx2, dy2):
        # Propagate with forward-difference in time, central-difference in space
        u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
                (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
                + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)

        u_nm1 = u.copy()
        return u_nm1, u


    # Number of timesteps
    nsteps = 101
    # Output 4 figures at these timesteps
    n_output = [0, 10, 50, 100]
    fig_counter = 0
    fig = plt.figure()

    # Time loop
    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)
        
        # Create figure
        if n in n_output:
            im, fig_counter = output.create_plot(n,fig_counter,fig,u,T_hot,T_cold,dt)

    # Plot output figures
    output.output_plots(fig, im)
