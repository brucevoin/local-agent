import streamlit as st
from code_editor import code_editor
import requests

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

back_end_base_url = "http://localhost:5000/api/v1/"


def load_models():
    response = requests.request("GET", back_end_base_url + "models")
    if response.status_code == 200:
        data = response.json()
        models = data["data"]
        return models
    else:
        return None


def create_model(data):
    response = requests.request(
        method="POST", url=back_end_base_url + "models", json=data
    )
    if response.status_code == 200:
        return True
    else:
        return False


@st.experimental_dialog("Settings")
def settings_dialog():
    tab_models, tab_tools = st.tabs(["Models", "Tools"])
    models = load_models()

    model_dict = {}
    for model in models:
        if not model["model"] in model_dict.keys():
            model_dict[model["model"]] = model

    model_names = list(model_dict.keys())
    model_names.append("+")

    with tab_models:
        selected_model = st.selectbox("Select Model", model_names)
        if selected_model:
            if selected_model == "+":
                model_name = st.text_input("Model Name:red[*]:")
                description = st.text_input("Description:", key="model_description")
                api_key = st.text_input("API Key:", key="model_api_key")
                base_url = st.text_input("Base URL:", key="model_base_url")
                if st.button("Submit", use_container_width=True, key="model_submit"):
                    data = {
                        "model": model_name,
                        "description": description,
                        "api_key": api_key,
                        "base_url": base_url,
                    }
                    create_model(data=data)
            else:
                selected_model = model_dict[selected_model]

                model_name = st.text_input(
                    "Model Name:red[*]:", value=selected_model["model"]
                )
                description = st.text_input(
                    "Description:",
                    key="model_description",
                    value=selected_model["description"],
                )
                api_key = st.text_input(
                    "API Key:", key="model_api_key", value=selected_model["api_key"]
                )
                base_url = st.text_input(
                    "Base URL:", key="model_base_url", value=selected_model["base_url"]
                )
                if st.button("Update",use_container_width=True):
                    pass
                if st.button("Delete",use_container_width=True):
                    pass

    with tab_tools:
        selected_tool = st.selectbox("Select Tool", ["web_search", "code_search", "+"])
        if selected_tool:
            if selected_tool == "+":
                tool_name = st.text_input("Tool Name:red[*]:")
                description = st.text_input("Description:", key="tool_description")
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
                description = st.text_input("Description:", key="tool_description")
                response_dict = code_editor(
                    default_function,
                    lang="python",
                    buttons=btn_settings_editor_btns,
                    props=ace_props,
                    allow_reset=True,
                    key="code_editor",
                )
                code = response_dict["text"]
            if st.button("Submit", use_container_width=True, key="tool_submit"):
                pass
