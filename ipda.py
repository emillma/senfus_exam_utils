import sympy as sp
from sympy.stats import Poisson, density

lamb = sp.symbols('lambda')
n = sp.symbols('n')
distro = Poisson('N', lamb)
dens = density(distro)(n)

Pd = sp.symbols('P_d')
Pd = 0.234
r_k_prev = 0.5  # previous existance probability
# l^ak probability that the meesurement k os associated to the current state
sum_l = 0.1  # probability that any of the measurement comes from current state

L_k = sp.simplify((1 - Pd) + (Pd/lamb) * sum_l)

# IPDA existence probability
r_k = sp.simplify((L_k*r_k_prev)/(1-(1-L_k)*r_k_prev), rational=1)
