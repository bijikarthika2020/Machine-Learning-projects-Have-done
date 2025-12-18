import os
import json
import streamlit as st
from openai import OpenAI

# -----------------------------
# Load API Key from config.json
# -----------------------------
working_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(working_dir, "config.json")

with open(config_path) as f:
    config_data = json.load(f)

os.environ["OPENAI_API_KEY"] = config_data["OPENAI_API_KEY"]

# Initialize OpenAI client (NEW SDK)
client = OpenAI()

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="GPT-4o Chat",
    page_icon="💬",
    layout="centered"
)

st.title("🤖 GPT-4o Chatbot")

# -----------------------------
# Initialize chat history
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Display chat history
# -----------------------------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User input
# -----------------------------
user_prompt = st.chat_input("Ask GPT-4o...")

if user_prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Save user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_prompt
    })

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content

    # Save assistant response
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_response
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
