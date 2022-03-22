import numpy as np
import streamlit as st
import pytesseract as pt
from PIL import Image #python Imaging library, to open image, streamlit does not support cv2 directly

st.set_option('deprecation.showfileUploaderEncoding',False) #to warning ignore
st.title("OCR-Optical Character Recognition")  #print title and text
st.text("Upload the Image")

uploaded_file=st.sidebar.file_uploader("Choose an image...",type=['jpg','png','jpeg'])
if uploaded_file is not None:
  img=Image.open(uploaded_file)  #reads the image, similar cv2.imread
  st.image(img,caption="Uploaded Image",use_column_width=True) 
  st.write("")  #print black space

  if st.button("PREDICT"):  #creates a button called as predict
    st.write("Result...")   
    op=pt.image_to_string(img)  #pytesseract converts img to text and prints
    st.title(op)
