import numpy as np
import matplotlib.pyplot as plt

#region Define parameters
#Positive Affect Para
beta_Pa = 0.5

#Personality Para
omega_Ps = 0.5

#Dynamic Emotions Para
gamma_Dh = 0.1   #Happiness
lambda_Dh = 0.03
gamma_Ds = 0.1   #Sadness
lambda_Ds = 0.03
gamma_Df = 0.1   #Fear
lambda_Df = 0.03

#Willignness to Intereact Para
beta_Si = 0.5    #Short-Term
gamma_Li = 0.1   #Long-Term

#Readiness to Interact Para
omega_Ri = 0.5

#endregion

# Time settings
t_max = 1000
dt = 0.1
time = np.arange(0, t_max, dt)

# Initialize variables
Dh = np.zeros_like(time)
Ds = np.zeros_like(time)
Df = np.zeros_like(time)
Pa = np.zeros_like(time)
Si = np.zeros_like(time)
Li = np.zeros_like(time)
Ri = np.zeros_like(time)

#Input Conditions
Ha = 0.7
Sd = 0.2
Fe = 0.4

# Initial conditions
Dh[0] = Ha #Dynamic Happiness
Ds[0] = Sd
Df[0] = Fe
Pa[0] = 0.0
Si[0] = 0.2
Li[0] = 0.0
Ri[0] = 0.0

# Simulation loop
for i in range(1, len(time)):
    #Dyanmic Emotions
    Dh[i] = Dh[i-1] + gamma_Dh * (Pa[i-1] - lambda_Dh) * Dh[i-1] * (1 - Dh[i-1]) * dt
    Ds[i] = Ds[i-1] + gamma_Ds * (Pa[i-1] - lambda_Ds) * Ds[i-1] * (1 - Ds[i-1]) * dt
    Df[i] = Df[i-1] + gamma_Df * (Pa[i-1] - lambda_Df) * Df[i-1] * (1 - Df[i-1]) * dt
    
    #Postiive Affect
    Pa[i] = Dh[i] - beta_Pa * Ds[i]
    
    # Willingness to  Interact
    # Short Term
    Si[i] = beta_Si * Pa[i] + (1 - beta_Si) * (omega_Ps * Dh[i] + (1 - omega_Ps) * Ds[i]) * (1 - Df[i])
    # Long Term
    Li[i] = Li[i-1] + gamma_Li * (Si[i-1] - Li[i-1]) * (1 - Li[i-1]) * dt
    
    #Interaction Readiness
    Ri[i] = omega_Ri * Si[i] + (1 - omega_Ri) * Li[i]

# Plotting results
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(time, Dh, label='Dynamic Happiness')
plt.plot(time, Ds, label='Dynamic Sadness')
plt.plot(time, Df, label='Dynamic Fear')
plt.legend()
plt.title('Dynamic Emotions Over Time')

plt.subplot(3, 1, 2)
plt.plot(time, Pa, label='Positive Affect')
plt.legend()
plt.title('Positive Affect Over Time')

plt.subplot(3, 1, 3)
plt.plot(time, Si, label='Short-term Willingness to Interact')
plt.plot(time, Li, label='Long-term Willingness to Interact')
plt.plot(time, Ri, label='Readiness to Interact')
plt.legend()
plt.title('Willingness and Readiness to Interact Over Time')

plt.tight_layout()
plt.show()
