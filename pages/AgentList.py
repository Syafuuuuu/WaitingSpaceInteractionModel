import streamlit as st
import pandas as pd


st.title("Agent list")

# Prepare data for a dataframe
data = []
for agent in st.session_state.agentsDetail:
    data.append({
        "Name": agent.name,
        "Position (X, Y)": f"({agent.posX}, {agent.posY})",
        "Ha": agent.Ha,
        "Sd": agent.Sd,
        "Fe": agent.Fe,
        "Ex": agent.Ex,
        "Op": agent.Op,
        "Nu": agent.Nu,
        "Eh": agent.Eh,
        "Nc": agent.Nc,
        "Ni": agent.Ni,
        # Ensure all list items are converted to strings
        "Hobbies": ', '.join([str(item) for item in agent.HobbArr]),
        "Interests": ', '.join([str(item) for item in agent.IntArr]),
        "Languages": ', '.join([str(item) for item in agent.LangArr]),
        "Race": ', '.join([str(item) for item in agent.RaceArr]),
        "Religion": ', '.join([str(item) for item in agent.RelArr]),
    })

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Streamlit interface to display the dataframe
st.title("Agent Details")

# Display the agent details in a tabular format
st.dataframe(df)