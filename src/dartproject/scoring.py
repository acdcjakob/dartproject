import numpy as np
from .utils import cart2pol
from .utils import gaussian

def score_avg_integrand(h_x: float, h_y: float, t_x: float, t_y: float, sigma: np.ndarray) -> float:
    return gaussian(h_x, t_x, sigma[0])*gaussian(h_y, t_y, sigma[1])*calc_score(h_x, h_y)

def calc_score(h_x: float, h_y: float) -> int:
    h_phi, h_r = cart2pol(h_x, h_y)
    
    return calc_score_phi(h_phi)*calc_score_r(h_r)[1]+calc_score_r(h_r)[0]

def calc_score_phi(h_phi: float) -> int:
    zone_score = np.array([
        6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10
    ])
    zone_N = 20
    zone_rad = 2*np.pi / zone_N

    # convert to only-positive angles:
    if h_phi < 0:
        h_phi += 2*np.pi

    # check the zone:
    zone_idx = int(np.floor((h_phi+ zone_rad/2) / zone_rad))

    if zone_idx > 19:
        zone_idx = 0   

    
    # return zone_score[zone_idx]
    return int(zone_score[zone_idx])

def calc_score_r(h_r: float) -> tuple:
    # dimensions in mm:
    BULL_INNER = 12.7 / 2
    BULL_OUTER = 32 / 2

    TRIPLE_OUTER = 107
    TRIPLE_INNER = TRIPLE_OUTER - 8

    DOUBLE_OUTER = 170
    DOUBLE_INNER = DOUBLE_OUTER - 8

    # the return value is an absolute value and a multiplier
    if h_r < 0:
        raise ValueError('Radius cannot be negative!')
    
    if h_r <= BULL_INNER:
        return 50, 0  # Bullseye inner
    
    elif h_r <= BULL_OUTER:
        return 25, 0  # Bullseye outer
    
    elif TRIPLE_INNER <= h_r <= TRIPLE_OUTER:
        return 0, 3  # Triple ring
    
    elif DOUBLE_INNER <= h_r <= DOUBLE_OUTER:
        return 0, 2  # Double ring
    
    elif h_r > DOUBLE_OUTER:
        return 0, 0  # Outside the board
    
    else:
        return 0, 1  # Single ring