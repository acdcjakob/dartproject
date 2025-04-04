import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from src import score_avg

def test_score_avg():
    score_avg(0,100,[1,1])
    print(score_avg)

# test_score_avg()

# y = np.array([0,4,7,10,14,18,25,30,40,60,80,95,98,100,103,106,109,115,120])
# I = [score_avg(0,yi,[1,1]) for yi in y]