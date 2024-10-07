import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Initialize session state for agents and television positions if not already initialized
if 'agents' not in st.session_state:
    st.session_state.agents = []

if 'television' not in st.session_state:
    st.session_state.television = []

# Create columns
col1, col2 = st.columns([1, 2])

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
    # Top Section: Split into left and right
    top_left, top_right = st.columns(2)
    
    with top_left:
        st.write("### Personality")
        personality_1 = st.text_input("Variable 1", "Calm", key="personality_1")
        personality_2 = st.text_input("Variable 2", "Outgoing", key="personality_2")
        personality_3 = st.text_input("Variable 3", "Assertive", key="personality_3")
        
        st.write("### Emotions")
        emotions_1 = st.text_input("Emotion 1", "Happy", key="emotions_1")
        emotions_2 = st.text_input("Emotion 2", "Anxious", key="emotions_2")
        emotions_3 = st.text_input("Emotion 3", "Excited", key="emotions_3")
        
        st.write("### Exhaustion")
        exhaustion_1 = st.text_input("Exhaustion Level 1", "Low", key="exhaustion_1")
        exhaustion_2 = st.text_input("Exhaustion Level 2", "Moderate", key="exhaustion_2")
        exhaustion_3 = st.text_input("Exhaustion Level 3", "High", key="exhaustion_3")
    
    with top_right:
        st.write("### Hobbies")
        hobbies = ['Cognitive', 'Cultural', 'Religious', 'Social', 'Gardening', 'Travelling', 'Physical']
        for idx, hobby in enumerate(hobbies):
            st.checkbox(hobby, key=f"hobby_{idx}")
        
        st.write("### Interests")
        interests = ['Realistic', 'Investigating', 'Artistic', 'Social', 'Enterprising', 'Conventional']
        for idx, interest in enumerate(interests):
            st.checkbox(interest, key=f"interest_{idx}")
    
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
