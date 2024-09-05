import numpy as np
import matplotlib.pyplot as plt
import math

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
gamma_Li = 0.5   #Long-Term

#Readiness to Interact Para
omega_Ri = 0.5
beta_Ri = 1.0

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
Ha = 0.7 #Happiness
Sd = 0.1 #Sadness
Fe = 0.7 #Fear
Ex = 0.7 #Extrovertness
Op = 0.8 #Openness
Nu = 0.9 #Neuroticism
Eh = 0.5 #Level of Exhaustion

#Inter-Agent Variables
Nc = 0.5 #Cultural Preference Similarities
Ni = 0.5 #Interest Similarities

# Initial conditions
Dh[0] = 0.01
Ds[0] = 0.01
Df[0] = 0.01
Pa[0] = 0.01
Si[0] = 0.2
Li[0] = 0.01
Ri[0] = 0.01

# Simulation loop
for t in range(1, len(time)):
    #Dyanmic Emotions
    Dh[t] = Dh[t-1] + gamma_Dh * (Ha - lambda_Dh) * Dh[t-1] * (1 - Dh[t-1]) * dt
    Ds[t] = Ds[t-1] + gamma_Ds * (Sd - lambda_Ds) * Ds[t-1] * (1 - Ds[t-1]) * dt
    Df[t] = Df[t-1] + gamma_Df * (Fe - lambda_Df) * Df[t-1] * (1 - Df[t-1]) * dt
    
    #Postiive Affect
    Pa[t] = Dh[t] - beta_Pa * Ds[t]
    
    # Willingness to  Interact
    # Short Term
    Si[t] = beta_Si * Pa[t] + (1 - beta_Si) * (omega_Ps * Ex + (1 - omega_Ps) * Op) * Nc * (1 - Eh)
    # Long Term
    Li[t] = Li[t-1] + gamma_Li * (Si[t-1] - Li[t-1]) * (1 - Li[t-1]) * Li[t-1] * dt
    
    #Experienced Fear
    k = 1.0
    Psi = 1/(1+math.e**(-1*k*(Df[t]*Nu)))
    
    #Interaction Readiness
    Ri[t] = beta_Ri*(omega_Ri * Si[t] + (1 - omega_Ri) * Li[t]) * Ni * (1-Psi)

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
