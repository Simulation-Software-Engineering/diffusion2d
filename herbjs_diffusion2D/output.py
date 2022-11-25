import matplotlib.pyplot as plt

def create_plot(fig, fig_counter, u, T_cold, T_hot, t):
    """Create a plot with number `fig_counter` in `fig` for the solution `u` at a specific time step.

    Args:
        fig (matplotlib.figure.Figure): matplotlib figure
        fig_counter (int): figure number (0..3)
        u (np.ndarray): NumPy array with the solution `u`
        T_cold (float): lowest temperature
        T_hot (float): highest temperature
        t (float): elapsed time at the timestep in seconds

    Returns:
        fig_counter: figure number
        im: matplotlib image
    """
    fig_counter += 1
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(t * 1000))
    return fig_counter, im

def output_plots(fig, im):
    """Show the plots in the figure `fig` and add a color bar based on `im`

    Args:
        fig (matplotlib.figure.Figure): matplotlib figure which contains the plots
        im (matplotlib image): matplotlib image
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
