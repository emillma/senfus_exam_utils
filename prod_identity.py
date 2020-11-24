import sympy as sp

shape = 2
z = sp.MatrixSymbol('z', shape, 1)
H = sp.MatrixSymbol('H', shape, shape)
x = sp.MatrixSymbol('', shape, 1)
R = sp.MatrixSymbol('R', shape, shape)

x_bar = sp.MatrixSymbol('x_bar', shape, 1)
P_bar = sp.MatrixSymbol('P_bar', shape, shape)

I = sp.Identity(shape)

z_bar = H*x_bar
S = R + H*P_bar*H.T
W = P_bar * H.T * S.inv()
x_hat = x_bar + W*(z-H*x_bar)
P_hat = (I-W*H)*P_bar
