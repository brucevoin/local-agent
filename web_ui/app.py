import streamlit as st
from settings import settings_dialog

from websocket_client import send_message

st.title("Local Agent")
st.write("Your private work assistant")

pompt = st.text_input("Enter your prompt here...", key="prompt")
if pompt:
    if st.button("Send"):
        def callback(message):
            print("****************")
            print(message)
        res = send_message(pompt)
        st.write(res)
    
        
# Variables 
settings = {}
toolbox = {}
model = None

with st.container(border=True):
    with st.sidebar:
        st.header(":blue[Options:]")
        st.multiselect("Select models",["deepseek","openai"])
        st.multiselect("Select tools",["web-search"])
        st.slider("temprature",value=0,max_value=1,min_value=-1)
        st.number_input("Max Consecutive Replay",value=5)
        
        model = st.selectbox("Interact Model: ", ["Text", "Voice","Video"])
        st.divider()
        st.header(":blue[Settings]")
        if st.button("Settings",use_container_width=True):
            settings_dialog()

if model == "Text":
    message = st.chat_input("Enter your message: ")
elif model == "Voice":
    st.write("This is a voice model")
elif model == "Video":
    st.write("This is a video model")