import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from dartproject.findBest import score_avg
from dartproject.findBest import scan_dartboard
from dartproject.findBest import plot_result
from dartproject.findBest import create_overview
from dartproject.findBest import plot_gauss

def test_score_avg_gives60():
    assert abs(score_avg(0,103,[.5,.5])-60)<0.1

def test_score_avg_gives0():
    assert abs(score_avg(0,200,[.5,.5]))<0.1
    assert abs(score_avg(-200,-200,[.5,.5]))<0.1
    assert abs(score_avg(-200,200,[.5,.5]))<0.1

def test_fastTest():
    scan_dartboard([1,1],10)

def test_scan_dartboard_outputShape():
    '''
    check if the dimensions of output are okay
    '''
    N = 10
    x, y, results = scan_dartboard([1,1],N)

    assert x.shape == (N,1)
    assert y.shape == (N,1)
    assert results.shape == (N,N)

def test_plot_result():
    N = 10
    x, y, results = scan_dartboard([1,1],N)

    plot_result(x,y,results)

def test_plot_result_givenAxes():
    N = 10
    x, y, results = scan_dartboard([1,1],N)

    fig = plt.figure()
    axs = fig.subplot_mosaic([
        ["dart",    "y-gauss"],
        ["dart",    "x-gauss"]
    ])
    plot_result(x,y,results,axs["dart"])

def test_create_overview():
    fig = plt.figure()
    create_overview([10,10])
    plt.show()

def test_plot_gauss():
    plot_gauss(np.linspace(0,180,40),[1,1])

def test_plot_gauss_withInputs():
    x, y, _ = scan_dartboard([1,1],10)
    fig = plt.figure()
    ax = fig.add_subplot(122)
    plot_gauss(x,[1,1],ax=ax,direction='y')
    # fig.show()
    # input('PRESS ANY BUTTON ...')