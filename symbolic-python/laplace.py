"""
In a control system, the Laplace Transform of the system equation is:

H(s) = \frac{1}{s^2 + 3s + 2}

    ] Task:

        Factor the denominator symbolically.
        Compute the inverse Laplace Transform to find h(t)h(t).
        Find the poles of the system.
"""

import sympy as sy

s, t = sy.symbols('s t')

H_s = 1 / (s**2 + 3*s + 2)

denominator = s**2 + 3*s + 2
factored_denominator = sy.factor(denominator)

h_t = sy.inverse_laplace_transform(H_s, s, t)

poles = sy.solve(denominator, s)

print("Factored Denominator:", factored_denominator)
print("Inverse Laplace Transform h(t):", h_t)
print("Poles of the System:", poles)
