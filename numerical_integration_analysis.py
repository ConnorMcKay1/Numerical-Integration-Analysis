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
   """x^4 - 5x^2 + 10"""
   return ((x**4) - (5*(x**2)) + 10)



# input range --> goes into trap method and display (linespace)
# (x2 - x1)/slice
#number of slices
def slice_controler():
   print("ENTERING: slice_controler")
   number_of_slices = 15
   x2 = 3.5
   x1 = -3
   slice_step_distance = (x2-x1)/number_of_slices
   slices = [x1]
   while len(slices) <= number_of_slices:
      x1 += slice_step_distance
      slices.append(x1)
      
   slices = np.array(slices) #this is just to convert from py list to np array for math
      
   #print("Slice Step Distance: ", slice_step_distance)
   print("List of slices: ", slices)
   
   return slices
   
# TRAPEZOID METHOD
def trapezoid_method(f1, slices):
   print("ENTERING: trapezoid_method")
   #slices = np.array([-3, -2, -1, 0, 1, 2, 3])
   y = f1(slices)
   I1 = integrate.trapezoid(y, slices)
   print(f"Trapezoid method result: {I1}|")
   return slices, y
   
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
      
# GAUSS-KRONROD METHOD
def gauss_kronrod_method(f1):
   I2 = integrate.quad(f1, 0, 5)
   print("\n Gauss-Kronrod Result:", I2[0])

# Displays function, slices(ax.vlines), and connects slices to form trapezoids
def display(f, slices, y):
   print("ENTERING: display")
   
   min, max = slices.min(), slices.max()
   x_intputs = np.linspace(min, max, 1000)
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

   ax.set(xlabel='STEPS', ylabel="F(x)",
          title='Trapezoid Method\n' f"F(x) = ${f.__doc__}$" if f.__doc__ else f"${f.__name__}(x)$")
   ax.grid(alpha = .5, linestyle = 'dashed')
   ax.margins(0.5)

   plt.show()
   


#slice_controler()

#print(slice_controler())

#trapezoid_method(f1, slices)

#gauss_kronrod_method(f1)

#slice_connecting(slices, y)

#display(f1, slices, y)


def main():
   print("Starting Analysis...")
   
   slices = slice_controler()
   
   
   _, y = trapezoid_method(f1, slices)
   gauss_kronrod_method(f1)
   
   
   display(f1, slices, y)

if __name__ == "__main__":
   main()

