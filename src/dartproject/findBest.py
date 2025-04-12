import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()

# from .scoring import score_avg_integrand
# from .utils import monte_carlo_uniform

from .scoring import calc_score
from .utils import monte_carlo_general
from .utils import pol2cart
from .utils import gaussian

# def score_avg(t_x: float, t_y: float, sigma: np.ndarray) -> float:
#     range = [(t_x-3*np.sqrt(sigma[0]), t_x+3*np.sqrt(sigma[0])), (t_y-3*np.sqrt(sigma[1]), t_y+3*np.sqrt(sigma[1]))]
#     I = sp.integrate.dblquad(score_avg_integrand,*range[0],*range[1],args=(t_x,t_y,sigma))
#     return I

# def score_avg(t_x: float, t_y: float, sigma: np.ndarray) -> float:

#     passToMonteCarlo = lambda h_x, h_y: score_avg_integrand(h_x,h_y,t_x,t_y,sigma)

#     lim_mult = 6
#     sample_number = 1000000

#     limits = [[t_x - lim_mult*sigma[0], t_x + lim_mult*sigma[0]],
#               [t_y - lim_mult*sigma[1], t_y + lim_mult*sigma[1]]]

#     return monte_carlo_uniform(passToMonteCarlo,limits,sample_number)[0]

def score_avg(t_x: float, t_y: float, sigma: list) -> float:
    N = 1_000 # sampling number
    samples_x = rng.normal(t_x,sigma[0],(N,1))
    samples_y = rng.normal(t_y,sigma[1],(N,2))
    samples = np.hstack([samples_x,samples_y])

    result = monte_carlo_general(calc_score,samples)

    return result

def scan_dartboard(sigma: list, N = 50) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    '''
    Returns a tuple of 3 arrays:
    `x` ... `N` x 1 array of sampled x-values
    `y` ... `N` x 1 array of sampled y-values
    `result` ... N x N array of averaged scores
    '''
    x = np.linspace(-170,170,N).reshape(-1,1)
    y = np.linspace(-170,170,N).reshape(-1,1)

    doCalc = np.zeros((N,N))
    # result = np.nan((N,N))
    result = np.full((N,N),np.nan)

    cart_flatten = np.zeros((N**2,2))
    result_flatten = np.zeros((N**2,1))
    idx_flatten = 0
    for xi in range(len(x)):
        print(f'Row: {xi}/{N-1}')
        for yi in range(len(y)):
            if np.sqrt(x[xi]**2+y[yi]**2) > 175:
                # doCalc[xi,yi] = False
                continue
            result[yi,xi] = score_avg(x[xi],y[yi],sigma)
            
            # result_flatten[idx_flatten] = result[xi,yi]
            # cart_flatten[idx_flatten,0] = x[xi,0]
            # cart_flatten[idx_flatten,1] = y[yi,0]
            # idx_flatten += 1
    
    return x, y, result


def plot_result(x,y,result,ax = None):
    if ax == None:
        ax = plt.axes()
    colorPlot = ax.pcolor(x.flatten(),y.flatten(),result)
    ax.set_aspect('equal') 
    # plt.show()
    return colorPlot

def create_overview(sigma: list,N = 20,fig = None) -> None:
    if fig == None:
        fig = plt.figure(figsize=(10,4))

    axs = fig.subplot_mosaic([
        ["x-gauss", "dartboard",   "y-gauss"]
    ])
    fig.subplots_adjust(wspace=.5)
    
    for ax in axs.values():
        ax.set_box_aspect(1)  # Set the aspect ratio to be square

    x,y,results = scan_dartboard(sigma,N)
    pcolor = plot_result(x,y,results,axs["dartboard"])
    # plt.show()

    plot_gauss(x,sigma,direction = 'x',ax=axs["x-gauss"])
    plot_gauss(x,sigma,direction = 'y',ax=axs["y-gauss"])


    cbar = fig.colorbar(pcolor,ax=axs["dartboard"],shrink = .5)
    cbar.set_label('Score')
    # cbar.ax.set_aspect(20)  # Adjust the aspect ratio of the colorbar
    # cbar.ax.set_box_aspect(axs["dartboard"].get_position().height / cbar.ax.get_position().height)
    # labelling
    axs["x-gauss"].set_yticklabels([])
    axs["y-gauss"].yaxis.tick_right()
    axs["y-gauss"].set_xticklabels([])

    xL = "$x\\ (\\mathrm{mm})$"
    yL = "$y\\ (\\mathrm{mm})$"
    axs["dartboard"].set_xlabel(xL)
    axs["dartboard"].set_ylabel(yL)
    axs["x-gauss"].set_xlabel(xL)
    axs["y-gauss"].yaxis.set_label_position("right")
    axs["y-gauss"].set_ylabel(yL)

    axs["x-gauss"].set_title('Distribution along $x$')
    axs["y-gauss"].set_title('Distribution along $y$')

    # find max
    max_value = np.nanmax(results)
    xMax, yMax = np.unravel_index(np.nanargmax(results), results.shape)
    axs["dartboard"].scatter(y[yMax][0],x[xMax][0],marker='x',color='red')
    print(x[xMax][0])

def plot_gauss(x: np.ndarray, sigma: list, direction = 'x', ax = None):
    if ax == None:
        ax = plt.axes()
    
    if direction == 'x':
        s = sigma[0]
    elif direction == 'y':
        s = sigma[1]

    location = np.linspace(np.min(x),np.max(x),1000)
    gauss = [gaussian(loci,(np.max(x)+np.min(x))/2,s) for loci in location]
    if direction == 'x':
        ax.plot(location, gauss)
    elif direction == 'y':
        ax.plot(gauss,location)