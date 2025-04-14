import numpy as np
from scipy.optimize import fsolve

def T0_T_relation(M, k):
    return 1 + ((k - 1)/2) * M**2

def P0_P_relation(T0_T, k):
    return T0_T ** (k / (k - 1))

def A_Astar_relation(M, k):
    T0_T = T0_T_relation(M, k)
    return (1 / M) * ((2 / (k + 1)) * T0_T) ** ((k + 1) / (2 * (k - 1)))

def solve_mach_from_area(A_Astar_target, k=1.4, branch='subsonic'):
    def A_Astar_eqn(M):
        return A_Astar_relation(M, k) - A_Astar_target

    M_guess = 0.3 if branch == 'subsonic' else 2.5
    return fsolve(A_Astar_eqn, M_guess)[0]

def solve_mach_branches(A_Astar_target, k=1.4):
    def A_Astar_eqn(M):
        return A_Astar_relation(M, k) - A_Astar_target

    M_sub = fsolve(A_Astar_eqn, 0.3)[0]
    M_sup = fsolve(A_Astar_eqn, 2.5)[0]
    return M_sub, M_sup
