from numpy.core.numeric import identity
import sympy as sp
from sympy.matrices.expressions.matexpr import Identity
shape = 4
x_prev = sp.MatrixSymbol('X_{k-1}', shape, 1)
P_prev = sp.MatrixSymbol('P_{k-1}', shape, shape)
z_k = sp.MatrixSymbol('z_{k}', shape, 1)
F = sp.MatrixSymbol('F', shape, shape)
H = sp.MatrixSymbol('H', shape, shape)
Q = sp.MatrixSymbol('Q', shape, shape)
R = sp.MatrixSymbol('R', shape, shape)


x_ateori = F*x_prev
P_ateori = F*P_prev*F.T + Q
z_ateori = H*x_ateori
innovation = z_k - z_ateori
S_k = H*P_ateori*H.T + R
W_k = P_ateori*H.T*S_k.inv()  # gain
x_apost = x_ateori + W_k*innovation
P_apost = (sp.Identity(shape) - W_k*H)*P_ateori
