from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.image import AxesImage


def create_plot(fig: Figure, fig_counter: int, T_cold: int, T_hot: int, n: int, dt: float, u: np.ndarray) -> Tuple[int, AxesImage]:
    """
    Create one plot for one timepoint

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to add the plot to.
    fig_counter : int
        The counter of plots we have drawn

    Returns
    -------
    int : The counter of plots we have drawn
    matplotlib.AxesImage.AxesImage : The axes image created for this plot
    """
    fig_counter += 1
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))

    return fig_counter, im


def output_plots(fig: Figure, ax_im: AxesImage):
    """
    Output the given figure containing the plots.

    ax_im should be a matplotlib.AxesImage.AxesImage for the colorbar
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(ax_im, cax=cbar_ax)
    plt.show()
