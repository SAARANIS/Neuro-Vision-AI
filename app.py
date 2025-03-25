import os
import sys
import streamlit as st
import webbrowser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "model")))
from pages._pages import home
from pages._pages import about
from pages._pages import github
from pages._pages import try_it


# Function to open the 3D brain visualization
def open_3d_visualization():
    webbrowser.open("https://brainchop.org/", new=2)



routes = {
    "Home": home.main,
    "Try it out": try_it.main,
    "3D Brain Visualization": open_3d_visualization,
    # "About": about.main,
    # "GitHub": github.main,
}

st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon=":brain:",
    layout="wide",
    menu_items={
        "Get Help": "",
        "Report a bug": "",
        "About": "Detecting brain tumors using *deep Convolutional Neural Networks*",
    },
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
   [data-testid="stSelectbox"] .st-emotion-cache-13bfgw8 p {
        font-size: 24px;
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

def format_func(page):
    return page[0]

page = st.selectbox(
    "Menu",
    list(routes.items()),
    index=0,
    format_func=format_func,
)

page[1]()

# Include the title.html file


