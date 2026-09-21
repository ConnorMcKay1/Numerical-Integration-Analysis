'''
LIST OF VARIOUS IMPORTS/PACKAGES/LIBRARIES

import scipy.integrate as integrate
import scipy.special as special
from numpy import sqrt, sin, cos, pi

'''

import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np

from numerical_integration_analysis import slice_connecting

print("whats up bro?")


def temp():
    print("\n ENTERING TEMP")




def display():
    print("\n ENTERING DISPLAY")
   
    for x0, y0, m in zip(x, y, slopes):
        x_line = np.linspace(x0 - 2, x0 + 2, 100)
        y_line = m * (x_line - x0) + y0

        plt.plot(x_line, y_line)
   
   
   
   
temp()