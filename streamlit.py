import streamlit as st 
from yolo import YoloDetecter
import numpy as np
from PIL import Image



st.header("welcome to my project")

task= st.sidebar.selectbox(
   "choose task",
    ("DETECTION", "SEGMENTATION")
)

model_size = st.sidebar.selectbox(
    "Choose Model Size",
    ("NANO", "SMALL", "MEDIUM", "LARGE", "XLARGE")
)

if task=="DETECTION":
    model=YoloDetecter(task=task,size=model_size)
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        image = np.array(image)

        detected = model.detect(image)
        st.image(detected, channels="RGB")
        
if task=="SEGMENTATION":
    model=YoloDetecter(task=task,size=model_size)
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        image = np.array(image)

        detected = model.segment_image(image)
        st.image(detected)
    
    
    


