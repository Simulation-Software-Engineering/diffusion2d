import matplotlib.pyplot as plt

def create_plot(n, fig_counter, fig, u, T_hot, T_cold, dt):	    
    
    fig_counter += 1
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for col>
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
                
    return im, fig_counter


def output_plots(fig, im):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
