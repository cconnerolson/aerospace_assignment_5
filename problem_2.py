""" A large tank supplies helium through a conv-div nozzle to the atmosphere.  Pressure in the tank remains constant at
P_t = 8 MPa and temperature remains constant at T_t = 1000 K.  There are no shock waves at the nozzle.  The nozzle is
designed to discharge at exit Mach number of 3.5 with exit area A_e = 100 mm².  For helium, 𝜸 = 1.66 and
R = 2077 J/(kg·K).

Determine:
    -the pressure at the nozzle exit, P_e
    -the mass flux through the device, mdot
"""

# Givens

P_t = 8  # MPa
T_t = 1000  # K
Ma = 3.5
A_e = 100  # mm²
gamma = 1.66  # 𝜸
R = 2077  # J/(kg·K)
