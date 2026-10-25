import scipy.integrate as integrate
from numpy import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
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
    
    return start_slice_amount, stop_slice_amount, slice_amount_step, start_integral, stop_integral, slice_list, universal_slice_list
    
# TRAPEZOID RESULTS
def trapezoid_results(f1, universal_slice_list):
    print("\n ENTERING: trapezoid_results")
            
    trapezoid_results_list = []
    
    for inputs in universal_slice_list:
        _, _, I1 = trapezoid_method(f1, inputs)
        trapezoid_results_list.append(I1)
        #print("Simpson's inputs being added:  ", inputs)

    print("Complete list of Trapezoid Results:  ", trapezoid_results_list)
    
    return trapezoid_results_list
    
# SIMPSON'S RESULTS
def simpsons_results(f1, universal_slice_list):
    print("\n ENTERING: simpsons_results")
    
    simpsons_results_list = []
    
    for inputs in universal_slice_list:
        _, _, I1 = simpsons_rule(f1, inputs)
        simpsons_results_list.append(I1)
        #print("Simpson's inputs being added:  ", inputs)
        
    print("Complete list of Simpson's Results:  ", simpsons_results_list)
    
    return simpsons_results_list
               
# GAUSS-KRONROD METHOD (for accuracy testing)
def gauss_kronrod_method(f1, a, b):
    print("\n ENTERING: gauss_Kronrod_method")
    I2 = integrate.quad(f1, a, b)
    print("Gauss-Kronrod Result:", I2[0])
    return I2[0]


# COMPARISON DISPLAY
def comparison_display(f1):
    print("\n ENTERING: comparison_display")

    # Get integration settings and calculate results
    start_slice_amount, stop_slice_amount, slice_amount_step, start_integral, stop_integral, slice_list, universal_slice_list = slices()
    print("PRINTING FROM THE comparison_display FUNCTION", slice_list)


    trapezoid_results_list = trapezoid_results(f1, universal_slice_list)
    simpsons_results_list = simpsons_results(f1, universal_slice_list)
    I2 = gauss_kronrod_method(f1, start_integral, stop_integral)

    # Convert plotting data to predictable numeric formats
    x = np.asarray(slice_list, dtype=float)
    trap = np.asarray(trapezoid_results_list, dtype=float)
    simp = np.asarray(simpsons_results_list, dtype=float)
    reference = float(np.asarray(I2).squeeze())

    # Catch mismatched data before Matplotlib raises an error
    if not (len(x) == len(trap) == len(simp)):
        raise ValueError(
            "slice_list, trapezoid results, and Simpson results "
            "must all have the same length."
        )

    # Dashboard colors
    bg_top = "#30343D"
    bg_bottom = "#17191E"
    panel = "#22262E"
    cyan = "#67D9F5"
    violet = "#B6A0FF"
    mint = "#66D9A8"
    text_main = "#F1F5F9"
    text_muted = "#A8B0BD"
    grid_color = "#59616E"

    # Figure and gradient background
    fig = plt.figure(figsize=(13, 8), facecolor=bg_bottom)

    gradient = np.linspace(0, 1, 400).reshape(-1, 1)
    gradient = np.repeat(gradient, 400, axis=1)

    gradient_map = LinearSegmentedColormap.from_list(
        "dashboard_grey",
        [bg_top, "#22252C", bg_bottom]
    )

    bg_ax = fig.add_axes([0, 0, 1, 1], zorder=0)
    bg_ax.imshow(
        gradient,
        cmap=gradient_map,
        aspect="auto",
        extent=[0, 1, 0, 1],
        interpolation="bicubic"
    )
    bg_ax.axis("off")

    # Main plotting panel
    ax = fig.add_axes([0.09, 0.17, 0.84, 0.59])
    ax.set_facecolor(panel)
    ax.set_zorder(2)

    # Header
    formula = (
        rf"$\int_{{{start_integral:.6g}}}^"
        rf"{{{stop_integral:.6g}}} "
        rf"{f1.__doc__}\,dx$"
        if f1.__doc__
        else (
            rf"$\int_{{{start_integral:.6g}}}^"
            rf"{{{stop_integral:.6g}}} "
            rf"{f1.__name__}(x)\,dx$"
        )
    )

    fig.text(
        0.09, 0.94,
        "NUMERICAL INTEGRATION ANALYSIS",
        fontsize=10,
        fontweight="bold",
        color=cyan
    )

    fig.text(
        0.09, 0.885,
        "Convergence Comparison",
        fontsize=24,
        fontweight="bold",
        color=text_main
    )

    fig.text(
        0.09, 0.84,
        formula,
        fontsize=13,
        color=text_muted
    )

    # Slice configuration subtitle
    config_text = (
        f"Slices: {start_slice_amount}-{stop_slice_amount}"
        f"   |   Increment: {slice_amount_step}"
    )

    fig.text(
        0.09, 0.795,
        config_text,
        fontsize=10,
        color=text_muted
    )

    # Main comparison lines
    ax.plot(
        x, trap,
        color=cyan,
        linewidth=2.5,
        marker="o",
        markersize=7,
        markerfacecolor=cyan,
        markeredgecolor=panel,
        markeredgewidth=1.2,
        label="Trapezoidal Rule",
        zorder=3
    )

    ax.plot(
        x, simp,
        color=violet,
        linewidth=2.5,
        marker="s",
        markersize=6.5,
        markerfacecolor=violet,
        markeredgecolor=panel,
        markeredgewidth=1.2,
        label="Simpson's Rule",
        zorder=4
    )

    ax.axhline(
        y=reference,
        color=mint,
        linewidth=1.8,
        linestyle=(0, (5, 4)),
        label=f"Gauss–Kronrod ({reference:.6f})",
        zorder=2
    )

    # Axes styling
    ax.set_xlabel(
        "Number of slices",
        fontsize=11,
        color=text_main,
        labelpad=12
    )

    ax.set_ylabel(
        "Approximate integral",
        fontsize=11,
        color=text_main,
        labelpad=12
    )

    ax.set_xticks(x)
    ax.tick_params(colors=text_muted, labelsize=10)

    for spine in ax.spines.values():
        spine.set_color("#414752")
        spine.set_linewidth(0.8)

    ax.grid(
        True,
        color=grid_color,
        alpha=0.28,
        linestyle="--",
        linewidth=0.7
    )

    ax.margins(x=0.06, y=0.12)

    ax.legend(
        loc="upper right",
        facecolor="#2A2F39",
        edgecolor="#414752",
        framealpha=0.97,
        fontsize=10,
        labelcolor=text_main
    )

    # Footer
    fig.text(
        0.09, 0.085,
        f"REFERENCE VALUE   {reference:.8f}",
        fontsize=9,
        fontweight="bold",
        color=mint
    )

    fig.text(
        0.91, 0.085,
        f"{len(x)} DATA POINTS",
        fontsize=9,
        color=text_muted,
        ha="right"
    )

    plt.show()



def main():
    print("Going Through Entry Point")
    
    #trapezoid_results(f1, universal_slice_list)
    #simpsons_results(f1, universal_slice_list)
    
    comparison_display(f1)

if __name__ == "__main__":
   main()



