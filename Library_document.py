def gorner_calc(a, x):
    """Method calculate polynom value. Algorithm use Gorner method. a - coeff, x - point(value). Return polynom value in the point x."""
    polynom_value = 0.0
    for i in range(len(a) - 1, -1, -1):
        polynom_value = polynom_value*x + a[i]
    return polynom_value

def polynom_value_calc(a, x):
    """Method calculate polynom value. a - coeff, x - point(value). Return polynom value in the point x."""
    polynom_value = 0.0
    n = len(a)
    for i in range(n):
        polynom_value = polynom_value + a[i] * x**i
    return polynom_value 
