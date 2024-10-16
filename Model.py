import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D

#--- STRANGER SOCIAL INTERACTION MODEL - SSIC MODEL ---%#

# Clear variables
plt.close('all')

# Time settings
maxLimY = 1.2  # graph Y axis max
minLimX = 0    # graph X axis min
numStep = 1000
numStepChange = 1000
dt = 0.1
k = 12  # Psi Cap

# Agent Object
agentArray = np.array([
    [0.1, 0.9, 0.9, 0.1, 0.1, 0.9, 0.9, 0.1, 0.1],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.9, 0.1, 0.1, 0.9, 0.9, 0.1, 0.1, 0.9, 0.9]
])

numAgents, numAttributes = agentArray.shape

# Declare All Variables and Set INITIAL VALUES
Pa = np.zeros((numAgents, numStep))
Si = np.zeros((numAgents, numStep))
Ri = np.zeros((numAgents, numStep))
Dh = np.full((numAgents, numStep), 0.5)
Ds = np.full((numAgents, numStep), 0.5)
Df = np.full((numAgents, numStep), 0.5)
Li = np.full((numAgents, numStep), 0.5)
Psi = np.zeros((numAgents, numStep))

# Difference arrays
dfDh = np.zeros((numAgents, numStepChange))
dfDs = np.zeros((numAgents, numStepChange))
dfDf = np.zeros((numAgents, numStepChange))
dfLi = np.zeros((numAgents, numStepChange))

# Initialisation of all parameters
beta_Pa = 0.2
omega_Ps = 0.5
beta_Si = 0.5
omega_Ri = 0.0
beta_Ri = 1.0

gamma_Dh = 0.1
lambda_Dh = 0.03
gamma_Ds = 0.1
lambda_Ds = 0.03
gamma_Df = 0.1
lambda_Df = 0.03
gamma_Li = 0.5

# Run the model at t=1
for i in range(numAgents):
    Pa[i, 0] = Dh[i, 0] - (beta_Pa * Ds[i, 0])
    Si[i, 0] = beta_Si * Pa[i, 0] + (1 - beta_Si) * (omega_Ps * agentArray[i, 3] + (1 - omega_Ps) * agentArray[i, 4]) * agentArray[i, 7] * (1 - agentArray[i, 6])
    Psi[i, 0] = 1 / (1 + np.exp(-k * (Df[i, 0] * agentArray[i, 5])))
    Ri[i, 0] = beta_Ri * (omega_Ri * Si[i, 0] + (1 - omega_Ri) * Li[i, 0]) * agentArray[i, 8] * (1 - Psi[i, 0])

# Run the model at t=2
for t in range(1, numStep):
    for i in range(numAgents):
        Dh[i, t] = Dh[i, t-1] + gamma_Dh * (agentArray[i, 0] - lambda_Dh) * Dh[i, t-1] * (1 - Dh[i, t-1]) * dt
        Ds[i, t] = Ds[i, t-1] + gamma_Ds * (agentArray[i, 1] - lambda_Ds) * Ds[i, t-1] * (1 - Ds[i, t-1]) * dt
        Df[i, t] = Df[i, t-1] + gamma_Df * (agentArray[i, 2] - lambda_Df) * Df[i, t-1] * (1 - Df[i, t-1]) * dt

        Pa[i, t] = Dh[i, t] - (beta_Pa * Ds[i, t])
        Si[i, t] = beta_Si * Pa[i, t] + (1 - beta_Si) * (omega_Ps * agentArray[i, 3] + (1 - omega_Ps) * agentArray[i, 4]) * agentArray[i, 7] * (1 - agentArray[i, 6])
        Li[i, t] = Li[i, t-1] + gamma_Li * (Si[i, t-1] - Li[i, t-1]) * (1 - Li[i, t-1]) * Li[i, t-1] * dt
        Psi[i, t] = Df[i, t] * agentArray[i, 5] / (1 + np.exp(-k * (Df[i, t] * agentArray[i, 5])))
        Ri[i, t] = beta_Ri * (omega_Ri * Si[i, t] + (1 - omega_Ri) * Li[i, t]) * agentArray[i, 8] * (1 - Psi[i, t])

# Checking equilibrium
for t in range(2, numStepChange):
    for i in range(numAgents):
        dfDh[i, t] = Dh[i, t-1] - Dh[i, t-2]
        dfDs[i, t] = Ds[i, t-1] - Ds[i, t-2]
        dfDf[i, t] = Df[i, t-1] - Df[i, t-2]
        dfLi[i, t] = Li[i, t-1] - Li[i, t-2]

# Plotting
# fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# fig.suptitle('Temporal Factors')

# axes[0, 0].imshow(Dh, aspect='auto')
# axes[0, 0].set_title('Dynamic Happiness')

# axes[0, 1].imshow(Ds, aspect='auto')
# axes[0, 1].set_title('Dynamic Sadness')

# axes[1, 0].imshow(Df, aspect='auto')
# axes[1, 0].set_title('Dynamic Fear')

# axes[1, 1].imshow(Li, aspect='auto')
# axes[1, 1].set_title('Long-Term Willingness to Interact')

# plt.show()

# Additional code for other graphs can be similarly plotted

#Simpler 3-D Graph

# Set up the figure for multiple 3D plots
fig = plt.figure(figsize=(12, 8))
fig.suptitle('Temporal Factors (3D Surface Plots)')

# Time and agent dimensions for meshgrid
time = np.arange(numStep)
agents = np.arange(numAgents)
T, A = np.meshgrid(time, agents)

# Plot Dynamic Happiness
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(T, A, Dh, cmap='viridis')
ax1.set_title('Dynamic Happiness')
ax1.set_xlabel('Time steps')
ax1.set_ylabel('Agents')
ax1.set_zlabel('Levels')

# Plot Dynamic Sadness
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(T, A, Ds, cmap='plasma')
ax2.set_title('Dynamic Sadness')
ax2.set_xlabel('Time steps')
ax2.set_ylabel('Agents')
ax2.set_zlabel('Levels')

# Plot Dynamic Fear
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax3.plot_surface(T, A, Df, cmap='cividis')
ax3.set_title('Dynamic Fear')
ax3.set_xlabel('Time steps')
ax3.set_ylabel('Agents')
ax3.set_zlabel('Levels')

# Plot Long-Term Willingness to Interact
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot_surface(T, A, Li, cmap='magma')
ax4.set_title('Long-Term Willingness to Interact')
ax4.set_xlabel('Time steps')
ax4.set_ylabel('Agents')
ax4.set_zlabel('Levels')

plt.tight_layout()
plt.show()

# Set up the figure for multiple 3D plots
fig = plt.figure(figsize=(12, 8))
fig.suptitle('Instantaneous Factors (3D Surface Plots)')

# Time and agent dimensions for meshgrid
T, A = np.meshgrid(time, agents)

# Plot Positive Affect
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(T, A, Pa, cmap='viridis')
ax1.set_title('Positive Affect')
ax1.set_xlabel('Time steps')
ax1.set_ylabel('Agents')
ax1.set_zlabel('Levels')

# Plot Short-Term Willingness to Interact
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(T, A, Si, cmap='plasma')
ax2.set_title('Short-Term Willingness to Interact')
ax2.set_xlabel('Time steps')
ax2.set_ylabel('Agents')
ax2.set_zlabel('Levels')

# Plot Experienced Fear
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax3.plot_surface(T, A, Psi, cmap='cividis')
ax3.set_title('Experienced Fear')
ax3.set_xlabel('Time steps')
ax3.set_ylabel('Agents')
ax3.set_zlabel('Levels')

# Plot Readiness to Interact
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot_surface(T, A, Ri, cmap='magma')
ax4.set_title('Readiness to Interact')
ax4.set_xlabel('Time steps')
ax4.set_ylabel('Agents')
ax4.set_zlabel('Levels')

plt.tight_layout()
plt.show()


#Interactive Graph

# # Plot Dynamic Happiness
# fig = go.Figure()
# fig.add_trace(go.Surface(z=Dh, x=dt, y=numAgents, colorscale='Viridis'))
# fig.update_layout(title='Dynamic Happiness', scene=dict(
#                     xaxis_title='Time Steps',
#                     yaxis_title='Agents',
#                     zaxis_title='Levels'))
# fig.show()

# # Similarly, create figures for other factors
# # Dynamic Sadness
# fig = go.Figure()
# fig.add_trace(go.Surface(z=Ds, x=dt, y=numAgents, colorscale='Plasma'))
# fig.update_layout(title='Dynamic Sadness', scene=dict(
#                     xaxis_title='Time Steps',
#                     yaxis_title='Agents',
#                     zaxis_title='Levels'))
# fig.show()

# # Dynamic Fear
# fig = go.Figure()
# fig.add_trace(go.Surface(z=Df, x=dt, y=numAgents, colorscale='Cividis'))
# fig.update_layout(title='Dynamic Fear', scene=dict(
#                     xaxis_title='Time Steps',
#                     yaxis_title='Agents',
#                     zaxis_title='Levels'))
# fig.show()

# # Long-Term Willingness to Interact
# fig = go.Figure()
# fig.add_trace(go.Surface(z=Li, x=dt, y=numAgents, colorscale='Magma'))
# fig.update_layout(title='Long-Term Willingness to Interact', scene=dict(
#                     xaxis_title='Time Steps',
#                     yaxis_title='Agents',
#                     zaxis_title='Levels'))
# fig.show()