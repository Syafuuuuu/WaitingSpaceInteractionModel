import streamlit as st
import matplotlib.pyplot as plt
from Agent import Agent as Agent

st.set_page_config(layout="wide")

# class Agent:
#     def __init__(self, name, agent_X, agent_Y, Ha, Sd, Fe, Ex, Op, Nu, Eh, Nc, Ni, HobbArr, IntArr, LangArr, RaceArr, RelArr) -> None:
#         self.name = name
#         self.posX = agent_X
#         self.posY = agent_Y
#         self.Ha = Ha
#         self.Sd = Sd
#         self.Fe = Fe
#         self.Ex = Ex
#         self.Op = Op
#         self.Nu = Nu
#         self.Eh = Eh
#         self.Nc = Nc
#         self.Ni = Ni
#         self.Dh = 0.5
#         self.Ds = 0.5
#         self.Df = 0.5
#         self.Li = 0.5
#         self.HobbArr = HobbArr
#         self.IntArr = IntArr
#         self.LangArr = LangArr
#         self.RaceArr = RaceArr
#         self.RelArr = RelArr
        
        
    # def printInfo(self):
    #     print("Name: " , self.name)
    #     print("PosX: " , self.posX)
    #     print("PosY: " , self.posY)
    #     print("Ha: " , self.Ha)
    #     print("Sd: " , self.Sd)
    #     print("Fe: " , self.Fe)
    #     print("Ex: " , self.Ex)
    #     print("Op: " , self.Op)
    #     print("Nu: " , self.Nu)
    #     print("Eh: " , self.Eh)
    #     print("Nc: " , self.Nc)
    #     print("Ni: " , self.Ni)
        
        

# # Initialize session state for agents and television positions if not already initialized
# if 'agents' not in st.session_state:
#     st.session_state.agents = []
#     st.session_state.agentsDetail = []

# if 'television' not in st.session_state:
#     st.session_state.television = []

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
        
        st.button('### Clear', type="primary")
        
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
        #hobbies = ['Cognitive', 'Cultural', 'Religious', 'Social', 'Gardening', 'Travelling', 'Physical']
        hob1 = st.checkbox("Cognitive", key="hob1")
        hob2 = st.checkbox("Cultural", key="hob2")
        hob3 = st.checkbox("Religious", key="hob3")
        hob4 = st.checkbox("Social", key="hob4")
        hob5 = st.checkbox("Gardening", key="hob5")
        hob6 = st.checkbox("Travelling", key="hob6")
        hob7 = st.checkbox("Physical", key="hob7")
        #for idx, hobby in enumerate(hobbies):
        #    st.checkbox(hobby, key=f"hobby_{idx}")
            
        st.write("### Interests")
        int1 = st.checkbox("Realistic", key="int1")
        int2 = st.checkbox("Investigating", key="int2")
        int3 = st.checkbox("Artistic", key="int3")
        int4 = st.checkbox("Social", key="int4")
        int5 = st.checkbox("Enterprising", key="int5")
        int6 = st.checkbox("Conventional", key="int6")
        #interests = ['Realistic', 'Investigating', 'Artistic', 'Social', 'Enterprising', 'Conventional']
        #for idx, interest in enumerate(interests):
        #    st.checkbox(interest, key=f"interest_{idx}")

    with col4:
        
        st.write("### Additional Information")
        #Language
        st.write("#### Language")
        lang1 = st.checkbox("English", key="lang_english")
        lang2 = st.checkbox("Malay", key="lang_malay")
        lang3 = st.checkbox("Mandarin", key="lang_mandarin")
        lang4 = st.checkbox("Tamil", key="lang_tamil")
        
        #Race
        st.write("#### Race")
        race1 = st.checkbox("Malay", key="race_malay")
        race2 = st.checkbox("Chinese", key="race_chinese")
        race3 = st.checkbox("Indian", key="race_indian")
        race4 = st.checkbox("Others", key="race_others")
        
        #Relgiion
        st.write("#### Religion")
        rel1 = st.checkbox("Islam", key="religion_islam")
        rel2 = st.checkbox("Christianity", key="religion_christianity")
        rel3 = st.checkbox("Buddhism", key="religion_buddhism")
        rel4 = st.checkbox("Hinduism", key="religion_hinduism")        
        
        # name = st.text_input('Name', key='name')
        
        # # Input fields for television coordinates
        # agent_x = st.text_input("Agent X-coordinate", "7", key='agent_x')
        # agent_y = st.text_input("Agent Y-coordinate", "7", key='agent_y')
        
        # if st.button('### Add Agent'):
        #     try:
        #         hobbArr = [hob1,hob2,hob3,hob4,hob5,hob6,hob7]
        #         intArr = [int1, int2, int3, int4, int5, int6]
        #         langArr = [lang1, lang2, lang4, lang4]
        #         raceArr = [race1, race2,race3,race4]
        #         relArr = [rel1, rel2, rel3, rel4]
        #         print(hobbArr)
        #         print(intArr)
        #         # Convert input to integer coordinates
        #         agent_x = int(agent_x)
        #         agent_y = int(agent_y)
        #         if 0 <= agent_x <= 10 and 0 <= agent_y <= 10:  # Ensure within grid range
        #             # Add new television position to session state
        #             st.session_state.agents.append((agent_x, agent_y))
                    
        #             st.session_state.agentsDetail.append(Agent(name=name, agent_X=agent_x, agent_Y=agent_y, Ha=Ha, Sd=Sd, Fe=Fe, Ex=Ex, Op=Op, Nu=Nu, Eh=Eh, Nc=0.5, Ni=0.5))
        #             # for agent in st.session_state.agentsDetail:
        #             #     agent.printInfo()
                    
                    
        #             st.rerun()  # Re-render the app to update the grid
        #         else:
        #             st.error("Coordinates must be between 0 and 10.")
        #     except ValueError:
        #         st.error("Please enter valid integer coordinates.")
            
        # st.write("### Agent List")
        # for agent in st.session_state.agentsDetail:
        #     st.write(agent.name)
        
    #bottom Spacing
    # bot_col1, bot_col2 = st.columns([2,3])

    # with bot_col2:

name = st.sidebar.text_input('Name', key='name')

# Input fields for television coordinates
agent_x = st.sidebar.text_input("Agent X-coordinate", "7", key='agent_x')
agent_y = st.sidebar.text_input("Agent Y-coordinate", "7", key='agent_y')

if st.sidebar.button('### Add Agent'):
    try:
        hobbArr = [hob1,hob2,hob3,hob4,hob5,hob6,hob7]
        intArr = [int1, int2, int3, int4, int5, int6]
        langArr = [lang1, lang2, lang4, lang4]
        raceArr = [race1, race2,race3,race4]
        relArr = [rel1, rel2, rel3, rel4]
        print(hobbArr)
        print(intArr)
        # Convert input to integer coordinates
        agent_x = int(agent_x)
        agent_y = int(agent_y)
        if 0 <= agent_x <= 10 and 0 <= agent_y <= 10:  # Ensure within grid range
            # Add new television position to session state
            st.session_state.agents.append((agent_x, agent_y))
            
            st.session_state.agentsDetail.append(Agent(name=name, agent_X=agent_x, agent_Y=agent_y, Ha=Ha, Sd=Sd, Fe=Fe, Ex=Ex, Op=Op, Nu=Nu, Eh=Eh, Nc=0.5, Ni=0.5, HobbArr=hobbArr, IntArr=intArr, LangArr=langArr, RaceArr=raceArr, RelArr=relArr))
            # for agent in st.session_state.agentsDetail:
            #     agent.printInfo()
            
            
            st.rerun()  # Re-render the app to update the grid
        else:
            st.error("Coordinates must be between 0 and 10.")
    except ValueError:
        st.error("Please enter valid integer coordinates.")

st.sidebar.write("### Agent List")
for agent in st.session_state.agentsDetail:
    st.sidebar.write(agent.name)