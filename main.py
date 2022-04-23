import os
import streamlit as st
from stegano import exifHeader as stg

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
    st.header('Decoded Text:')
    st.subheader(text)

st.title("Image Steganography")
st.header("")
st.header("")
st.subheader('Select the type of file:')
imag = st.radio('', ('Image', 'Audio', 'Video'))
if imag == 'Image':
    st.subheader('Type of operation:')
    imgencd = st.radio('', ('Encode', 'Decode'))
    if imgencd == 'Encode':
        st.subheader('Upload Image as JPG:')
        filebyte = st.file_uploader("", accept_multiple_files=False, type='jpg')
        if filebyte is not None:
            st.image(filebyte)
            st.subheader('Text or Text File:')
            opt = st.radio("", ('Text', 'Text File'))
            if opt == 'Text':
                st.subheader('Enter Text:')
                txt_input = st.text_input("")
                if txt_input and st.button("Encode") is not None: Encode(filebyte, txt_input)
            elif opt == 'Text File':
                st.subheader('Upload File as TXT:')
                txt_file = st.file_uploader("", accept_multiple_files=False, type='txt')
                if txt_file is not None:
                    with open(os.path.join("", txt_file.name), "wb") as f:
                        f.write(txt_file.getbuffer())
                    with open(txt_file.name) as f:
                        data = f.readline()
                        if data and st.button("Encode") is not None:Encode(filebyte, data)
    elif imgencd == 'Decode':
        dimg = st.file_uploader("Upload File", type='jpg')
        if dimg is not None:
            st.image(dimg)
            if st.button("Decode"):Decode(dimg)