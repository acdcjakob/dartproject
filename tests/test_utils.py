import numpy as np
import matplotlib.pyplot as plt

from dartproject.utils import cart2pol
from dartproject.utils import gaussian
from dartproject.utils import monte_carlo

# def test_cart2pol():
#     h_x = 0
#     h_y = np.linspace(-200,200,1000)

#     phi = np.array([cart2pol(h_x,hi)[0] for hi in h_y])
#     plt.plot(h_y,phi*180/np.pi)
#     plt.yticks(np.arange(-90,91,10))
#     plt.grid()
#     plt.show()

# def test_gaussian():
#     sigma = 5
#     t_x = 102
#     h_x = np.linspace(70,130,100)
#     prb = np.array([gaussian(hi,t_x,sigma) for hi in h_x])

#     plt.plot(h_x,prb)
#     plt.show()

# def test_monte_carlo():
#     foo = lambda x,y: np.sin(x+y) if x*y<=0 else np.exp(x-y)
#     N = 4000

#     return monte_carlo(foo,[[-1,1],[-1,1]],10000)

def test_monte_carlo_gauss():
    '''
    Integrating over 2D gauss should yield a result of approx. 1
    '''
    from dartproject.utils import gaussian
    r = [0,0]
    s = [1,1]
    passableFunction = lambda x,y: gaussian(x,r[0],s[0])*gaussian(y,r[1],s[1])

    print(monte_carlo(passableFunction,[[-6,6],[-6,6]],1_000)[0])

# def check_that_mc_is_gauss():
#     from dartproject.utils import gaussian

#     r = [0,0]
#     s = [1,1]
#     passableFunction = lambda x,y: gaussian(x,r[0],s[0])*gaussian(y,r[1],s[1])
    
#     NN = 1000
#     results = np.zeros((NN,1))
#     for i in range(NN):
#         results[i,0] = monte_carlo(passableFunction,[[-6,6],[-6,6]],1000)[0]
#         # print('.')
    
#     plt.hist(results,bins=30)
#     plt.show()

#     # -> central limit theorem
