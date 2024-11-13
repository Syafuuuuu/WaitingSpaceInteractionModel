import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Public Interaction Model in Public Spaces")
st.sidebar.success("Select a page above.")

# Initialize session state for agents and television positions if not already initialized
if 'agents' not in st.session_state:
    st.session_state.agents = []
    st.session_state.agentsDetail = []

if 'television' not in st.session_state:
    st.session_state.television = []