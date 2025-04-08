import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from src import score_avg

def test_score_avg():
    return score_avg(0,70,[1,1])

def test_mapping():
    N = 100
    x = np.linspace(-170,170,N)
    y = np.linspace(-170,170,N)
    
    res = np.zeros((N,N))
    sigma = [1,1]
    for yi in range(N):
        print(yi)
        for xi in range(N):
            res[xi,yi] =  score_avg(x[xi],y[yi],sigma)

    # plt.scatter(x,y,c=res)
    plt.pcolormesh(res)
    plt.show()

# print(test_score_avg())

test_mapping()