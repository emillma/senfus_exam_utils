import sympy as sp
import numpy as np
quat_vars = sp.symbols('q:4')
theta_vars = sp.symbols('theta:3')

g = sp.Quaternion(*quat_vars) * sp.Quaternion(1, *theta_vars)
g_mat = sp.Matrix([getattr(g, att) for att in 'abcd'])
G = g_mat.jacobian(theta_vars)

for i in range(1):
    quat_this = sp.Quaternion(*np.random.uniform(-1, 1, 4)).normalize()
    subdict = dict(zip(quat_vars, [getattr(quat_this, att) for att in 'abcd']))
    G_this = G.subs(subdict)
    P_this = sp.randMatrix(3, 3)
    P_this = P_this * P_this.T
    Pq = G_this*sp.randMatrix(3, 3)*G_this.T
