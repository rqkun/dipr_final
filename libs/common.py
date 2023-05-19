import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/pt3bm6M.png/200/200);
                background-repeat: no-repeat;
                background-size: 200px;
                padding-top: 120px;
                background-position: 60px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "DIPR430685";
                margin-left: 80px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )