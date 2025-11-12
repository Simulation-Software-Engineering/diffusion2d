import numpy as np
import matplotlib.pyplot as plt
from .output import create_plot, output_plots


def solve(dx=0.1, dy=0.1, D=4.0):

    w, h = 10.0, 10.0

    dx2, dy2 = dx*dx, dy*dy
    dt = dx2*dy2 / (2.0 * D * (dx2 + dy2))

  
    T_cold, T_hot = 300.0, 700.0

    
    nx, ny = int(w/dx), int(h/dy)

    
    u0 = T_cold * np.ones((ny, nx))
    r = 2.0           
    cx, cy = w/2, h/2 
    for i in range(ny):
        y = i * dy
        for j in range(nx):
            x = j * dx
            if (x - cx)**2 + (y - cy)**2 < r**2:
                u0[i, j] = T_hot

    u = u0.copy()

    alpha_x = D * dt / dx2
    alpha_y = D * dt / dy2

   
    nsteps = 101
    frames = [0, 10, 50, 100]

   
    fig = plt.figure(figsize=(8, 6))
    im_for_cbar = None
    fig_counter = 0  

    for n in range(nsteps):
        u_copy = u.copy()

      
        u[1:-1, 1:-1] = (
            u_copy[1:-1, 1:-1]
            + alpha_x * (u_copy[1:-1, 2:] - 2.0*u_copy[1:-1, 1:-1] + u_copy[1:-1, :-2])
            + alpha_y * (u_copy[2:, 1:-1] - 2.0*u_copy[1:-1, 1:-1] + u_copy[:-2, 1:-1])
        )

        u[0, :]  = T_cold
        u[-1, :] = T_cold
        u[:, 0]  = T_cold
        u[:, -1] = T_cold

       
        if n in frames:
            fig_counter += 1
            t_ms = (n * dt) * 1000.0
            im_for_cbar = create_plot(fig, fig_counter, u, T_cold, T_hot, t_ms)

    if im_for_cbar is not None:
        output_plots(fig, im_for_cbar)
    else:
        plt.close(fig)


if __name__ == "__main__":
    solve()
