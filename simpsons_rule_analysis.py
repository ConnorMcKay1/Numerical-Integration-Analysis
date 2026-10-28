import scipy.integrate as integrate
from numpy import sin, cos, tan, pi
import numpy as np
import matplotlib.pyplot as plt
      
      
print("SIMPSONS_METHOD_ANALYSIS.py")

#f(x)=x^{4}-5x^{2}+10
#f(x)=((x**4) - (5*(x**2)) + 10)X
#f(x) = ((np.sqrt(x) + 1)**3)/(2*(np.sqrt(x)))
#f(x)=tan(sin(x))-sin(tan(x))
def f1(x):
   """tan(sin(x))-sin(tan(x))"""
   return (tan(sin(x))-sin(tan(x)))

# SLICE CONTROLLER
def slice_controller():
    print("\n ENTERING: slice_controler")
    number_of_slices = 50
    a = 1
    b = 3
    slices = np.linspace(a, b, number_of_slices + 1)
        
    return a, b, slices

# SIMPSON'S RULE
def simpsons_rule(f1, slices):
   print("\n ENTERING: simpsons rule")
   y = f1(slices)
   I1 = integrate.simpson(y, slices)
   print(f"Panel amount: {len(slices)}, Simpson's rule result: {I1}|")
   return slices, y, I1
   

# POLYNOMIAL_CREATOR
def polynomial_creator(f1, slices):
    print("\n ENTERING: polynomial_creator")
    
    y = f1(slices)

    # Quadratics for the all of the Simpson subsections/slices
    polynomials = []
    
    list_of_panel_points = []
    
    smooth_polynomial_inputs = []
    smooth_polynomial_values = []

    for i in range(0, (len(slices)) - 2, 2):
        p = np.poly1d(np.polyfit(slices[i:i+3], y[i:i+3], 2))
        
        panel_points = (slices[i:i+3], y[i:i+3], 2)
        
        x_smooth = np.linspace(slices[i], slices[i+2], 100)
        y_smooth = p(x_smooth)

        polynomials.append(p)
        
        list_of_panel_points.append(panel_points)
        
        smooth_polynomial_inputs.append(x_smooth)
        smooth_polynomial_values.append(y_smooth)

    # just prints list of polynomials   
    # for i, p in enumerate(polynomials):
    #     print(f"PANEL {i}: \n {p}")
      
        
    # used to actually see the 3 points used to fit a polynomial for each panel/slice
    # for i, panel_points in enumerate(list_of_panel_points):
    #     print(f"PANEL POINTS {i}: \n {panel_points}")


    return y, polynomials,smooth_polynomial_inputs ,smooth_polynomial_values  
        # returns a list of polynomials

# GAUSS-KRONROD METHOD (for accuracy testing)
def gauss_kronrod_method(f1, a, b):
   print("\n ENTERING: gauss_Kronrod_method")
   I2 = integrate.quad(f1, a, b)
   print("Gauss-Kronrod Result:", I2[0])

# DISPLAY
def display(f, slices, y, smooth_polynomial_inputs, smooth_polynomial_values):
    print("\n ENTERING: display")
    
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
   
    # draws the lines from one panel to another using computed quadratics
    for x_smooth, y_smooth in zip(
        smooth_polynomial_inputs,
        smooth_polynomial_values
        ):
            ax.plot(
            x_smooth,
            y_smooth,
            color='fuchsia',
            linewidth=1.5,
            zorder=3
    )

    ax.set(xlabel='STEPS', ylabel="F(x)",
        title=(
            'Simpson\'s Rule\n'
            + (rf"$\int_{{{min:.6g}}}^{{{max:.6g}}} {f.__doc__}\,dx$"
               if f.__doc__
               else rf"$\int_{{{min:.6g}}}^{{{max:.6g}}} {f.__name__}(x)\,dx$"
              )
            + f" | # of slices: {len(slices) - 1}"
            )
         )
    ax.grid(alpha = .5, linestyle = 'dashed')
    ax.margins(0.5)

    plt.show()


def main():
    print("Going Through Entry Point")
    
    a, b, slices = slice_controller()
    
    y, _, smooth_polynomial_inputs, smooth_polynomial_values = polynomial_creator(f1, slices)
    
    
    #simpsons_rule(f1, slices)
    
    #gauss_kronrod_method(f1, a, b)
    
    display(f1, slices, y, smooth_polynomial_inputs, smooth_polynomial_values)


if __name__ == "__main__":
   main()