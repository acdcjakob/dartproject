import numpy as np

def calc_score_phi(h_phi: float) -> int:
    zone_score = np.array([
        6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10
    ])
    zone_N = 20
    zone_rad = 2*np.pi / zone_N

    # convert to only-positive angles:
    if h_phi < 0:
        h_phi += 2*np.pi + h_phi

    # check the zone:
    zone_idx = int(np.floor((h_phi+ zone_rad/2) / zone_rad))

    if zone_idx > 19:
        zone_idx = 0   

    
    # return zone_score[zone_idx]
    return zone_score[zone_idx]