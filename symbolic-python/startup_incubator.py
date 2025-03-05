"""
A startup incubator at JKUAT is optimizing the cost function:

C(x) = 5x^3 - 10x^2 + 4x + 3

    ] where xx is the number of AI startups funded.

    Task:

        Find the symbolic derivative of C(x)C(x).
        Solve for xx when the cost is minimized.
        Interpret the result for decision-making.
"""

import sympy as sy

x = sy.symbols('x')

C_x = 5*x**3 - 10*x**2 + 4*x + 3

C_prime = sy.diff(C_x, x)

optimal_x = sy.solve(C_prime, x)

C_double_prime = sy.diff(C_prime, x)
concavity = [C_double_prime.subs(x, val) for val in optimal_x]

# Print results
print("Cost Function Derivative: ", C_prime)
print("Optimal x values: ", optimal_x)
print("Second Derivative Test Results: t", concavity)
