import sympy as sp

t = sp.symbols('t')
a = sp.symbols('a')
A = sp.Matrix([[0, -1, 0],
               [0, 0, 0],
               [0, 0, 1]],
              )
F = sp.simplify(sp.exp(A*t))
