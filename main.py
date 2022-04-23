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
        filebyte = st.file_uploader("Upload Image", accept_multiple_files=False, type='jpg')
        if filebyte is not None:
            st.image(filebyte)
            opt = st.radio("Text or Text File:", ('Text', 'Text File'))
            if opt == 'Text':
                txt_input = st.text_input("Enter Text:")
                if txt_input and st.button("Encode") is not None: Encode(filebyte, txt_input)
            elif opt == 'Text File':
                txt_file = st.file_uploader("Upload Text File:", accept_multiple_files=False, type='txt')
                if txt_file is not None:
                    with open(os.path.join("", txt_file.name), "wb") as f:
                        f.write(txt_file.getbuffer())
                    with open(txt_file.name) as f:
                        data = f.readline()
                        if data and st.button("Encode") is not None: Encode(filebyte, data)
    elif imgencd == 'Decode':
        dimg = st.file_uploader("Upload File", type='jpg')
        if dimg is not None:
            st.image(dimg)
            if st.button("Decode"):Decode(dimg)