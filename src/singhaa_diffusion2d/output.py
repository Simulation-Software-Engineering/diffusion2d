import matplotlib.pyplot as plt

def create_plot(fig, fig_counter, dt, T, title):
    """
    Creates a single plot within the figure for a specific timestamp.
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(T.copy(), cmap=plt.get_cmap('hot'), vmin=0, vmax=100)  
    ax.set_axis_off()
    ax.set_title(f'{title}\nTime: {dt*1000:.1f} ms')
    return im

def output_plots(fig, im):
    """
    Finalizes and displays/saves the figure.
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()