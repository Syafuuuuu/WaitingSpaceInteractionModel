import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

st.set_page_config(layout="wide")

class Agent:
    def __init__(self, name, agent_X, agent_Y, Ha, Sd, Fe, Ex, Op, Nu, Eh, Nc, Ni) -> None:
        self.name = name
        self.posX = agent_X
        self.posY = agent_Y
        self.Ha = Ha
        self.Sd = Sd
        self.Fe = Fe
        self.Ex = Ex
        self.Op = Op
        self.Nu = Nu
        self.Eh = Eh
        self.Nc = Nc
        self.Ni = Ni
        self.Dh = 0.5
        self.Ds = 0.5
        self.Df = 0.5
        self.Li = 0.5

# # Initialize session state for agents and television positions if not already initialized
# if 'agents' not in st.session_state:
#     st.session_state.agents = []
#     st.session_state.agentsDetail = []

# if 'television' not in st.session_state:
#     st.session_state.television = []

if st.button('### Clear', type="primary"):
    st.session_state.agents.clear()
    st.session_state.television.clear()
    st.session_state.agentsDetail.clear()

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def cluster_agents(agents, televisions):
    """Cluster agents based on the closest TV using Euclidean distance."""
    clusters = defaultdict(list)  # Dictionary to hold clusters
    
    # Iterate through each agent
    for agent in agents:
        closest_tv_index = None
        min_distance = float('inf')  # Start with an infinitely large distance
        
        # Calculate distance to each TV
        for index, tv in enumerate(televisions):
            distance = euclidean_distance(agent, tv)
            if distance < min_distance:
                min_distance = distance
                closest_tv_index = index
        
        # Assign agent to the closest TV cluster
        clusters[closest_tv_index].append(agent)
    
    return dict(clusters)  # Return clusters as a regular dictionary

# Technical Container
with st.container():
    # Create columns
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

    #NumStep
    numStep = 0.01
    # Left side: Grid for agents and TV

    with col1:
        st.write("### Spatial Grid Layout")

        # Create the figure and grid layout
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xticks(range(11))
        ax.set_yticks(range(11))
        ax.grid(True)

        # Plot existing agents (blue dots)
        for agent in st.session_state.agents:
            ax.plot(agent[0], agent[1], 'bo')

        # Plot televisions (green triangles)
        for tv in st.session_state.television:
            ax.plot(tv[0], tv[1], 'g^')

        # Display the grid
        st.pyplot(fig)
        
        st.write("### Add Television")
        
        # Input fields for television coordinates
        tv_x = st.text_input("Television X-coordinate", "7")
        tv_y = st.text_input("Television Y-coordinate", "7")
        
        # Add television button with input validation
        if st.button("Add Television"):
            try:
                # Convert input to integer coordinates
                tv_x = int(tv_x)
                tv_y = int(tv_y)
                if 0 <= tv_x <= 10 and 0 <= tv_y <= 10:  # Ensure within grid range
                    # Add new television position to session state
                    st.session_state.television.append((tv_x, tv_y))
                    st.rerun()  # Re-render the app to update the grid
                else:
                    st.error("Coordinates must be between 0 and 10.")
            except ValueError:
                st.error("Please enter valid integer coordinates.")

    with col2:
        name = st.text_input('Name', key='name')
        
        # Input fields for television coordinates
        agent_x = st.text_input("Agent X-coordinate", "7", key='agent_x')
        agent_y = st.text_input("Agent Y-coordinate", "7", key='agent_y')
        
        if st.button('### Add Agent'):
            try:
                # Convert input to integer coordinates
                agent_x = int(agent_x)
                agent_y = int(agent_y)
                if 0 <= agent_x <= 10 and 0 <= agent_y <= 10:  # Ensure within grid range
                    # Add new television position to session state
                    st.session_state.agents.append((agent_x, agent_y))
                    
                    st.session_state.agentsDetail.append(Agent(name=name, agent_X=agent_x, agent_Y=agent_y, Ha=0, Sd=0, Fe=0, Ex=0, Op=0, Nu=0, Eh=0, Nc=0.5, Ni=0.5))
                    for agent in st.session_state.agentsDetail:
                        print(agent.name)
                        print(agent.posX)
                        print(agent.posY)
                        print(agent.Ni)
                    
                    
                    st.rerun()  # Re-render the app to update the grid
                else:
                    st.error("Coordinates must be between 0 and 10.")
            except ValueError:
                st.error("Please enter valid integer coordinates.")
            
        st.write("### Agent List")
        for agent in st.session_state.agentsDetail:
            st.write(agent.name)
    
    with col3:
        if st.button("### Cluster Agents"):
            clusters = cluster_agents(st.session_state.agents, st.session_state.television)
            st.write("### Clusters of Agents")
            for tv_index, agents in clusters.items():
                st.write(f"**Television {tv_index + 1}:**")
                for agent in agents:
                    st.write(f"- Agent at {agent}")
    
    with col4:
        st.write("YEet")