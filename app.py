import streamlit as st
from streamlit_chat import message
from src.faq import FAQ

# Initialize FAQ system
faq_system = FAQ()

# Ensure session state variables are initialized
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "user_id" not in st.session_state:
    st.session_state["user_id"] = ""

if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""

# Callback to update user ID
def update_user_id():
    st.session_state["user_id"] = st.session_state.get("user_id_input", "").strip()

# Callback to process user input and clear input field
def process_input():
    user_question = st.session_state.get("input_text", "").strip()
    user_id = st.session_state.get("user_id", "").strip()

    if not user_id:
        st.warning("Please provide a valid User ID.")
    elif user_question:
        st.session_state["messages"].append({"role": "user", "content": user_question})

        response = faq_system.chat_function(user_question, user_id=user_id)

        st.session_state["messages"].append({"role": "assistant", "content": response})

    # Clear input field
    st.session_state["input_text"] = ""

# Display conversation history
st.title("E-commerce FAQ Assistant")
st.caption("Powered by Streamlit")
st.markdown("### Conversation")

for i, msg in enumerate(st.session_state["messages"]):
    message(msg["content"], is_user=(msg["role"] == "user"), key=f"msg_{i}")

# User ID input with callback
st.text_input(
    "Enter your User ID:",
    key="user_id_input",
    value=st.session_state["user_id"],
    placeholder="e.g., 12345",
    on_change=update_user_id
)

# User input field with callback
st.text_input(
    "Type your message here:",
    key="input_text",
    placeholder="Ask your question...",
    on_change=process_input
)
