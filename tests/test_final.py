import numpy as np
import matplotlib.pyplot as plt

from dartproject.findBest import create_overview

def test_create_overview():
    fig = plt.figure(figsize=(10,10))
    create_overview([15,15],N = 30,fig = fig)
    plt.show()