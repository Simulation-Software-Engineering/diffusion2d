"""
Output functionality for the 2D diffusion solver: creating and showing plots.
"""

import matplotlib.pyplot as plt


def create_plot(fig, u, n, dt, fig_counter, T_cold, T_hot):
    """
    Create one subplot (one time stamp) inside the given figure.

    :param fig: matplotlib figure to which the subplot is added
    :param u: 2D array with the temperature field at the current time step
    :param n: current time step number
    :param dt: size of one time step in seconds
    :param fig_counter: index of the subplot (1 to 4) in the 2x2 grid
    :param T_cold: lower limit of the color scale
    :param T_hot: upper limit of the color scale
    :return: the figure and the image object (needed for the color bar)
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return fig, im


def output_plots(fig, im):
    """
    Add the shared color bar to the figure and show all plots as one figure.

    :param fig: matplotlib figure containing the subplots
    :param im: image object of one of the subplots, used for the color bar
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()