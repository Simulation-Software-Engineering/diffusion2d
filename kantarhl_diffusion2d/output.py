"""Plotting helpers for the two-dimensional diffusion simulation."""

import matplotlib.pyplot as plt


def create_plot(fig, temperature, step, dt, plot_number, T_cold, T_hot):
    """Add one temperature snapshot to the four-panel figure.

    Returns the Matplotlib image needed for the shared color bar.
    """
    ax = fig.add_subplot(220 + plot_number)
    image = ax.imshow(
        temperature.copy(),
        cmap=plt.get_cmap("hot"),
        vmin=T_cold,
        vmax=T_hot,
    )
    ax.set_axis_off()
    ax.set_title("{:.1f} ms".format(step * dt * 1000))
    return image


def output_plots(fig, image):
    """Add the common color bar and show the completed figure."""
    fig.subplots_adjust(right=0.85)
    colorbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    colorbar_ax.set_xlabel("$T$ / K", labelpad=20)
    fig.colorbar(image, cax=colorbar_ax)
    plt.show()
