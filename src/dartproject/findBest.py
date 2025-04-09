import scipy as sp
import numpy as np
from .scoring import score_avg_integrand
from .utils import monte_carlo

# def score_avg(t_x: float, t_y: float, sigma: np.ndarray) -> float:
#     range = [(t_x-3*np.sqrt(sigma[0]), t_x+3*np.sqrt(sigma[0])), (t_y-3*np.sqrt(sigma[1]), t_y+3*np.sqrt(sigma[1]))]
#     I = sp.integrate.dblquad(score_avg_integrand,*range[0],*range[1],args=(t_x,t_y,sigma))
#     return I

def score_avg(t_x: float, t_y: float, sigma: np.ndarray) -> float:

    passToMonteCarlo = lambda h_x, h_y: score_avg_integrand(h_x,h_y,t_x,t_y,sigma)

    lim_mult = 6
    sample_number = 1000000

    limits = [[t_x - lim_mult*sigma[0], t_x + lim_mult*sigma[0]],
              [t_y - lim_mult*sigma[1], t_y + lim_mult*sigma[1]]]

    return monte_carlo(passToMonteCarlo,limits,sample_number)[0]