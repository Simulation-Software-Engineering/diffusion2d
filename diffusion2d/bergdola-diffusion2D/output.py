import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def create_plot(fig,u,T_cold,T_hot,title):    
    ax = fig.add_subplot(111) # the actual position will be assigned later
    ax.set_axis_off()
    ax.set_title(title)
    img = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    return (ax,img) # return both as img is needed for setting the color bar 

def output_plots(fig, images):
    """output all the four plots as one figure"""
    num_rows = (len(images)+1)/2 # round up
    gs = gridspec.GridSpec(2,2)
    for fig_counter,(ax,img) in enumerate(images):
        ax.set_position(gs[fig_counter].get_position(fig))
        ax.set_subplotspec(gs[fig_counter]) 
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(images[0][1], cax=cbar_ax)
    plt.show()