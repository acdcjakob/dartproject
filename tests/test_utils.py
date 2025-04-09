import numpy as np
import matplotlib.pyplot as plt

from dartproject.utils import cart2pol
from dartproject.utils import gaussian
from dartproject.utils import monte_carlo_uniform
from dartproject.utils import monte_carlo_general

from dartproject.scoring import calc_score

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

    print(monte_carlo_uniform(passableFunction,[[-6,6],[-6,6]],1_000)[0])

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

def test_monte_carlo_general_square():
    '''
    This tests checks whether integrating over a square [-1,+1]x[-1,+1] yields the expected result of 4
    '''
    t = [0,0]
    sigma = [1,1]
    N = 1_000_000
    rng = np.random.default_rng()
    samples_x = rng.normal(t[0],sigma[0],(N,1))
    samples_y = rng.normal(t[1],sigma[1],(N,1))

    samples = np.hstack([samples_x,samples_y])

    def stepfun(x,y):
        if abs(x) > 1 or abs(y) > 1:
            return 0
        else:
            return (1/gaussian(x,t[0],sigma[0])/gaussian(y,t[1],sigma[1]))
        
    assert abs(monte_carlo_general(stepfun,samples)-4) < 0.1
    
    if False:
        plt.scatter(samples_x,samples_y,c=[float(stepfun(xi[0],yi[0])) for xi,yi in zip(samples_x,samples_y)]) 
        plt.colorbar()
        plt.show()
    


def test_monte_carlo_general_score():
    '''
    This test checks whether aiming at triple 20 yields 60 points with sufficient accuracy of sigma = 1 in both directions
    '''
    # create samples
    t = [0,103.5]
    sigma = [1,1]
    N = 1_000
    rng = np.random.default_rng()
    samples_x = rng.normal(t[0],sigma[0],(N,1))
    samples_y = rng.normal(t[1],sigma[1],(N,1))

    # create passable function

    samples = np.hstack([samples_x,samples_y])

    assert abs(monte_carlo_general(calc_score,samples)-60)<0.5


if __name__ == '__main__':
    print(test_monte_carlo_general_square())
    # print(test_monte_carlo_general_score())


