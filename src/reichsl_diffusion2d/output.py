import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.image import AxesImage
from numpy import ndarray


def create_plot(fig: Figure, u: ndarray, v_min: int, v_max: int, title: str, subplot_num: int) -> AxesImage:
    ax = fig.add_subplot(220 + subplot_num)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=v_min, vmax=v_max)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title(title)
    return im


def output_plots(fig: Figure, im: AxesImage) -> None:
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()

