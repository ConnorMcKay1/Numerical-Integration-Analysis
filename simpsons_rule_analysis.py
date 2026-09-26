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
   number_of_slices = 15
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
    print(f"Simpson's Rule result: {I1}|")





def main():
    print("Going Through Entry Point")
    
    slices = slice_controler()
    simpsons_rule(f1, slices)


if __name__ == "__main__":
   main()