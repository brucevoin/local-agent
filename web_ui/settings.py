
import streamlit as st
from code_editor import code_editor

ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}

default_function = """
def foo(age: int, name: str):
    st.write(f"Hey! My name is {name} and I'm {age} years old")
"""

btn_settings_editor_btns = [
    {
        "name": "Copy",
        "feather": "Copy",
        "hasText": True,
        "alwaysOn": True,
        "commands": ["copyAll"],
        "style": {"top": "0rem", "right": "0.4rem"},
    },
    {
        "name": "Save",
        "feather": "RefreshCw",
        "primary": True,
        "hasText": True,
        "showWithIcon": True,
        "commands": ["submit"],
        "style": {"bottom": "0rem", "right": "0.4rem"},
    },
]

@st.experimental_dialog("Settings")
def settings_dialog():
    tab_models,tab_tools = st.tabs(["Models", "Tools"])
    with tab_models:
        selected_mode = st.selectbox("Select Model",["deepseek","openai","+"])
        if selected_mode:
            if selected_mode == "+":
                model_name = st.text_input("Model Name:red[*]:")
                description = st.text_input("Description:",key="model_description")
                api_key = st.text_input("API Key:",key="model_api_key")
                base_url = st.text_input("Base URL:",key="model_base_url")
            else: 
                model_name = st.text_input("Model Name:red[*]:")
                description = st.text_input("Description:",key="model_description")
                api_key = st.text_input("API Key:",key="model_api_key")
                base_url = st.text_input("Base URL:",key="model_base_url")
                
            if st.button("Submit",use_container_width=True,key="model_submit"):
                pass
        
    with tab_tools:
        selected_tool = st.selectbox("Select Tool",["web_search","code_search","+"])
        if selected_tool:
            if selected_tool == "+":
                tool_name = st.text_input("Tool Name:red[*]:")
                description = st.text_input("Description:",key="tool_description")
                response_dict = code_editor(
                    default_function,
                    lang="python",
                    buttons=btn_settings_editor_btns,
                    props=ace_props,
                    allow_reset=True,
                    key="code_editor",
                )
                code = response_dict["text"]
            else: 
                tool_name = st.text_input("Tool Name:red[*]:")
                description = st.text_input("Description:",key="tool_description")
                response_dict = code_editor(
                    default_function,
                    lang="python",
                    buttons=btn_settings_editor_btns,
                    props=ace_props,
                    allow_reset=True,
                    key="code_editor",
                )
                code = response_dict["text"]
            if st.button("Submit",use_container_width=True,key="tool_submit"):
                pass