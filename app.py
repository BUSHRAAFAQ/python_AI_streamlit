import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


# title
st.title("GIANIC [PYTHON] AI ! :airplane:")
# st header and subheader
st.header("About QUARTER 02 RESULT Form :star:")
st.subheader("Opinion about  QUARTER 03 :thumbsup:" )
#text

st.markdown("Hello everyone,welcome to my python station streamlit web App, I hope you like it! :rainbow:" )
#image (ensure 'logo.png'is in the same directory)

img= Image.open('logo.png')
st.image(img,caption='GOVERNOR HOUSE is one of the best IT initiative platform')

#st.markdown("<style>div[data-testide='stImage'] {display:flex;justify-content: center;}</style>",unsafe_allow_html=True)
# st.colorful text


name = st.text_input('Write your Name')
st.text_input('Write your Father name')
st.text_input('Write your Roll number')
#selectbox
st.selectbox('what is your Gender?',('','male','female'))
#slider
st.slider('what is your age?',12,50)
#sidebar
st.sidebar.title("About me!:woman:")

st.sidebar.write("""This is me Bushra Afaq,I am in Q3 (Alhmdullillah)because of my amazing teachers motivated and trained me *sir Hamza*
*sir Bilal Mohammad*
*sir Aneeq*
 I am very thankful to all of you !:sunny:""")
#st.sidebar.button('like'/'dislike')


st.sidebar.text('afaqbushrs38@gmail.com')
st.sidebar.radio ('Are you with me on this platform',('Active','Inactive'))


#selectbox
st.selectbox('where do you live?',[' ','Karachi','Hyderabad','Bahriatown'])
st.selectbox('what is your Qualification?',[' ','Matric','Inter','Graduate'])
st.selectbox('what is your profession?',[' ','own Business','programmer','Teacher','Engineer','others'])
st.selectbox('what is your Grading in Q2?',[' ','A','B','C'])
st.selectbox('what is you Remarks?',[' ','Best','Better','Good'])
#video
#vid = open('class.mp4','rb').read()
#st.video(vid)
#text-area
message=st.text_area('write your Experience about this course')
#text-input
gmail=st.text_input('Enter your Gmail ID:')

#data visulization
st.title('Bar chart')
st.text('hightest students passing rank')
data=pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)
st.title('Line chart')
st.write('rank for A grade students')
data=pd.DataFrame(np.random.randn(25,2),columns=['x','y'])
st.line_chart(data)
#display raw code
#code
st.text('How to install streamlit')
st.code ('pip install streamlit')
#upload file
st.file_uploader("upload your file/folder")

#balloons
st.balloons()
#final massage

st.title ('good luck!')