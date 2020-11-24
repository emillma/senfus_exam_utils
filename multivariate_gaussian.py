import sympy as sp

shape_x = 1
shape_y = 2
x = sp.MatrixSymbol('x', shape_x, 1)

a = sp.MatrixSymbol('a', shape_x, 1)
a = sp.Matrix([4])

y = sp.MatrixSymbol('y', shape_y, 1)
y = sp.Matrix([2, 3])

b = sp.MatrixSymbol('b', shape_y, 1)
b = sp.Matrix([2, 3])

P_xx = sp.MatrixSymbol('P_{xx}', shape_x, shape_x)
P_xx = sp.Matrix([1])


P_yy = sp.MatrixSymbol('P_{yy}', shape_y, shape_y)
P_yy = sp.Matrix([[2, 0], [0, 3]])


P_xy = sp.MatrixSymbol('P_{xy}', shape_x, shape_y)
P_xy = sp.Matrix([[1, 0]])

mu_x_given_y = a + P_xy*P_yy.inv()*(y-b)
P_x_given_y = P_xx - P_xy*P_yy.inv()*P_xy.T
P_x_given_y
