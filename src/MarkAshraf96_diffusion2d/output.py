# import imp
import matplotlib.pyplot as plt

def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    # Propagate with forward-difference in time, central-difference in space
    u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
            (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
            + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)

    u_nm1 = u.copy()
    return u_nm1, u


T_cold = 300
T_hot = 700
n = 101
dt = 0.0006250000000000001


def create_plot(u_nm1, u, D, dt, dx2, dy2):
        do_timestep(u_nm1, u, D, dt, dx2, dy2)
        fig = plt.figure()
        ax = fig.add_subplot()
        im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
        ax.set_axis_off()
        ax.set_title('{:.1f} ms'.format(n * dt * 1000))
        # Plot output figures
        fig.subplots_adjust(right=0.85)
        cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
        cbar_ax.set_xlabel('$T$ / K', labelpad=20)
        fig.colorbar(im, cax=cbar_ax)
        plt.show()


def output_plots(nsteps, n_output, u0, u, D, dt, dx2, dy2):
        fig = plt.figure()
        fig_counter = 0
        for n in range(nsteps):
                u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

                if n in n_output:
                        fig_counter += 1
                        ax = fig.add_subplot(220 + fig_counter)
                        im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
                        ax.set_axis_off()
                        ax.set_title('{:.1f} ms'.format(n * dt * 1000))

        # # Plot output figures
        fig.subplots_adjust(right=0.85)
        cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
        cbar_ax.set_xlabel('$T$ / K', labelpad=20)
        fig.colorbar(im, cax=cbar_ax)
        plt.show()
  


# create_plot()