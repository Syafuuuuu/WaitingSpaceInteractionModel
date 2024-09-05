import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta_Ap = 0.5
beta_Ws1 = 0.4
beta_Ws2 = 0.3
beta_Ws3 = 0.3
beta_An = 0.6
omega_Em1 = 0.3
omega_Em2 = 0.4
omega_Em3 = 0.3
omega_Ps = 0.5
omega_Ri1 = 0.3
omega_Ri2 = 0.4
omega_Ri3 = 0.3
gamma_Wl = 0.1

# Initial conditions
Pa = 0.5 #Positive Affect
Ws = 0.5 #Short Term Interaction Willigness
Wl = 0.5 #Long Term Interaction Willingness
Eh = 0.1 #Exhaustion

#Personality
Ex = 0.8 #Extravertness
Op = 0.6 #Openness
Nu = 0.2 #Neuroticism

#Emotions
Hp = 0.8 #Happiness
Sd = 0.2 #Sadness
Fr = 0.1 #Feaar

Ns = 0.8 #Similarity

# Time step
dt = 0.01
time_steps = 1000

# Arrays to store results
Pa_values = []
Ws_values = []
Wl_values = []

for t in range(time_steps):
    # Instantaneous Relationships
    Pa = beta_Ap * Hp + (1 - beta_Ap) * (omega_Em1 * Sd + omega_Em2 * Fr + omega_Em3 * Nu)
    Ws = beta_Ws1 * Pa + beta_Ws2 * (omega_Ps * Ex + (1 - omega_Ps) * Op) + beta_Ws3 * (1 - Eh)
    Ri = beta_An * (omega_Ri1 * Ws + omega_Ri2 * Wl + omega_Ri3 * Ns) * (1 - beta_An) * Nu

    # Temporal Relationship
    Wl = Wl + gamma_Wl * (Ws - Wl) * (1 - Wl) * Wl * dt

    # Store results
    Pa_values.append(Pa)
    Ws_values.append(Ws)
    Wl_values.append(Wl)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(Pa_values, label='Pa')
plt.plot(Ws_values, label='Ws')
plt.plot(Wl_values, label='Wl')
plt.xlabel('Time Steps')
plt.ylabel('Values')
plt.title('Pa, Ws, and Wl over Time')
plt.legend()
plt.grid(True)
plt.show()
