"""Plotting functions for the diffusion simulation."""

import matplotlib.pyplot as plt


def create_plot(fig, temperature, timestep, dt, subplot_number, T_cold=300, T_hot=700):
    """Add one temperature plot to ``fig`` and return its image."""
    ax = fig.add_subplot(220 + subplot_number)
    image = ax.imshow(
        temperature.copy(),
        cmap=plt.get_cmap("hot"),
        vmin=T_cold,
        vmax=T_hot,
    )
    ax.set_axis_off()
    ax.set_title("{:.1f} ms".format(timestep * dt * 1000))
    return image


def output_plots(fig, image):
    """Add the shared colour bar and display the completed figure."""
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel("$T$ / K", labelpad=20)
    fig.colorbar(image, cax=cbar_ax)
    plt.show()
