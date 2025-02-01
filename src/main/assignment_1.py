import math

def approximation_algorithm(x, epsilon=1e-6):
    guess = x / 2.0
    while abs(guess**2 - x) > epsilon:
        guess = (guess + x / guess) / 2.0
    return guess


def bisection_method(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    
    return (a + b) / 2.0


def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Example functions for testing
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def g(x):
    return (x + 2)**(1/3)

if __name__ == "__main__":
    print("Approximation Algorithm sqrt(10):", approximation_algorithm(10))
    print("Bisection Method Root of f(x) = x^3 - x - 2:", bisection_method(f, 1, 2))
    print("Fixed Point Iteration:", fixed_point_iteration(g, 1.5))
    print("Newton-Raphson Root of f(x) = x^3 - x - 2:", newton_raphson(f, df, 1.5))
