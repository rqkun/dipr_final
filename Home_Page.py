import streamlit as st
import libs.common as tools


st.set_page_config(
    page_title="Home",
    page_icon="🎥",
    initial_sidebar_state="expanded"
)

st.write("# DIPR430685 - FINAL👾")
st.write("20133030 - Ngô Hoàng Khánh Duy")
tools.add_logo()

st.markdown(
    """
    ## About
    This is a project for DIPR430685_22_2_10 🎥 class.
    The project was built using Python 3 on streamlit with 3 different pages.
    ### Which include:
    - 👤 Face Detection  
    - 👥 Face Regconition
    - 📷 Image Processing (Chapter 3,4,5,9)
    ### Contact:
    - Gmail: nhkduy0809@gmail.com
    - Github: [github.com](https://github.com/rqkun)
"""
)
