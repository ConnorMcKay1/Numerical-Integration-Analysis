import scipy.integrate as integrate
from numpy import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt

from trapezoid_method_analysis import trapezoid_method
from simpsons_rule_analysis import simpsons_rule
      
      
print("TRAPEZOID_SIMPSON_COMPARISON.py")

# create array of slices, from i = 4, i + 4, till i <= 100
#
# pass them in to the TRAP & SIMP function for getting results
#
# use actual GAUSS to form a baseline for result (X axis) 
#
# plot the results as the slices changes and approach the actual/baseline
#
## find the difference between both of the results for each respective slice
#


#f(x)=x^{4}-5x^{2}+10
#f(x)=((x**4) - (5*(x**2)) + 10)X
def f1(x):
   """x^4 - 5x^2 + 10"""
   return ((x**4) - (5*(x**2)) + 10)

# SLICE CONTROLLER: used for 
def slice_controller():
    print("\n ENTERING: slice_controler")
    number_of_slices = 16
    a = -3
    b = 3
    slices = np.linspace(a, b, number_of_slices + 1)
        
    return a, b, slices


def slices():
    print("\n ENTERING: slices")

    start = -4
    stop = 4
    step = 2
    slice_list = []
    
    for i in range(start, stop + 1, step):
        slice_list.append(i)
    print(slice_list)
    
    return slice_list
    


def trapezoid_results(f1, slice_list):
    print("\n ENTERING: trapezoid_results")

    print(slice_list)    
    trapezoid_result_list = []
    slices = np.array(slice_list)

    for i in slices:
        print(i)

    # for slices in slice_list:
    #     _, trap_result = trapezoid_method(f1, slices)
    #     trapezoid_result_list.append(trap_result)
        
    #print(trapezoid_result_list)



def main():
    print("Going Through Entry Point")
    
    slice_list = slices()
    trapezoid_results(f1, slice_list)

if __name__ == "__main__":
   main()



