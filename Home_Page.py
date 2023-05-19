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
    ### About - English 
    This is a project for DIPR430685_22_2_10 🎥 class.
    The project was built on streamlit with 3 different pages.
    Which include:
    - 👤 Face Detection  
    - 👥 Face Regconition
    - 📷 Image Processing (Chapter 3,4,5,9)
    ### About - Vietnamese
    Đây là project cuối kì của môn Xử lý ảnh số (DIPR430685_22_2_10 🎥)
    Project được dựng trên framework streamlit với 3 trang khác nhau
    tương ứng với 3 mục:
    - 👤 Face Detection: Phát hiện khuôn mặt
    - 👥 Face Regconition: Nhận dạng khuôn mặt
    - 📷 Image Processing: Xử lý ảnh (Chương 3,4,5,9)
"""
)
