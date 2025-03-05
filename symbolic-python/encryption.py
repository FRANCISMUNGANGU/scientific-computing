import sympy as sp

# Define symbols
P, e, N = sp.symbols('P e N')

C = sp.Mod(P**e, N)
print("Symbolic Encryption Function:", C)

P_value = 7
N_value = 33

mod_inverse = sp.mod_inverse(P_value, N_value)
print(f"Modular Inverse of {P_value} mod {N_value}:", mod_inverse)

P_val, e_val, N_val = 7, 3, 33
C_value = pow(P_val, e_val, N_val)
print(f"Ciphertext C when P={P_val}, e={e_val}, N={N_val}:", C_value)
