import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from dartproject.findBest import score_avg

def test_score_avg_gives60():
    assert abs(score_avg(0,103,[.5,.5])-60)<0.1

def test_score_avg_gives0():
    assert abs(score_avg(0,200,[.5,.5]))<0.1
    assert abs(score_avg(-200,-200,[.5,.5]))<0.1
    assert abs(score_avg(-200,200,[.5,.5]))<0.1