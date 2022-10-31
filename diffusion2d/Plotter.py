from matplotlib import pyplot as plt
import numpy as np
import math


class Plotter:
    def __init__(self,
                 T_cold: float,
                 T_hot: float,
                 total_figure_count: int) -> None:
        self._fig_counter = 0
        self._latest_axis_img = None
        self._total_figure_count = total_figure_count
        self._fig = plt.figure()
        self.T_cold = T_cold
        self.T_hot = T_hot

        self.col_count = math.ceil(math.sqrt(total_figure_count))
        self.row_count = math.floor(math.sqrt(total_figure_count))

    def create_plot(self,
                    data: np.ndarray,
                    step: int,
                    delta_time: float):

        self._fig_counter += 1
        ax = self._fig.add_subplot(
            self.row_count*100 + self.col_count*10 + self._fig_counter)
        self._latest_axis_img = ax.imshow(data.copy(), cmap=plt.get_cmap('hot'),
                                          vmin=self.T_cold, vmax=self.T_hot)  # image for color bar axes
        ax.set_axis_off()
        ax.set_title('{:.1f} ms'.format(step * delta_time * 1000))

    def output_plots(self):

        if (self._latest_axis_img is None):
            raise Exception("No plots have been created yet")

        self._fig.subplots_adjust(right=0.85)
        cbar_ax = self._fig.add_axes([0.9, 0.15, 0.03, 0.7])
        cbar_ax.set_xlabel('$T$ / K', labelpad=20)
        self._fig.colorbar(self._latest_axis_img, cax=cbar_ax)
        plt.savefig("out.png")
