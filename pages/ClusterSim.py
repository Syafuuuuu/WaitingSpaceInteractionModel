import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

st.title("Clustered Simulation Output")

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def cluster_agents(agents, televisions):
    """Cluster agents based on the closest TV using Euclidean distance."""
    clusters = defaultdict(list)
    
    for agent in agents:
        closest_tv_index = None
        min_distance = float('inf')
        
        for index, tv in enumerate(televisions):
            distance = euclidean_distance((agent.posX, agent.posY), tv)
            if distance < min_distance:
                min_distance = distance
                closest_tv_index = index
        
        clusters[closest_tv_index].append(agent)
    
    return dict(clusters)

def RunModel(Agents: np.array, cluster_index):
    """Run the model for a specific cluster of agents."""
    numAgents, numAttributes = Agents.shape
    numStep = 10000
    numStepChange = 10000
    dt = 0.1
    k = 12

    # Declare and initialize all necessary variables
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

    for i in range(numAgents):
        Pa[i, 0] = Dh[i, 0] - (beta_Pa * Ds[i, 0])
        Si[i, 0] = beta_Si * Pa[i, 0] + (1 - beta_Si) * (omega_Ps * Agents[i, 3] + (1 - omega_Ps) * Agents[i, 4]) * Agents[i, 7] * (1 - Agents[i, 6])
        Psi[i, 0] = 1 / (1 + np.exp(-k * (Df[i, 0] * Agents[i, 5])))
        Ri[i, 0] = beta_Ri * (omega_Ri * Si[i, 0] + (1 - omega_Ri) * Li[i, 0]) * Agents[i, 8] * (1 - Psi[i, 0])

    for t in range(1, numStep):
        for i in range(numAgents):
            Dh[i, t] = Dh[i, t-1] + gamma_Dh * (Agents[i, 0] - lambda_Dh) * Dh[i, t-1] * (1 - Dh[i, t-1]) * dt
            Ds[i, t] = Ds[i, t-1] + gamma_Ds * (Agents[i, 1] - lambda_Ds) * Ds[i, t-1] * (1 - Ds[i, t-1]) * dt
            Df[i, t] = Df[i, t-1] + gamma_Df * (Agents[i, 2] - lambda_Df) * Df[i, t-1] * (1 - Df[i, t-1]) * dt

            Pa[i, t] = Dh[i, t] - (beta_Pa * Ds[i, t])
            Si[i, t] = beta_Si * Pa[i, t] + (1 - beta_Si) * (omega_Ps * Agents[i, 3] + (1 - omega_Ps) * Agents[i, 4]) * Agents[i, 7] * (1 - Agents[i, 6])
            Li[i, t] = Li[i, t-1] + gamma_Li * (Si[i, t-1] - Li[i, t-1]) * (1 - Li[i, t-1]) * Li[i, t-1] * dt
            Psi[i, t] = Df[i, t] * Agents[i, 5] / (1 + np.exp(-k * (Df[i, t] * Agents[i, 5])))
            Ri[i, t] = beta_Ri * (omega_Ri * Si[i, t] + (1 - omega_Ri) * Li[i, t]) * Agents[i, 8] * (1 - Psi[i, t])

    # Checking equilibrium
    for t in range(2, numStepChange):
        for i in range(numAgents):
            dfDh[i, t] = Dh[i, t-1] - Dh[i, t-2]
            dfDs[i, t] = Ds[i, t-1] - Ds[i, t-2]
            dfDf[i, t] = Df[i, t-1] - Df[i, t-2]
            dfLi[i, t] = Li[i, t-1] - Li[i, t-2]
            
    # Set up the figure for multiple 3D plots for Temporal Factors
    fig1 = plt.figure(figsize=(12, 8))
    fig1.suptitle('Temporal Factors (3D Surface Plots)')

    # Time and agent dimensions for meshgrid
    time = np.arange(numStep)
    agents = np.arange(numAgents)
    T, A = np.meshgrid(time, agents)

    # Plot Dynamic Happiness
    ax1 = fig1.add_subplot(2, 2, 1, projection='3d')
    ax1.plot_surface(T, A, Dh, cmap='viridis')
    ax1.set_title('Dynamic Happiness')
    ax1.set_xlabel('Time steps')
    ax1.set_ylabel('Agents')
    ax1.set_zlabel('Levels')

    # Plot Dynamic Sadness
    ax2 = fig1.add_subplot(2, 2, 2, projection='3d')
    ax2.plot_surface(T, A, Ds, cmap='plasma')
    ax2.set_title('Dynamic Sadness')
    ax2.set_xlabel('Time steps')
    ax2.set_ylabel('Agents')
    ax2.set_zlabel('Levels')

    # Plot Dynamic Fear
    ax3 = fig1.add_subplot(2, 2, 3, projection='3d')
    ax3.plot_surface(T, A, Df, cmap='cividis')
    ax3.set_title('Dynamic Fear')
    ax3.set_xlabel('Time steps')
    ax3.set_ylabel('Agents')
    ax3.set_zlabel('Levels')

    # Plot Long-Term Willingness to Interact
    ax4 = fig1.add_subplot(2, 2, 4, projection='3d')
    ax4.plot_surface(T, A, Li, cmap='magma')
    ax4.set_title('Long-Term Willingness to Interact')
    ax4.set_xlabel('Time steps')
    ax4.set_ylabel('Agents')
    ax4.set_zlabel('Levels')

    plt.tight_layout()
    st.pyplot(fig1)
    
    # Plot 2D line plots for each parameter over time, with different colors per agent
    fig2, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig2.suptitle('Temporal Factors (2D Line Plots)')

    # Dynamic Happiness
    for i in range(numAgents):
        axes[0, 0].plot(time, Dh[i, :], label=f'Agent {i+1}')
    axes[0, 0].set_title('Dynamic Happiness')
    axes[0, 0].set_xlabel('Time steps')
    axes[0, 0].set_ylabel('Levels')
    axes[0, 0].legend()

    # Dynamic Sadness
    for i in range(numAgents):
        axes[0, 1].plot(time, Ds[i, :], label=f'Agent {i+1}')
    axes[0, 1].set_title('Dynamic Sadness')
    axes[0, 1].set_xlabel('Time steps')
    axes[0, 1].set_ylabel('Levels')
    axes[0, 1].legend()

    # Dynamic Fear
    for i in range(numAgents):
        axes[1, 0].plot(time, Df[i, :], label=f'Agent {i+1}')
    axes[1, 0].set_title('Dynamic Fear')
    axes[1, 0].set_xlabel('Time steps')
    axes[1, 0].set_ylabel('Levels')
    axes[1, 0].legend()

    # Long-Term Willingness to Interact
    for i in range(numAgents):
        axes[1, 1].plot(time, Li[i, :], label=f'Agent {i+1}')
    axes[1, 1].set_title('Long-Term Willingness to Interact')
    axes[1, 1].set_xlabel('Time steps')
    axes[1, 1].set_ylabel('Levels')
    axes[1, 1].legend()

    plt.tight_layout()
    st.pyplot(fig2)


    # Set up the figure for multiple 3D plots for Instantaneous Factors
    fig3 = plt.figure(figsize=(12, 8))
    fig3.suptitle('Instantaneous Factors (3D Surface Plots)')

    # Time and agent dimensions for meshgrid
    T, A = np.meshgrid(time, agents)

    # Plot Positive Affect
    ax1 = fig3.add_subplot(2, 2, 1, projection='3d')
    ax1.plot_surface(T, A, Pa, cmap='viridis')
    ax1.set_title('Positive Affect')
    ax1.set_xlabel('Time steps')
    ax1.set_ylabel('Agents')
    ax1.set_zlabel('Levels')

    # Plot Short-Term Willingness to Interact
    ax2 = fig3.add_subplot(2, 2, 2, projection='3d')
    ax2.plot_surface(T, A, Si, cmap='plasma')
    ax2.set_title('Short-Term Willingness to Interact')
    ax2.set_xlabel('Time steps')
    ax2.set_ylabel('Agents')
    ax2.set_zlabel('Levels')

    # Plot Experienced Fear
    ax3 = fig3.add_subplot(2, 2, 3, projection='3d')
    ax3.plot_surface(T, A, Psi, cmap='cividis')
    ax3.set_title('Experienced Fear')
    ax3.set_xlabel('Time steps')
    ax3.set_ylabel('Agents')
    ax3.set_zlabel('Levels')

    # Plot Readiness to Interact
    ax4 = fig3.add_subplot(2, 2, 4, projection='3d')
    ax4.plot_surface(T, A, Ri, cmap='magma')
    ax4.set_title('Readiness to Interact')
    ax4.set_xlabel('Time steps')
    ax4.set_ylabel('Agents')
    ax4.set_zlabel('Levels')

    plt.tight_layout()
    # plt.show()
    st.pyplot(fig3)
    
    # Plot 2D line plots for each parameter over time, with different colors per agent
    fig4, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig4.suptitle('Temporal Factors (2D Line Plots)')

    # Positive Affect
    for i in range(numAgents):
        axes[0, 0].plot(time, Pa[i, :], label=f'Agent {i+1}')
    axes[0, 0].set_title('Positive Affect')
    axes[0, 0].set_xlabel('Time steps')
    axes[0, 0].set_ylabel('Levels')
    axes[0, 0].legend()

    # Short-Term Willingness to Interact
    for i in range(numAgents):
        axes[0, 1].plot(time, Si[i, :], label=f'Agent {i+1}')
    axes[0, 1].set_title('Short-Term Willingness to Interact')
    axes[0, 1].set_xlabel('Time steps')
    axes[0, 1].set_ylabel('Levels')
    axes[0, 1].legend()

    # Experienced Fear
    for i in range(numAgents):
        axes[1, 0].plot(time, Psi[i, :], label=f'Agent {i+1}')
    axes[1, 0].set_title('Experienced Fear')
    axes[1, 0].set_xlabel('Time steps')
    axes[1, 0].set_ylabel('Levels')
    axes[1, 0].legend()

    # Readiness to Interact
    for i in range(numAgents):
        axes[1, 1].plot(time, Ri[i, :], label=f'Agent {i+1}')
    axes[1, 1].set_title('Readiness to Interact')
    axes[1, 1].set_xlabel('Time steps')
    axes[1, 1].set_ylabel('Levels')
    axes[1, 1].legend()

    plt.tight_layout()
    st.pyplot(fig4)

if st.button("Run Simulation"):
    # Cluster the agents based on proximity to televisions
    clusters = cluster_agents(st.session_state.agentsDetail, st.session_state.television)

    st.write("### Running Simulation for Each Cluster")

    # Run the model for each cluster independently
    for tv_index, agents in clusters.items():
        st.write(f"#### Cluster for Television {tv_index + 1}:")
        RunModel(np.array([[agent.Ha, agent.Sd, agent.Fe, agent.Ex, agent.Op, agent.Nu, agent.Eh, agent.Nc, agent.Ni] for agent in agents]), tv_index)

