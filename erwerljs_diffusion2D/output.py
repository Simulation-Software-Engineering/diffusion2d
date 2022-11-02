import matplotlib.pyplot as plt
import numpy as np


def create_plot(fig, fig_counter: int, T_cold: int, T_hot: int, n: int,
                dt: float, u: np.matrix):
    """
    Creates a new subplot under `fig` at position `fig_counter`
    """
    ax = fig.add_subplot(220 + fig_counter)
    # image for color bar axes
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return im


def output_plots(fig, im):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
