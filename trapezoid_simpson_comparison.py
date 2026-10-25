import scipy.integrate as integrate
from numpy import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

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

# SLICEs
def slices():
    print("\n ENTERING: slices")

    # start / stop for function, it sets the boundaries of the integral
    start_integral = -3
    stop_integral = 3    
    
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
    
    universal_slice_list = [] # list of x/slice values, ex: [-3.  -2.6 -2.2 -1.8 -1.4 -1.  -0.6 -0.2 
                               #                               0.2  0.6  1.  1.4  1.8  2.2   2.6  3. ]
    
    for number_of_slices in (np_slice_list):
        slices = np.linspace(start_integral, stop_integral, number_of_slices)# number of for that step  + 1)
        universal_slice_list.append(slices)


    # this loop will print out the slice_amount with it's corresponding number_of_slices 
    '''
    for slice_amount, number_of_slices in zip(slice_list, universal_slice_list):
        print(
              f"Slice Amount: {slice_amount}\n"
              f"Number of Slices: {number_of_slices}\n"
        )
    '''
    
    return start_integral, stop_integral, slice_list, universal_slice_list
    

# TRAPEZOID RESULTS
def trapezoid_results(f1, universal_slice_list):
    print("\n ENTERING: trapezoid_results")
            
    trapezoid_results_list = []
    
    for inputs in universal_slice_list:
        _, _, I1 = trapezoid_method(f1, inputs)
        trapezoid_results_list.append(I1)
        #print("Simpson's inputs being added:  ", inputs)

    print("Complete list of Trapezoid Results:  ", trapezoid_results_list)


# SIMPSON'S RESULTS
def simpsons_results(f1, universal_slice_list):
    print("\n ENTERING: simpsons_results")
    
    simpsons_results_list = []
    
    for inputs in universal_slice_list:
        _, _, I1 = simpsons_rule(f1, inputs)
        simpsons_results_list.append(I1)
        #print("Simpson's inputs being added:  ", inputs)
        
    print("Complete list of Simpson's Results:  ", simpsons_results_list)
        
        
# GAUSS-KRONROD METHOD (for accuracy testing)
def gauss_kronrod_method(f1, a, b):
    print("\n ENTERING: gauss_Kronrod_method")
    I2 = integrate.quad(f1, a, b)
    print("Gauss-Kronrod Result:", I2[0])
    return I2
        
def comparison_display(f1, universal_slice_list):
    print("\n ENTERING: comparison_display")
    
    start_integral, stop_integral, slice_list, universal_slice_list = slices()
    
    trapezoid_results_list = trapezoid_results(f1, universal_slice_list)
    simpsons_results_list = simpsons_results(f1, universal_slice_list)
    I2 = gauss_kronrod_method(f1, start_integral, stop_integral)
    
    # REMOVE FOR COMPARISON
    # x_intputs = np.linspace(start_integral, stop_integral, 1000)
    # x_axis = x_intputs
    # y_axis = f1(x=x_intputs)
    fig, ax = plt.subplots()
   
    # colours axis red, and places vertical lines for trapezoid slices
    # ax.plot(x_axis, y_axis)
    ax.axhline(0, color='red', linewidth=.8, zorder=1)
    ax.axvline(0, color='red', linewidth=.8, zorder=1)
   

    

    ax.set(xlabel='STEPS', ylabel="F(x)",
        title=(
            'Simpson\'s Rule\n'
            + (rf"$\int_{{{start_integral:.6g}}}^{{{stop_integral:.6g}}} {f1.__doc__}\,dx$"
               if f1.__doc__
               else rf"$\int_{{{start_integral:.6g}}}^{{{start_integral:.6g}}} {f1.__name__}(x)\,dx$"
              )
            + f" | # of slices: {slice_list}"
            )
         )
    ax.grid(alpha = .5, linestyle = 'dashed')
    ax.margins(0.5)

    plt.show()




def main():
    print("Going Through Entry Point")
    
    _, _ , _, universal_slice_list = slices()
    #trapezoid_results(f1, universal_slice_list)
    #simpsons_results(f1, universal_slice_list)
    
    comparison_display(f1, universal_slice_list)

if __name__ == "__main__":
   main()



