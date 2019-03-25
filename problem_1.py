""" A stagnation temperature probe is mounted on the nose cone of a supersonic aircraft.  A normal shock wave stands in
front of the tip of the probe.  The measured stagnation temperature pressure is T_2 = 488 K as the jet cruises at an
altitude of z = 15 km with ambient temperature T_1 = 217 K and ambient pressure P_1 = 12 kPa.

Find:
	-the Mach number, Ma
	-the velocity of the aircraft, v
	-the static pressure behind the shock wave, P_s
	-the stagnation pressure behind the shock wave, P_t
"""

# Givens


T_2 = 488 # K
z = 15e3 # km
T_1 = 217 # K
P_1 = 12 # kPa


a_1 = 295.3 # m/s, sqrt(gamma * R * T_1)