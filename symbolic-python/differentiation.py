import sympy as sy

"""
A machine learning model at JKUAT is trained using the loss function:

L(x) = 3x^2 + 2x - 5

    ] Task:

        Compute the symbolic derivative of L(x)L(x) to find the gradient.
        Solve for xx when the gradient is zero (optimal solution).
        Use second derivatives to check if it is a minimum or maximum.
"""

x = sy.Symbol('x')

L = 1*x**2 + 4*x + 3

L_differential = sy.diff(L, x)
print(f'Gradient: {L_differential}')

optimal_solution = sy.solve(L_differential, x)
print(f"Solution at X = 0: {optimal_solution}")

second_diff = sy.diff(L_differential, x)
print("Second Derivative:", second_diff)


for val in optimal_solution:
    concavity = second_diff.subs(x, val)
    print(f"Second derivative at x = {val}:", concavity)

    if concavity > 0:
        print(f"x = {val} is a Minimum.")
    elif concavity < 0:
        print(f"x = {val} is a Maximum.")
    else:
        print(f"x = {val} is a Saddle Point.")
