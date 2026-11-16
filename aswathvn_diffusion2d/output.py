import matplotlib.pyplot as plt

def create_plot(fig,u,n,dt, T_cold,T_hot,fig_counter):
    """Create one temperature plot at a given timestep."""
    fig_counter += 1
    ax=fig.add_subplot(220 + fig_counter)
    im=ax.imshow(
        u.copy(),
        cmap=plt.get_cmap('hot'),
        vmin=T_cold,
        vmax=T_hot
    )

    ax.set_axis_off()
    ax.set_title(' {:.1f} ms'.format(n * dt*1000))
    return im,fig_counter

def output_plots(fig, im):
    """Display all four temperature plots in one figure."""

    fig.subplots_adjust(right=0.85)

    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)

    fig.colorbar(im, cax=cbar_ax)

    plt.show()