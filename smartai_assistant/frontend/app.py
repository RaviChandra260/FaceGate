import streamlit as st

st.set_page_config(
    page_title="Smart AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ----------------- SIDEBAR -----------------
st.sidebar.title("🤖 Smart AI Assistant")
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Face Registration", "Face Login", "Voice Assistant", "Translator"]
)

# ----------------- HEADER -----------------
st.markdown(
    "<h1 style='text-align:center;'>Smart AI Assistant System</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# ----------------- PAGES -----------------
if menu == "Home":
    st.subheader("Welcome")
    st.write("""
    This application integrates:
    - Face Recognition for secure access
    - Voice Assistant for hands-free control
    - Speech Translation for multilingual interaction
    """)
    st.success("System Ready")

elif menu == "Face Registration":
    st.subheader("📸 Face Registration")
    st.info("Register a new user face")
    st.button("Capture Face")

elif menu == "Face Login":
    st.subheader("🔐 Face Recognition Login")
    st.warning("Please face the camera")
    st.button("Start Recognition")

elif menu == "Voice Assistant":
    st.subheader("🎙 Voice Assistant")
    st.write("Speak commands to control the system")
    st.button("Start Listening")

elif menu == "Translator":
    st.subheader("🌍 Voice Translator")
    st.selectbox("Select Target Language", ["Tamil", "Hindi", "French"])
    st.button("Start Translation")

# ----------------- FOOTER -----------------
st.markdown("---")
st.caption("Final Year Project | AI-Based Smart Assistant")
