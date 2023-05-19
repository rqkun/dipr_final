import cv2
import numpy as np
import streamlit as st
import libs.Chapter03 as ch3
import libs.Chapter04 as ch4
import libs.Chapter05 as ch5
import libs.Chapter09 as ch9
import libs.common as tools
st.set_page_config(page_title="Image Processing", page_icon="📷",initial_sidebar_state="expanded")
tools.add_logo()

st.markdown("# 📷 Image Processing")

st.write("""""")


def OpenGrey(uploaded_file):
    img_grey = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    return img_grey

def OpenColor(uploaded_file):
    img_color = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    imageRGB = cv2.cvtColor(img_color , cv2.COLOR_BGR2RGB)
    return imageRGB

def onNegative():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onNegative_bt=st.button("Apply")
            if onNegative_bt:
                with col2:
                    imgout = ch3.Negative(img_grey)
                    st.image(imgout, clamp=True)

def onLogarit():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            col1, col2 = st.columns(2)
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onLogarit_bt=st.button("Apply")
            if onLogarit_bt:
                with col2:
                    imgout = ch3.Logarit(img_grey)
                    st.image(imgout, clamp=True)

def onPower():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onPower_bt=st.button("Apply")
            if onPower_bt:
                with col2:
                    imgout = ch3.Power(img_grey)
                    st.image(imgout, clamp=True)

def onPiecewiseLinear():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onPower_bt=st.button("Apply")
            if onPower_bt:
                with col2:
                    imgout = ch3.PiecewiseLinear(img_grey)
                    st.image(imgout, clamp=True)

def onHistogram():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            col1, col2 = st.columns(2)
            with col1:
                img_grey = OpenGrey(uploaded_file)
                st.image(img_grey, clamp=True)
                onHistogram_bt=st.button("Apply")
            if onHistogram_bt:
                with col2:
                    imgout = ch3.Histogram(img_grey)
                    st.image(imgout, clamp=True)

def onHistEqual():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onHistEqual_bt=st.button("Apply")
            if onHistEqual_bt:
                with col2:
                    imgout = cv2.equalizeHist(img_grey)
                    st.image(imgout, clamp=True)

def onHistEqualColor():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            col1, col2 = st.columns(2)
            with col1:
                img_color = OpenColor(uploaded_file)
                st.image(img_color, clamp=True)
                onHistEqualColor_bt=st.button("Apply")
            if onHistEqualColor_bt:
                with col2:
                    imgout = ch3.HistEqualColor(img_color)
                    st.image(imgout, clamp=True)

def onLocalHist():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onLocalHist_bt=st.button("Apply")
            if onLocalHist_bt:
                with col2:
                    imgout = ch3.LocalHist(img_grey)
                    st.image(imgout, clamp=True)

def onHistStat():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onHistStat_bt=st.button("Apply")
            if onHistStat_bt:
                with col2:
                    imgout = ch3.HistStat(img_grey)
                    st.image(imgout, clamp=True)

def onBoxFilter():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onBoxFilter_bt=st.button("Apply")
            if onBoxFilter_bt:
                with col2:
                    imgout = cv2.blur(img_grey,(21,21))
                    st.image(imgout, clamp=True)

def onGaussFilter():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onGaussFilter_bt=st.button("Apply")
            if onGaussFilter_bt:
                with col2:
                    imgout = cv2.GaussianBlur(img_grey,(43,43),7.0)
                    st.image(imgout, clamp=True)

def onThreshold():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onThreshold_bt=st.button("Apply")
            if onThreshold_bt:
                with col2:
                    imgout = ch3.Threshold(img_grey)
                    st.image(imgout, clamp=True)

def onMedianFilter():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            st.image(img_grey, clamp=True)
            col1, col2 = st.columns(2)
            with col1:
                onMedianFilter_bt=st.button("Apply")
            if onMedianFilter_bt:
                with col2:
                    imgout = cv2.medianBlur(img_grey,7)
                    st.image(imgout, clamp=True)

def onSharpen():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onSharpen_bt=st.button("Apply")
            if onSharpen_bt:
                with col2:
                    imgout = ch3.Sharpen(img_grey)
                    st.image(imgout, clamp=True)

def onGradient():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onGradient_bt=st.button("Apply")
            if onGradient_bt:
                with col2:
                    imgout = ch3.Gradient(img_grey)
                    st.image(imgout, clamp=True)

def onSpectrum():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onSpectrum_bt=st.button("Apply")
            if onSpectrum_bt:
                with col2:
                    imgout = ch4.Spectrum(img_grey)
                    st.image(imgout, clamp=True)

def onFrequencyFilter():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onFrequencyFilter_bt=st.button("Apply")
            if onFrequencyFilter_bt:
                with col2:
                    imgout = ch4.FrequencyFilter(img_grey)
                    st.image(imgout, clamp=True)
def onDrawNotchRejectFilter():
        onDrawNotchRejectFilter_bt=st.button("Draw")
        if onDrawNotchRejectFilter_bt:
            imgout = ch4.DrawNotchRejectFilter()
            st.image(imgout, clamp=True)
def onRemoveMoire():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onRemoveMoire_bt=st.button("Apply")
            if onRemoveMoire_bt:
                with col2:
                    imgout = ch4.RemoveMoire(img_grey)
                    st.image(imgout, clamp=True)
def onCreateMotionNoise():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onCreateMotionNoise_bt=st.button("Apply")
            if onCreateMotionNoise_bt:
                with col2:
                    imgout = ch5.CreateMotionNoise(img_grey)
                    st.image(imgout, clamp=True)
def onDenoiseMotion():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onDenoiseMotion_bt=st.button("Apply")
            if onDenoiseMotion_bt:
                with col2:
                    imgout = ch5.DenoiseMotion(img_grey)
                    st.image(imgout, clamp=True)
def onDenoisestMotion():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onDenoisestMotion_bt=st.button("Apply")
            if onDenoisestMotion_bt:
                with col2:
                    temp = cv2.medianBlur(img_grey, 7)
                    imgout = ch5.DenoiseMotion(temp)
                    st.image(imgout, clamp=True)
def onConnectedComponent():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onConnectedComponent_bt=st.button("Apply")
            if onConnectedComponent_bt:
                with col2:
                    imgout = ch9.ConnectedComponent(img_grey)
                    st.image(imgout, clamp=True)
def onCountRice():
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
        if uploaded_file is not None:
            img_grey = OpenGrey(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_grey, clamp=True)
                onCountRice_bt=st.button("Apply")
            if onCountRice_bt:
                with col2:
                    imgout = ch9.CountRice(img_grey)
                    st.image(imgout, clamp=True)


chapters = st.sidebar.selectbox("Chapter",["Chapter 3", "Chapter 4", "Chapter 5", "Chapter 9"])
if chapters =="Chapter 3":
    chapter3 = st.sidebar.selectbox("Option",["Negative","Logarit","Power","PieceWiseLinear","Histogram","HistEqual","HistEqualColor","LocalHist","HistStat","BoxFilter","GaussFilter","Threshold","MedianFilter","Sharpen", "Gradient"])
    if chapter3 =="Negative":
        st.subheader('Chater 3 - Negative')
        onNegative()
    elif chapter3 =="Logarit":
        st.subheader('Chater 3 - Logarit')
        onLogarit()
    elif chapter3 =="Power":
        st.subheader('Chater 3 - Power')
        onPower()
    elif chapter3 =="PieceWiseLinear":
        st.subheader('Chater 3 - PiecewiseLinear')
        onPiecewiseLinear()
    elif chapter3 =="Histogram":
        st.subheader('Chater 3 - Histogram')
        onHistogram()
    elif chapter3 =="HistEqual":
        st.subheader('Chater 3 - Histogram Equalization')
        onHistEqual()
    elif chapter3 =="HistEqualColor":
        st.subheader('Chater 3 - Colored Histogram Equalization')
        onHistEqualColor()
    elif chapter3 =="LocalHist":
        st.subheader('Chater 3 - Histogram Localization')
        onLocalHist()
    elif chapter3 =="HistStat":
        st.subheader('Chater 3 - Histogram Statistics')
        onHistStat()
    elif chapter3 =="BoxFilter":
        st.subheader('Chater 3 - Box Filter')
        onBoxFilter()
    elif chapter3 =="GaussFilter":
        st.subheader('Chater 3 - Gaussian Filter')
        onGaussFilter()
    elif chapter3 =="Threshold":
        st.subheader('Chater 3 - Threshold Filter')
        onThreshold()
    elif chapter3 =="MedianFilter":
        st.subheader('Chater 3 - Median Filter')
        onMedianFilter()
    elif chapter3 =="Sharpen":
        st.subheader('Chater 3 - Sharpen')
        onSharpen()
    elif chapter3 =="Gradient":
        st.subheader('Chater 3 - Gradient')
        onGradient()
elif chapters =="Chapter 4":
    chapter4 = st.sidebar.selectbox("Option",["Spectrum","FrequencyFilter","DrawNotchRejectFilter","RemoveMoire"])
    if chapter4 =="Spectrum":
        st.subheader('Chater 4 - Spectrum')
        onSpectrum()
    elif chapter4 =="FrequencyFilter":
        st.subheader('Chater 4 - Frequency Filter')
        onFrequencyFilter()
    elif chapter4 =="DrawNotchRejectFilter":
        st.subheader('Chater 4 - Draw Notch Reject Filter')
        onDrawNotchRejectFilter()
    elif chapter4 =="RemoveMoire":
        st.subheader('Chater 4 - Remove Moire')
        onRemoveMoire()
elif chapters =="Chapter 5":
    chapter5 = st.sidebar.selectbox("Option",["CreateMotionNoise","DenoiseMotion","DenoisestMotion"])
    if chapter5 =="CreateMotionNoise":
        st.subheader('Chater 5 - Create Motion Noise')
        onCreateMotionNoise()
    elif chapter5 =="DenoiseMotion":
        st.subheader('Chater 5 - Denoise Motion')
        onDenoiseMotion()
    elif chapter5 =="DenoisestMotion":
        st.subheader('Chater 5 - Denoisest Motion')
        onDenoisestMotion()
elif chapters =="Chapter 9":
    chapter9 = st.sidebar.selectbox("Option",["ConnectedComponent","CountRice"])
    if chapter9 =="ConnectedComponent":
        st.subheader('Chater 9 - Connected Component')
        onConnectedComponent()
    elif chapter9 =="CountRice":
        st.subheader('Chater 9 - Count Rice')
        onCountRice()

