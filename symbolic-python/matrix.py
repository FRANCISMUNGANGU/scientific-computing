"""

In AI applications, dimensionality reduction is done using eigenvalues of matrices.
    Given a feature matrix:

A = begin{bmatrix} 2 & 1 \ 1 & 3 \end{bmatrix}

    ] Task:

        Compute the symbolic determinant of AA.
        Find the eigenvalues of AA using symbolic computation.
        Verify that the eigenvalues satisfy the characteristic equation.
        
"""

import sympy as sy

λ = sy.Symbol('λ')

A = sy.Matrix([[2, 1], [1, 3]])

det_A = A.det()
print("Determinant of A: ", det_A)

char_eq = (A - λ*sy.eye(2)).det()
print("Characteristic Equation: ", char_eq)

eigenvalues = sy.solve(char_eq, λ)
print("Eigenvalues: ", eigenvalues)

for eigen in eigenvalues:
    verification = char_eq.subs(λ, eigen)
    print(f"Verification for λ = {eigen}: {verification}")

