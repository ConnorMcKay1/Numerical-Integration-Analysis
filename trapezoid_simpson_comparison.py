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

def slices():
    print("\n ENTERING: slices")

    # start / stop for function, it sets the boundaries of the integral
    start_integral = -3
    stop_integral = 3
    slices_per_integral = None
    
    
    # [SYMBOLIC PSEUDO] this is for the list of "# of slices" to be computed
    # esentially it will make a, list of lists [4, 8, 12, 16, . . . n]
    start_slice_amount = 4
    stop_slice_amount = 20
    slice_amount_step = 4
    
    slice_list = [] # list containing number of slices, ex: [4, 8, 12, 16, . . . n]
    
    
    for slice_amount in range(start_slice_amount, stop_slice_amount + 1, slice_amount_step):
        slice_list.append(slice_amount)
        
    print(slice_list)
    
    np_slice_list = np.array(slice_list) # again converst list to np array
    
    trapezoid_result_list = [] # list of x/slice values, ex: [-3.  -2.6 -2.2 -1.8 -1.4 -1.  -0.6 -0.2 
                               #                               0.2  0.6  1.  1.4  1.8  2.2   2.6  3. ]
    
    for number_of_slices in (np_slice_list):
        slices = np.linspace(start_integral, stop_integral, number_of_slices)# number of for that step  + 1)
        trapezoid_result_list.append(slices)


    # this loop will print out the slice_amount with it's corresponding number_of_slices 
    for slice_amount, number_of_slices in zip(slice_list, trapezoid_result_list):
        print(
              f"Slice Amount: {slice_amount}\n"
              f"Number of Slices: {number_of_slices}\n"
        )


    # for slice_amount, number_of_slices in slice_list, trapezoid_result_list:
    #     print(f"Slice Amount: {slice_amount} \n Number of Slices: {trapezoid_result_list} \n ")
    
    # for slices in (np_slice_list):
    #     print("Numbers:",slices)
    #     _, trap_result = trapezoid_method(f1, slices)
    #     trapezoid_result_list.append(trap_result)

    
    
    
    return slice_list
    


def trapezoid_results(f1, slice_list):
    print("\n ENTERING: trapezoid_results")
    
    trapezoid_result_list = []

    
    # for slices in slice_list:
    #     _, trap_result = trapezoid_method(f1, slices)
    #     trapezoid_result_list.append(trap_result)
        
    print(trapezoid_result_list)



def main():
    print("Going Through Entry Point")
    
    slice_list = slices()
    trapezoid_results(f1, slice_list)

if __name__ == "__main__":
   main()



