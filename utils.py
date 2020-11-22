import sympy as sp
from sympy.algebras.quaternion import Quaternion


"""
Remember! This assumes r i j k and not i j k r
"""
pi = sp.symbols('myvar')
q = Quaternion(0, 1, 0, 0).normalize()
omega = sp.Matrix([0, pi, 0])
omega_quat = Quaternion(0, *omega)
q_dot = (1/2) * q * omega_quat
print(q_dot)
