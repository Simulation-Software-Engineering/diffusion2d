import matplotlib.pyplot as plt


def create_plot(fig, fig_counter, u, T_cold, T_hot, n, dt):
    ax = fig.add_subplot(220 + fig_counter)
    ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title(f'{n * dt * 1000:.1f} ms')


def output_plots(fig):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(fig.axes[0].images[0], cax=cbar_ax)
    plt.show()
