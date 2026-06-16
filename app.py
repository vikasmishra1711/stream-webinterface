import streamlit as st
st.set_page_config(
    page_title="ChatGPT UI",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Background */
.stApp {
    background-color: #343541;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #202123;
}

/* Title */
.main-title {
    text-align: center;
    color: white;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* Chat Container */
.chat-container {
    max-width: 900px;
    margin: auto;
}

/* User Message */
.user-msg {
    background-color: #444654;
    color: white;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    width: fit-content;
    max-width: 80%;
    margin-left: auto;
}

/* Assistant Message */
.bot-msg {
    background-color: #202123;
    color: white;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    width: fit-content;
    max-width: 80%;
}

/* Input Box */
.stChatInputContainer {
    background-color: #40414F;
}

/* Mobile Responsive */
@media (max-width: 768px) {

    .main-title {
        font-size: 24px;
    }

    .user-msg,
    .bot-msg {
        max-width: 95%;
        font-size: 14px;
    }
}

</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🤖 ChatGPT")
    st.markdown("---")
    st.button("➕ New Chat", use_container_width=True)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# Title
st.markdown(
    '<div class="main-title">ChatGPT Clone UI</div>',
    unsafe_allow_html=True
)

# Display Messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-msg">{msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="bot-msg">{msg["content"]}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# Chat Input
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Dummy Response
    response = f"You said: {prompt}"

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()