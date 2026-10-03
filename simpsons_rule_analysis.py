import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt



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
   number_of_slices = 4
   x2 = 3
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
   



def simpsons_rule(f1, slices):
    print("Entering Simpson's Rule")
    y = f1(slices)
    I1 = integrate.simpson(y, slices)
    print(f"Simpson's Rule result: *{I1}*")
    return slices, y



# GAUSS-KRONROD METHOD (for accuracy testing)
def gauss_kronrod_method(f1):
   I2 = integrate.quad(f1, -3, 3)
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
          title=(
            'Trapezoid Method\n'
            + (rf"$\int_{{{min:.6g}}}^{{{max:.6g}}} {f.__doc__}\,dx$"
               if f.__doc__
               else rf"$\int_{{{min:.6g}}}^{{{max:.6g}}} {f.__name__}(x)\,dx$"
              )
            + f" | # of slices: {len(slices)}"
            )
         )
   ax.grid(alpha = .5, linestyle = 'dashed')
   ax.margins(0.5)

   plt.show()






def main():
   print("Going Through Entry Point")
    
   slices = slice_controler()
   #simpsons_rule(f1, slices)
    
   _, y = simpsons_rule(f1, slices)
   gauss_kronrod_method(f1)
   
   
   display(f1, slices, y)


if __name__ == "__main__":
   main()