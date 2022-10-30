#create 2 functions create_plot() and output_plots()
#create_plot() should create one plot for a particular time stamp
#output_plots() should output all the four plots as one figure

import matplotlib.pyplot as plt

def create_plot(fig, fig_counter, u, T_cold, T_hot, n, dt):
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return fig_counter, im

def output_plots(fig, im):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
    plt.savefig('figures/diffusion2d.pdf')
