import matplotlib.pyplot as plt

def create_plot(fig,fig_counter,v_min,v_max,u,n,dt):
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=v_min, vmax=v_max)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return im
    
def output_plots(fig,im):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.savefig('diffusion2d_after_refactor.png')
    plt.show()