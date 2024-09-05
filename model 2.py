import numpy as np
import matplotlib.pyplot as plt

# Define time range
t = np.linspace(0, 10, 100)

# Define parameters (example values)
beta_Ap = 0.5
beta_An = 0.5
omega_Em1 = 0.3
omega_Em2 = 0.4
omega_Em3 = 0.3
beta_Ws1 = 0.4
beta_Ws2 = 0.3
beta_Ws3 = 0.3
omega_Ps = 0.5
omega_Ri1 = 0.3
omega_Ri2 = 0.4
omega_Ri3 = 0.3
gamma_Wl = 0.1

# Define functions
def Pa(t):
    return beta_Ap * Hp(t) + (1 - beta_Ap) * (omega_Em1 * Sd(t) + omega_Em2 * Fr(t) + omega_Em3 * An(t))

def Ws(t):
    return beta_Ws1 * Pa(t) + beta_Ws2 * (omega_Ps * Ex(t) + (1 - omega_Ps) * Op(t)) + beta_Ws3 * (1 - Eh(t))

def Ri(t):
    return beta_An * (omega_Ri1 * Ws(t) + omega_Ri2 * Wl(t) + omega_Ri3 * Ns(t)) * (1 - beta_An) * An(t)

def Wl(t, dt=0.1):
    return Wl(t) + gamma_Wl * (Ws(t) - Wl(t)) * (1 - Wl(t)) * Wl(t) * dt

# Example functions for Hp, Sd, Fr, An, Ex, Op, Eh, Ns
def Hp(t): return np.sin(t)
def Sd(t): return np.cos(t)
def Fr(t): return np.sin(t/2)
def An(t): return np.cos(t/2)
def Ex(t): return np.sin(t/3)
def Op(t): return np.cos(t/3)
def Eh(t): return np.sin(t/4)
def Ns(t): return np.cos(t/4)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, Pa(t), label='Positive Affect (Pa)')
plt.plot(t, Ws(t), label='Willingness to Interact (Short Term) (Ws)')
plt.plot(t, Ri(t), label='Readiness to Interact (Ri)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Interaction Model Graph')
plt.legend()
plt.grid(True)
plt.show()
