"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""

import numpy as np
import matplotlib.pyplot as plt
from output import create_plot, output_plots


def solve(dx = 0.1, dy = 0.1, D = 4.):
    # plate size, mm
    w = h = 10.
    # intervals in x-, y- directions, mm
    # dx = dy = 0.1
    # Thermal diffusivity of steel, mm^2/s
    # D = 4.

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

    # Number of timesteps
    nsteps = 101
    # Output 4 figures at these timesteps
    n_output = [0, 10, 50, 100]

    create_plot(u0, u, D, dt, dx2, dy2)

    output_plots(nsteps,n_output,u0, u, D, dt, dx2, dy2 )

solve()