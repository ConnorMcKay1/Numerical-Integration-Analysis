# Connor McKay
# 9/10/26
## The whole goal of this micro-project is to analyze the accuracy of Trapezoidal vs Simpson's rule.

'''
RESEARCH MATERIAL:

"scipy array tip sheet"
https://cac.cornell.edu/myers/teaching/ComputationalMethods/python/arrays.html


'''

import scipy.integrate as integrate
from numpy import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt


print("test test 123")


#f(x)=x^{4}-5x^{2}+4
#f(x)=((x**4) - (5*(x**2)) + 10)
def f1(x):
   return ((x**4) - (5*(x**2)) + 10)

#number of slices
def slice_controler():
   
   return 15




# TRAPEZOID METHOD
def trapezoid_method(f1):
   slices = np.array([-3, -2, -1, 0, 1, 2, 3])
   y = f1(slices)
   I1 = integrate.trapezoid(y, slices)
   #print("\nTRAPAZOID METHOD results:")
   #print(f"|Number of Slices: {slices} | Y-values {y} | Trapezoid method result: {I1}|")
   return slices, y
   
slices, y = trapezoid_method(f1)

# Connecting Trapezoid Slices
def slice_connecting(slices, y):
   print("Entering the slice connecting function")
   
   # takes in the y (for the height)
   # takes in the x (for the slice location)
   # m = y2-y1/(X2-X1) (gives the slope for the line)
   # us slope(m) to draw from y1//x1 to y2//x2   --> didn't end up needing slope

   slopes = []
   
   
   for x2, x1, y2, y1  in zip(slices, slices[1:], y, y[1:]):
      print("slice:", x2, "Next slice:", x1)
      print("value:", y2, "Next value:", y1)
      
      m = (y2-y1)/(x2-x1)
      slopes.append(m)
      
   print("This should be a list of slopes: ", slopes)
   
   return slopes


#slopes = slice_connecting(slices, y)    don't currently need the slopes between the slices
   



# GAUSS-KRONROD METHOD
def gauss_kronrod_method(f1):
   I2 = integrate.quad(f1, 0, 5)
   print("\n Gauss-Kronrod Result:", I2[0])


def display(f, slices):
   print("entering the display function")
   
   x_intputs = np.linspace(-3, 3, 1000)
      
   x_axis = x_intputs
   y_axis = f(x=x_intputs)
   
   fig, ax = plt.subplots()
   
   
   # colours axis red, and places vertical lines for trapezoid slices
   ax.plot(x_axis, y_axis)
   ax.axhline(0, color='red', linewidth=.8, zorder=1)
   ax.axvline(0, color='red', linewidth=.8, zorder=1)
   ax.vlines(
      x=slices,
      ymin=0,
      ymax=y,
      color='springgreen',
      linewidth=.8,
      zorder= 2
   )
   
   
   # draws the lines from one slice to another using slope
   for x1, x2, y1, y2 in zip(slices, slices[1:], y, y[1:]):
      ax.plot(
         [x1, x2],
         [y1, y2],
         color='fuchsia',
         linewidth=1.5
         )

   ax.set(xlabel='STEPS', ylabel='F(x)',
          title='Just trying to test stuff out folks!')
   ax.grid(alpha = .5, linestyle = 'dashed')
   ax.margins(0.5)

   plt.show()
   


#print(slice_controler())

#trapezoid_method(f1)

#gauss_kronrod_method(f1)

#slice_connecting(slices, y)

display(f1, slices)




