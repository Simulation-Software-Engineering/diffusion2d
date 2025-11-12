"""
Helper functions for diffusion2d.

Create and diplay the plots
"""

from matplotlib.image import AxesImage
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from numpy.typing import NDArray


def create_plot(fig: Figure, fig_counter: int, T_cold: int, T_hot: int, dt: float, u: NDArray[np.floating], n: int) -> AxesImage:
    """
    Create a subplot with the current temperature field and title it by time.

    Args:
        fig (Figure): Matplotlib figure to which the subplot is added.
        fig_counter (int): Subplot index used with a 2x2 grid layout
        T_cold (int): Minimum temperature for color scaling (K).
        T_hot (int): Maximum temperature for color scaling (K).
        dt (float): Time step size (s).
        u (NDArray[np.floating]): Temperature field array of shape (nx, ny).
        n (int): Current time step index.

    Returns:
        AxesImage: The image object created by `imshow`, suitable for a
        shared colorbar.
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap("hot"), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title("{:.1f} ms".format(n * dt * 1000))
    return im


def output_plots(fig: Figure, im: AxesImage) -> None:
    """
    Finalize the layout, add a colorbar for the last image, and show the figure.

    Args:
        fig (Figure): Matplotlib figure containing the subplots.
        im (AxesImage): Image handle used to derive the colorbar scaling.

    Returns:
        None
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel("$T$ / K", labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
