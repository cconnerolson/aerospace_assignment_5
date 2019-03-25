""" An automobile tire bursts sending a shock wave (assume normal shock) propagating into the ambient air which has a
pressure P_1 and speed of sound c_1.  If the pressure behind the shock is P2 (roughly inflated tire pressure), show that
the speed of shock propagation u_s equals the given function.  Calculate this speed given ambient air temperature 
T_a = 303 K and tire pressure is 2 atmospheres gauge pressure P_g = 30 psi.
"""

# Requirements

from math import sqrt


# Given

T_a = 303 # K
P_g = 30 # psi


def shock_propagation(c_1, gamma, P_1, P_2): # speed of shock propagation, u_s
	return c_1 * sqrt((gamma - 1) / (2 * gamma) + (P_2 * (gamma + 1)) / (P_1 * 2 * gamma))
