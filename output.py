import matplotlib
import matplotlib.pyplot as plt
import numpy.typing as npt


def create_plot(T_cold: float, T_hot: float, dt: float, u: npt.NDArray, fig: matplotlib.figure.Figure, n: int,
                fig_counter: int) -> matplotlib.image.AxesImage:
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return im


def output_plots(fig: matplotlib.figure.Figure, im) -> matplotlib.image.AxesImage:
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
