import scipy as sp
import numpy as np
rng = np.random.default_rng()

# from .scoring import score_avg_integrand
# from .utils import monte_carlo_uniform

from .scoring import calc_score
from .utils import monte_carlo_general

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

