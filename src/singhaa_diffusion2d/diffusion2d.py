# diffusion2d.py
import numpy as np
import matplotlib.pyplot as plt
from .output import create_plot, output_plots

def solve(dx=0.1, dy=0.1, D=4.0):
    """
    Runs the diffusion simulation.
    
    Parameters:
    dx (float): Grid spacing in x-direction
    dy (float): Grid spacing in y-direction
    D (float): Thermal diffusivity
    """
    # Plate size, mm
    w = h = 10.

    # Thermal diffusivity of steel, mm^2.s^-1
    # D is passed as argument now

    T_cool, T_hot = 300, 700

    # Number of discrete mesh points in X and Y directions
    nx, ny = int(w / dx), int(h / dy)

    # Computing a stable time step
    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    print("dt = {}".format(dt))

    u0 = T_cool * np.ones((nx, ny))
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
                (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2 +
                (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)

        u0 = u.copy()
        return u0, u

    # Number of timesteps
    nsteps = 101

    # Output 4 figures at these timesteps
    mfig = [0, 10, 50, 100]
    fignum = 0
    fig = plt.figure()
    
    # Track the last image for the colorbar
    im = None

    for m in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)
        if m in mfig:
            fignum += 1
            print(m, fignum)
            im = create_plot(fig, fignum, dt*m, u, 'Diffusion 2D')

    output_plots(fig, im)