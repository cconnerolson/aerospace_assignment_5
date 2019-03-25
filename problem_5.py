from math import sqrt

""" An automobile tire bursts sending a shock wave (assume normal shock) propagating into the ambient air which has a
pressure P_1 and speed of sound c_1.  If the pressure behind the shock is P2 (roughly inflated tire pressure), show that
the speed of shock propagation u_s equals the given function.
"""

# Given


def shock_propagation(c_1, gamma, P_1, P_2):  # speed of shock propagation, u_s
	return c_1 * sqrt((gamma - 1) / (2 * gamma) + (P_2 * (gamma + 1)) / (P_1 * 2 * gamma))
