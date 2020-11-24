import sympy as sp

T, tau = sp.symbols('T, tau')
sigma_a, sigma_b = sp.symbols('sigma_a, sigma_b')
shape = 4

A = sp.MatrixSymbol('A', shape, shape)
A = sp.Matrix([[0, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 0, 0]])
zeros = sp.zeros(shape, shape)
G = sp.MatrixSymbol('G', shape, shape)
G = sp.Matrix([[0, 0],
               [1, 0],
               [0, 0],
               [0, 1]])

D = sp.diag(*[sigma_a, sigma_b])

myvar = sp.exp((T-tau)*A)*G*D*G.T*sp.exp((T-tau)*A.T)
Q = sp.simplify(sp.integrate(myvar, (tau, 0, T)))

vanloan = sp.BlockMatrix([[-A, G*D*G.T],
                          [zeros, A.T]]) * T
vanloan_exp = sp.exp(sp.Matrix(vanloan))
Q2 = vanloan_exp[shape:, shape:].T*vanloan_exp[:shape, shape:]
