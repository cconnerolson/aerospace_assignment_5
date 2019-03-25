""" A con-di nozzle, with an exit to throat area ratio A_e/A_t = 1.633 is designed to operate with atmospheric pressure
at the exit plane P_e = P_atm.
    a) Determine the ranges of upstream stagnation pressures P_0 for which the nozzle will be free of shocks.
    b) If the upstream stagnation pressure is P_t = 1.5·P_atm at which position x, will the normal shock occur?
"""

# Givens


def nozzle_area_ratio(A_e, A_t, x, l):  # the con-di nozzle area varies according to this ratio
    return (A_e / A_t - 1) * (2 * x / l - 1) ** 2 + 1
