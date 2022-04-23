import os
import streamlit as st
from stegano import exifHeader as stg
from PIL import Image

def Encode(img, text):
    global fileopen
    with open(os.path.join("", img.name), "wb") as f:
        f.write(img.getbuffer())
    FileOpen = "" + img.name
    stg.hide(FileOpen, "NewImg.jpg", text)
    with open("NewImg.jpg",'rb') as file:
        st.download_button(label="Download Image",file_name='Encoded_Image.jpg', data=file, mime='image/jpg')

def Decode(dimg):
    global dfileopen
    with open(os.path.join("", dimg.name), "wb") as f:
        f.write(dimg.getbuffer())
    dfileopen = "" + dimg.name
    text = stg.reveal(dfileopen)
    st.write(text)

st.title("Image Steganography")
imag = st.radio('Select the type of file', ('Image', 'Audio', 'Video'))
if imag == 'Image':
    imgencd = st.radio('Type of Operation', ('Encode', 'Decode'))
    if imgencd == 'Encode':
        text = st.text_input("Enter text to encode")
        filebytes = st.file_uploader("Upload File", type='jpg')
        if filebytes and text is not None:
            st.image(filebytes)
            if st.button("Encode"):Encode(filebytes, text)
    elif imgencd == 'Decode':
        dimg = st.file_uploader("Upload File", type='jpg')
        if dimg is not None:
            st.image(dimg)
            if st.button("Decode"):Decode(dimg)