import scipy as sp
import numpy as np
from .scoring import score_avg_integrand

def score_avg(t_x: float, t_y: float, sigma: np.ndarray) -> float:
    range = [(t_x-100, t_x+100), (t_y-100, t_y+100)]
    I = sp.integrate.dblquad(score_avg_integrand,*range[0],*range[1],args=(t_x,t_y,sigma))
    return I