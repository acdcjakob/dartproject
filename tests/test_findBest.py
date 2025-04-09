import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from dartproject.findBest import score_avg

# def test_score_avg():
#     return score_avg(0,70,[1,1])

# def test_mapping():
#     N = 100
#     x = np.linspace(-170,170,N)
#     y = np.linspace(-170,170,N)
    
#     res = np.zeros((N,N))
#     sigma = [1,1]
#     for yi in range(N):
#         print(yi)
#         for xi in range(N):
#             res[xi,yi] =  score_avg(x[xi],y[yi],sigma)

#     # plt.scatter(x,y,c=res)
#     plt.pcolormesh(res)
#     plt.show()

# # print(test_score_avg())

# test_mapping()

def test_score_avg_givesFloat():
    A = [[0,0],[0,102],[102,0],[60,60],[0,-102]]
    sigma = [0.1,0.1]
    for a in A:
        print(f'aim at {a}:',f'{score_avg(*a,sigma):.2f}')
        assert abs(score_avg(*a,sigma)) >= 0

def test_score_avg_reproducibility60():
    a = [0,102]
    sigma = [0.01,0.01]

    for i in range(5):
        print(f'aim at {a}:',f'{score_avg(*a,sigma):.2f}')
        assert abs(score_avg(*a,sigma)-60) <= 2

test_score_avg_reproducibility60()