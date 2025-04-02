import numpy as np

def gaussian(h_i: float,t_i: float,sigma_i: float) -> float:
    if sigma_i == 0:
        if h_i == t_i:
            return 1
        else:
            return 0
    else:
        return 1/(sigma_i*np.sqrt(2*np.pi))*np.exp(-(h_i-t_i)**2/sigma_i**2)
    
def cart2pol(h_x: float, h_y: float) -> tuple:
    h_r = np.sqrt(h_x**2 + h_y**2)
    h_phi = np.arctan2(h_y, h_x)
    return h_phi, h_r

def pol2cart(h_phi: float, h_r: float) -> tuple:
    h_x = h_r * np.cos(h_phi)
    h_y = h_r * np.sin(h_phi)
    return h_x, h_y