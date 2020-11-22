import numpy as np
import utils
import sympy as sp
from sympy.algebras.quaternion import Quaternion


def cross_product_matrix(vector):
    S = sp.array([[0, -vector[2], vector[1]],
                  [vector[2], 0, -vector[0]],
                  [-vector[1], vector[0], 0]])
    return S


def quaternion_to_rotation_matrix(quaternion: Quaternion):
    epsilon = quaternion.a
    eta = [quaternion.b, quaternion.c, quaternion.d]
    epsilon_cross_matrix = utils.cross_product_matrix(epsilon)
    R = (np.eye(3) + 2 * eta * epsilon_cross_matrix
         + 2 * epsilon_cross_matrix @ epsilon_cross_matrix)
    return R


def quaternion_to_euler(quaternion: sp.array) -> sp.array:
    if isinstance(quaternion, Quaternion):
        q = [quaternion.a, quaternion.b, quaternion.c, quaternion.d]
    else:
        q = quaternion
    q_2 = [i**2 for i in q]

    phi = sp.atan2(2 * (q[3]*q[2] + q[0]*q[1]),
                   q_2[0] - q_2[1] - q_2[2] + q_2[3])

    theta = sp.asin(2 * (q[0]*q[2] - q[1]*q[3]))

    psi = sp.atan2(2 * (q[1]*q[2] + q[0]*q[3]),
                   q_2[0] + q_2[1] - q_2[2] - q_2[3])

    euler_angles = sp.Array([phi, theta, psi])
    return euler_angles


def euler_to_quaternion(euler_angles: sp.array) -> sp.array:
    """Convert euler angles into quaternion

    Args:
        euler_angles (np.ndarray): Euler angles of shape (3,)

    Returns:
        np.ndarray: Quaternion of shape (4,)
    """
    half_angles = 0.5 * euler_angles
    c_phi2, c_theta2, c_psi2 = [sp.cos(i) for i in half_angles]
    s_phi2, s_theta2, s_psi2 = [sp.sin(i) for i in half_angles]
    quaternion = sp.Array(
        [
            c_phi2 * c_theta2 * c_psi2 + s_phi2 * s_theta2 * s_psi2,
            s_phi2 * c_theta2 * c_psi2 - c_phi2 * s_theta2 * s_psi2,
            c_phi2 * s_theta2 * c_psi2 + s_phi2 * c_theta2 * s_psi2,
            c_phi2 * c_theta2 * s_psi2 - s_phi2 * s_theta2 * c_psi2,
        ]
    )
    return quaternion


def quaternion_derivative(quaterion, omega):
    omega_quat = Quaternion(0, *omega)
    q_dot = (1/2) * quaterion * omega_quat
    return [getattr(q_dot, field) for field in 'abcd']


pi = sp.symbols('pi')
q = Quaternion(0, 1, 0, 0).normalize()
omega = sp.Matrix([0, pi, 0])
omega_quat = Quaternion(0, *omega)
q_dot = (1/2) * q * omega_quat

euler = quaternion_to_euler(q)
q2 = euler_to_quaternion(euler)

derivative = quaternion_derivative(
    sp.Quaternion(0, 1, 0, 0), [0, sp.symbols('pi'), 0])
