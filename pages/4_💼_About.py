import streamlit as st
import libs.common as tools


st.set_page_config(
    page_title="About",
    page_icon="💼",
    initial_sidebar_state="expanded"
)

st.write("# DIPR430685 - FINAL👾")
tools.add_logo()
st.markdown(
    """
    ## 🎓 Contribution 
    - Name: Ngô Hoàng Khánh Duy
    - MSSV: 20133030
    ## 💻 Tech
    - Streamlit ([streamlit.io](https://streamlit.io))
    - Python 3.7.0 (https://docs.python.org/3/whatsnew/3.7.html)
"""
)
