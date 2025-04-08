import numpy as np
import matplotlib.pyplot as plt

from src.utils import cart2pol
from src.utils import gaussian
from src.utils import monte_carlo

def test_cart2pol():
    h_x = 0
    h_y = np.linspace(-200,200,1000)

    phi = np.array([cart2pol(h_x,hi)[0] for hi in h_y])
    plt.plot(h_y,phi*180/np.pi)
    plt.yticks(np.arange(-90,91,10))
    plt.grid()
    plt.show()

def test_gaussian():
    sigma = 5
    t_x = 102
    h_x = np.linspace(70,130,100)
    prb = np.array([gaussian(hi,t_x,sigma) for hi in h_x])

    plt.plot(h_x,prb)
    plt.show()

def test_monte_carlo():
    foo = lambda x,y: np.sin(x+y) if x*y<=0 else np.exp(x-y)
    N = 4000

    return monte_carlo(foo,[[-1,1],[-1,1]],10000)

print(test_monte_carlo())