import sympy as sp

shape_x = 2
shape_y = 1
x = sp.MatrixSymbol('x', shape_x, 1)

a = sp.MatrixSymbol('a', shape_x, 1)

y = sp.MatrixSymbol('y', shape_y, 1)

b = sp.MatrixSymbol('b', shape_y, 1)

P_xx = sp.MatrixSymbol('P_{xx}', shape_x, shape_x)

P_yy = sp.MatrixSymbol('P_{yy}', shape_y, shape_y)

P_xy = sp.MatrixSymbol('P_{xy}', shape_x, shape_y)

z = sp.MatrixSymbol('z', shape_y, 1)

mu_x_given_y = a + P_xy*P_yy.inv()*(y-b)
P_x_given_y = P_xx - P_xy*P_yy*P_xy.T
