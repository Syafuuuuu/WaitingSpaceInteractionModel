import streamlit as st
import pandas as pd
from itertools import combinations

# Define the Agent class with boolean values for arrays
class Agent:
    def __init__(self, name, agent_X, agent_Y, Ha, Sd, Fe, Ex, Op, Nu, Eh, Nc, Ni, HobbArr, IntArr, LangArr, RaceArr, RelArr) -> None:
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
        self.HobbArr = HobbArr  # Now this will be a list of booleans
        self.IntArr = IntArr    # Now this will be a list of booleans
        self.LangArr = LangArr  # Now this will be a list of booleans
        self.RaceArr = RaceArr  # Now this will be a list of booleans
        self.RelArr = RelArr    # Now this will be a list of booleans

# Create a list of Agent objects (example data with True/False arrays)
agents = [
    Agent(
        name="Agent A",
        agent_X=10,
        agent_Y=20,
        Ha=5,
        Sd=7,
        Fe=3,
        Ex=4,
        Op=6,
        Nu=8,
        Eh=9,
        Nc=1,
        Ni=2,
        HobbArr=[True, False],  # Example boolean array
        IntArr=[True, False],   # Example boolean array
        LangArr=[True, False],  # Example boolean array
        RaceArr=[True, False],  # Example boolean array
        RelArr=[True, False]    # Example boolean array
    ),
    Agent(
        name="Agent B",
        agent_X=15,
        agent_Y=25,
        Ha=6,
        Sd=8,
        Fe=4,
        Ex=5,
        Op=7,
        Nu=9,
        Eh=10,
        Nc=3,
        Ni=4,
        HobbArr=[True, True],
        IntArr=[False, True],
        LangArr=[True, True],
        RaceArr=[True, False],
        RelArr=[False, True]
    ),
    Agent(
        name="Agent C",
        agent_X=20,
        agent_Y=30,
        Ha=7,
        Sd=6,
        Fe=5,
        Ex=8,
        Op=7,
        Nu=7,
        Eh=6,
        Nc=5,
        Ni=3,
        HobbArr=[True, False],
        IntArr=[True, False],
        LangArr=[False, True],
        RaceArr=[True, True],
        RelArr=[True, False]
    ),
]

# Jaccard similarity function for comparing boolean sets
def jaccard_similarity(set1, set2):
    intersection = sum([1 for a, b in zip(set1, set2) if a == b == True])
    union = sum([1 for a, b in zip(set1, set2) if a == True or b == True])
    return intersection / union if union != 0 else 0

# Function to calculate inter-agent similarity for all attributes
def calculate_inter_agent_similarity(agent1, agent2):
    attributes = ["HobbArr", "IntArr", "LangArr", "RaceArr", "RelArr"]
    similarities = {}
    
    for attr in attributes:
        sim = jaccard_similarity(getattr(agent1, attr), getattr(agent2, attr))
        similarities[attr] = sim
    
    return similarities

# Calculate the inter-agent similarities for all agent pairs
agent_pairs = combinations(agents, 2)
inter_agent_similarities = {}

for agent1, agent2 in agent_pairs:
    similarity = calculate_inter_agent_similarity(agent1, agent2)
    inter_agent_similarities[(agent1.name, agent2.name)] = similarity

# Calculate average inter-agent similarity for each agent
def calculate_average_inter_agent_similarity(agent, other_agents):
    total_similarity = {attr: 0 for attr in ["HobbArr", "IntArr", "LangArr", "RaceArr", "RelArr"]}
    num_comparisons = 0
    
    for other_agent in other_agents:
        if agent != other_agent:
            similarity = calculate_inter_agent_similarity(agent, other_agent)
            for attr in total_similarity:
                total_similarity[attr] += similarity[attr]
            num_comparisons += 1
    
    # Calculate the average similarity for each attribute
    average_similarity = {attr: total_similarity[attr] / num_comparisons for attr in total_similarity}
    
    # Return the average similarity across all attributes
    return sum(average_similarity.values()) / len(average_similarity)

# Calculate average inter-agent similarity for each agent
average_inter_agent_similarities = {}
for agent in agents:
    avg_similarity = calculate_average_inter_agent_similarity(agent, agents)
    average_inter_agent_similarities[agent.name] = avg_similarity

# Calculate the cluster similarity (average of all agents' average similarities)
def calculate_cluster_similarity(average_inter_agent_similarities):
    return sum(average_inter_agent_similarities.values()) / len(average_inter_agent_similarities)

cluster_similarity = calculate_cluster_similarity(average_inter_agent_similarities)

# Display the results in Streamlit
st.title("Agent Similarity Analysis")

# Display Inter-agent similarities
st.header("Inter-agent Similarities")
for (agent1_name, agent2_name), similarities in inter_agent_similarities.items():
    st.subheader(f"Similarity between {agent1_name} and {agent2_name}:")
    st.write(similarities)

# Display Average inter-agent similarities
st.header("Average Inter-agent Similarity for Each Agent")
for agent_name, avg_similarity in average_inter_agent_similarities.items():
    st.subheader(f"{agent_name}: {avg_similarity:.2f}")

# Display Cluster Similarity
st.header("Cluster Similarity")
st.write(f"Cluster Similarity: {cluster_similarity:.2f}")
