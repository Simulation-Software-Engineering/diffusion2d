"""Solve the two-dimensional diffusion equation."""

import numpy as np

from .output import create_plot, output_plots


def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    """Advance the temperature field by one timestep."""
    u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
        (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
        + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2
    )

    return u.copy(), u


def solve(dx=0.1, dy=0.1, D=4.0):
    """Run the simulation and display the temperature plots.

    Parameters
    ----------
    dx, dy : float
        Grid spacing in the x and y directions, in millimetres.
    D : float
        Thermal diffusivity, in square millimetres per second.
    """
    if dx <= 0 or dy <= 0 or D <= 0:
        raise ValueError("dx, dy and D must be positive")

    w = h = 10.0
    T_cold = 300
    T_hot = 700
    nx, ny = int(w / dx), int(h / dy)
    if nx < 3 or ny < 3:
        raise ValueError("dx and dy must produce at least three grid points")

    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    print("dt = {}".format(dt))

    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    r = min(h, w) / 4.0
    cx = w / 2.0
    cy = h / 2.0
    r2 = r**2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot

    nsteps = 101
    n_output = [0, 10, 50, 100]
    fig_counter = 0
    import matplotlib.pyplot as plt

    fig = plt.figure()
    im = None
    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)
        if n in n_output:
            fig_counter += 1
            im = create_plot(
                fig, u, n, dt, fig_counter, T_cold=T_cold, T_hot=T_hot
            )

    output_plots(fig, im)
