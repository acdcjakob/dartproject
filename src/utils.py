import numpy as np

def gaussian(h_i: float,t_i: float,sigma_i: float) -> float:
    if sigma_i == 0:
        if h_i == t_i:
            return 1
        else:
            return 0
    else:
        return 1/(sigma_i*np.sqrt(2*np.pi))*np.exp(-(h_i-t_i)**2/(2*sigma_i**2))
    
def cart2pol(h_x: float, h_y: float) -> tuple:
    # Output is in arctan2 style: -pi ... +pi
    h_r = np.sqrt(h_x**2 + h_y**2)
    h_phi = np.arctan2(h_y, h_x)
    return h_phi, h_r

def pol2cart(h_phi: float, h_r: float) -> tuple:
    h_x = h_r * np.cos(h_phi)
    h_y = h_r * np.sin(h_phi)
    return h_x, h_y

def monte_carlo(fh, limits: list, N = 1000) -> float:
    rng = np.random.default_rng()
    samples = np.hstack([rng.uniform(limits[0][0],limits[0][1],(N,1)),
                        rng.uniform(limits[1][0],limits[1][1],(N,1))])
    
    V = 1
    for i in range(len(limits)):
        V *= abs(limits[i][1]-limits[i][0])

    summands = np.zeros((N,1))
    for i in range(N):
        summands[i] = fh(samples[i,0],samples[i,1])

    if False:
        import matplotlib.pyplot as plt
        x = samples[:,0]
        y = samples[:,1]
        plt.scatter(x, y, c=summands[:, 0], cmap='viridis')
        plt.colorbar(label='Summand Value')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Monte Carlo Summands')
        plt.axis('equal')
        plt.show()
    
    tot = np.sum(summands)
    return tot * V / N