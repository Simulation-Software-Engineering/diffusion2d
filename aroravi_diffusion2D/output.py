# added output functions
import matplotlib.pyplot as plt

def output_plots(fig, im):
    """
    Subplots
    -------
    """
    fig.subplots_adjust(right=0.85)
    #define axes
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    #set labels
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()

def create_plot(fig_counter, dt, u, n, T_cold, T_hot, fig):
    """
    Plot
    Creation
    -------
    """
    fig_counter += 1
    ax = fig.add_subplot(220 + fig_counter)
    # image for color axes
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return fig_counter, im
