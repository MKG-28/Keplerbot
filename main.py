
import streamlit as st
from chatbot import AdmissionChatbot
import time

# First command: Set page config
st.set_page_config(page_title="🌟 KeplerBot Genie - Your Smart Study Companion", layout="centered")

# Custom CSS - Academic theme (dark mode) with animations
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #1565C0 0%, #26A69A 50%, #E8F5E8 100%);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        min-height: 100vh;
    }
    .stApp {
        background: linear-gradient(135deg, #1565C0 0%, #26A69A 50%, #E8F5E8 100%);
        min-height: 100vh;
    }
    .user-bubble {
        background: linear-gradient(135deg, #1976D2, #42A5F5, #64B5F6);
        color: white;
        border-radius: 20px;
        padding: 15px 20px;
        margin: 10px 0;
        max-width: 75%;
        align-self: flex-end;
        text-align: right;
        animation: slideInRight 0.5s ease-out;
        box-shadow: 0 6px 20px rgba(25, 118, 210, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.3);
        font-weight: 500;
        backdrop-filter: blur(10px);
    }
    .bot-bubble {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(240, 248, 255, 0.95));
        color: #0D47A1;
        border-radius: 20px;
        padding: 15px 20px;
        margin: 10px 0;
        max-width: 75%;
        align-self: flex-start;
        text-align: left;
        animation: slideInLeft 0.5s ease-out;
        box-shadow: 0 6px 20px rgba(13, 71, 161, 0.2);
        border: 2px solid rgba(38, 166, 154, 0.4);
        font-weight: 500;
        backdrop-filter: blur(10px);
    }
    
    /* Welcome Animation */
    .welcome-container {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #0D47A1 0%, #1976D2 50%, #26A69A 100%);
        border-radius: 20px;
        margin: 20px 0;
        animation: welcomeFadeIn 2s ease-in-out;
        box-shadow: 0 12px 32px rgba(13, 71, 161, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .welcome-title {
        font-size: 2.5em;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
        animation: bounceIn 1.5s ease-out;
    }
    
    .welcome-subtitle {
        font-size: 1.2em;
        color: #E8E8E8;
        margin-bottom: 20px;
        animation: fadeInUp 2s ease-out;
    }
    
    .welcome-feature {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        padding: 8px 15px;
        border-radius: 20px;
        margin: 5px;
        animation: pulse 2s infinite;
    }
    
    /* Typing Animation */
    .typing-indicator {
        display: flex;
        align-items: center;
        padding: 15px 20px;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 248, 255, 0.9));
        color: #1565C0;
        border-radius: 20px;
        margin: 10px 0;
        max-width: 75%;
        box-shadow: 0 6px 20px rgba(21, 101, 192, 0.25);
        border: 2px solid rgba(38, 166, 154, 0.5);
        backdrop-filter: blur(10px);
        font-weight: 500;
    }
    
    .typing-dot {
        height: 8px;
        width: 8px;
        background-color: #1565C0;
        border-radius: 50%;
        display: inline-block;
        margin: 0 2px;
        animation: typing 1.4s infinite;
    }
    
    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    /* Keyframe Animations */
    @keyframes welcomeFadeIn {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes bounceIn {
        0% {
            opacity: 0;
            transform: scale(0.3);
        }
        50% {
            opacity: 1;
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
        100% {
            transform: scale(1);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes typing {
        0%, 60%, 100% {
            transform: translateY(0);
            opacity: 0.4;
        }
        30% {
            transform: translateY(-10px);
            opacity: 1;
        }
    }
    
    /* Enhanced Chat Input Styling */
    .stChatInput > div > div > div {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 248, 255, 0.9)) !important;
        border: 3px solid rgba(25, 118, 210, 0.6) !important;
        border-radius: 25px !important;
        box-shadow: 0 8px 25px rgba(13, 71, 161, 0.3) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stChatInput > div > div > div > div > div > textarea {
        background: transparent !important;
        color: #0D47A1 !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        border: none !important;
        padding: 15px 20px !important;
    }
    
    .stChatInput > div > div > div > div > div > textarea::placeholder {
        color: #26A69A !important;
        opacity: 0.8 !important;
        font-style: italic !important;
    }
    
    .stChatInput > div > div > div > div > button {
        background: linear-gradient(135deg, #1976D2, #26A69A) !important;
        border: none !important;
        border-radius: 50% !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(25, 118, 210, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stChatInput > div > div > div > div > button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 6px 20px rgba(25, 118, 210, 0.6) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize chatbot once
if "bot" not in st.session_state:
    try:
        st.session_state.bot = AdmissionChatbot("data/Chatbot Questions & Answers.xlsx")
        st.session_state.messages = [
            {"role": "assistant", "content": st.session_state.bot.greeting_response}
        ]
        st.session_state.show_welcome = True
    except Exception as e:
        st.error("❌ Failed to load knowledge base. Make sure the Excel file is in the correct location.")
        st.stop()

# Show welcome animation on first load
if st.session_state.get("show_welcome", False):
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-title">🌟 Meet KeplerBot Genie!</div>
        <div class="welcome-subtitle">Your Magical Study Companion & Admission Wizard</div>
        <div>
            <span class="welcome-feature">🧙‍♂️ 203 Magic Answers</span>
            <span class="welcome-feature">🔮 Crystal Clear Guidance</span>
            <span class="welcome-feature">✨ Instant Wisdom</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Auto-hide welcome after 3 seconds
    time.sleep(3)
    st.session_state.show_welcome = False
    st.rerun()

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-bubble">🧑‍🎓 You: {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">🧙‍♂️ KeplerBot Genie: {message["content"]}</div>', unsafe_allow_html=True)

# User input
if prompt := st.chat_input("Ask the Genie anything about Kepler... ✨"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble">🧑‍🎓 You: {prompt}</div>', unsafe_allow_html=True)

    # Show typing animation
    typing_placeholder = st.empty()
    typing_placeholder.markdown("""
    <div class="typing-indicator">
        🔮 KeplerBot Genie is consulting the crystal ball
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
    </div>
    """, unsafe_allow_html=True)
    
    # Simulate thinking time with typing animation
    time.sleep(2)
    typing_placeholder.empty()

    # Get bot response
    response = st.session_state.bot.get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f'<div class="bot-bubble">🧙‍♂️ Magical Answer: {response}</div>', unsafe_allow_html=True)