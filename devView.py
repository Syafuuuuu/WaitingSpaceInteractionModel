import streamlit as st
import matplotlib.pyplot as plt

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

# Initialize session state for agents and television positions if not already initialized
if 'agents' not in st.session_state:
    st.session_state.agents = []
    st.session_state.agentsDetail = []

if 'television' not in st.session_state:
    st.session_state.television = []

st.button('### Clear', type="primary")


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

    # Right side: Split into top and bottom sections
    with col2:
        st.write("### Personality")
        Ex = st.slider("Extravertness", min_value=0.0, max_value=1.0, step=numStep, key="Ex")
        Op = st.slider("Openness", min_value=0.0, max_value=1.0, step=numStep, key="Op")
        Nu = st.slider("Neuroticism", min_value=0.0, max_value=1.0, step=numStep, key="Nu")
        
        st.write("### Emotions")
        Ha = st.slider("Happiness", min_value=0.0, max_value=1.0, step=numStep, key="Ha")
        Sd = st.slider("Sadness", min_value=0.0, max_value=1.0, step=numStep, key="Sd")
        Fe = st.slider("Fear", min_value=0.0, max_value=1.0, step=numStep, key="Fe")
        
        st.write("### Exhaustion")
        Eh = st.slider("Exhaustion", min_value=0.0, max_value=1.0, step=numStep, key="Eh")


    with col3:
        
        st.write("### Hobbies")
        hobbies = ['Cognitive', 'Cultural', 'Religious', 'Social', 'Gardening', 'Travelling', 'Physical']
        for idx, hobby in enumerate(hobbies):
            st.checkbox(hobby, key=f"hobby_{idx}")
            
        st.write("### Interests")
        interests = ['Realistic', 'Investigating', 'Artistic', 'Social', 'Enterprising', 'Conventional']
        for idx, interest in enumerate(interests):
            st.checkbox(interest, key=f"interest_{idx}")

    with col4:
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
                    
                    st.session_state.agentsDetail.append(Agent(name=name, agent_X=agent_x, agent_Y=agent_y, Ha=Ha, Sd=Sd, Fe=Fe, Ex=Ex, Op=Op, Nu=Nu, Eh=Eh, Nc=0.5, Ni=0.5))
                    for agent in st.session_state.agentsDetail:
                        print(agent.name)
                        print(agent.posX)
                        print(agent.posY)
                    
                    
                    st.rerun()  # Re-render the app to update the grid
                else:
                    st.error("Coordinates must be between 0 and 10.")
            except ValueError:
                st.error("Please enter valid integer coordinates.")
            
        st.write("### Agent List")
        
    #bottom Spacing
    bot_col1, bot_col2 = st.columns([2,3])

    with bot_col2:
        # Bottom Section: Three columns for Language, Race, Religion
        st.write("### Additional Information")
        col_lang, col_race, col_religion = st.columns(3)

        with col_lang:
            st.write("#### Language")
            st.checkbox("English", key="lang_english")
            st.checkbox("Malay", key="lang_malay")
            st.checkbox("Mandarin", key="lang_mandarin")
            st.checkbox("Tamil", key="lang_tamil")

        with col_race:
            st.write("#### Race")
            st.checkbox("Malay", key="race_malay")
            st.checkbox("Chinese", key="race_chinese")
            st.checkbox("Indian", key="race_indian")
            st.checkbox("Others", key="race_others")

        with col_religion:
            st.write("#### Religion")
            st.checkbox("Islam", key="religion_islam")
            st.checkbox("Christianity", key="religion_christianity")
            st.checkbox("Buddhism", key="religion_buddhism")
            st.checkbox("Hinduism", key="religion_hinduism")