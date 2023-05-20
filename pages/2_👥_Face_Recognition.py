import streamlit as st
import numpy as np
import cv2 as cv
import joblib
import libs.common as tools

st.set_page_config(page_title="Face Regconition Demo", page_icon="👥",initial_sidebar_state="expanded")
tools.add_logo()

st.markdown("# 👥 Face Regconition Demo")
st.write(
    """"""
)

def OpenColor(uploaded_file):
    img_color = cv.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv.IMREAD_COLOR)
    imageRGB = cv.cvtColor(img_color , cv.COLOR_BGR2RGB)
    return imageRGB

def visualize(input, faces, thickness=2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            # print('Face {}, top-left coordinates: ({:.0f}, {:.0f}), box width: {:.0f}, box height {:.0f}, score: {:.2f}'.format(idx, face[0], face[1], face[2], face[3], face[-1]))

            coords = face[:-1].astype(np.int32)
            cv.rectangle(input, (coords[0], coords[1]), (coords[0]+coords[2], coords[1]+coords[3]), (0, 255, 0), thickness)
            cv.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv.circle(input, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv.circle(input, (coords[12], coords[13]), 2, (0, 255, 255), thickness)

FRAME_WINDOW = st.image([])
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","tif"])
if uploaded_file is not None:
    
    img_color = OpenColor(uploaded_file)
    FRAME_WINDOW = st.image(img_color)
    
    svc = joblib.load('models/face_reg/svc.pkl')
    mydict = ['KhanhDuy', 'NhatMinh', 'ThayDuc']
    detector = cv.FaceDetectorYN.create(
        'models/face_detect/face_detection_yunet_2022mar.onnx',
        "",
        (320, 320),
        0.9,
        0.3,
        5000
    )
    recognizer = cv.FaceRecognizerSF.create('models/face_reg/face_recognition_sface_2021dec.onnx',"")
    frameWidth = img_color.shape[1]
    frameHeight = img_color.shape[0]
    detector.setInputSize([frameWidth, frameHeight])
    frame = cv.resize(img_color, (frameWidth, frameHeight))
    faces = detector.detect(frame) # faces is a tuple
    # Draw results on the input image
    if faces[1] is not None:
            face_align = recognizer.alignCrop(frame, faces[1][0])
            face_feature = recognizer.feature(face_align)
            test_predict = svc.predict(face_feature)
            result = mydict[test_predict[0]]
            cv.putText(frame,result,(1,50),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    visualize(frame, faces)
    # Visualize results
    FRAME_WINDOW.image(frame, channels='RGB')
