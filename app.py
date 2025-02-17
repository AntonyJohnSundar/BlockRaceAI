import streamlit as st
import time
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="AI-Powered Racing", layout="wide")

# Inject custom CSS for neon dark theme styling
st.markdown("""
    <style>
    /* Overall page style */
    body {
        background-color: #000;
        color: #fff;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .neon-text {
        color: #39ff14;
        text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 20px #39ff14;
    }
    .cta-button {
        background-color: #39ff14;
        color: #000;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        border: none;
        box-shadow: 0 0 5px #39ff14;
    }
    .cta-button:hover {
        background-color: #2ecc71;
        cursor: pointer;
    }
    .card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px;
    }
    .roadmap-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .contract-box {
        border: 2px dashed #39ff14;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# -------------------------------
# 1. Hero Section
# -------------------------------
st.markdown("<h1 class='neon-text' style='text-align: center;'>AI-Powered Racing</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Race. Earn. Own the Track.</h3>", unsafe_allow_html=True)

# Countdown Timer (Demo: 10-second countdown)
st.markdown("<h2 style='text-align: center; color: #39ff14;'>Countdown Timer (Demo)</h2>", unsafe_allow_html=True)
countdown_placeholder = st.empty()
target_time = datetime.now() + timedelta(seconds=10)  # 10-second demo countdown

# Loop to update countdown timer (for demo purposes)
for _ in range(11):
    now = datetime.now()
    if now >= target_time:
        countdown_text = "00:00:00"
    else:
        diff = target_time - now
        minutes, seconds = divmod(diff.seconds, 60)
        countdown_text = f"{minutes:02d}:{seconds:02d}"
    countdown_placeholder.markdown(f"<h2 style='text-align: center; color: #39ff14;'>Countdown: {countdown_text}</h2>", unsafe_allow_html=True)
    time.sleep(1)

# Hero CTA Button
if st.button("Join Now", key="hero-cta", help="Click to join the racing game"):
    st.success("CTA clicked! (This is a placeholder action)")

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# 2. Features Section (5 Cards)
# -------------------------------
st.markdown("<h2 class='neon-text' style='text-align: center;'>Features</h2>", unsafe_allow_html=True)
feature_titles = [
    "Game Overview",
    "Booster Top-ups",
    "Garage Customization",
    "Prize Distribution",
    "Crypto Integration"
]
feature_descriptions = [
    "Experience high-speed AI-powered racing.",
    "Enhance your vehicle with dynamic boosters.",
    "Customize your NFT-based vehicles.",
    "Win crypto rewards and more.",
    "Trade and manage tokens seamlessly."
]

cols = st.columns(5)
for idx, col in enumerate(cols):
    with col:
        st.markdown(f"""
            <div class="card">
                <h3 class="neon-text">{feature_titles[idx]}</h3>
                <p>{feature_descriptions[idx]}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# 3. Roadmap Section (5 Milestone Cards)
# -------------------------------
st.markdown("<h2 class='neon-text' style='text-align: center;'>Project Roadmap</h2>", unsafe_allow_html=True)
roadmap = [
    ("Concept & Design", "Initial concept and game design."),
    ("Blockchain Integration", "Set up crypto and smart contracts."),
    ("AI Racing Mechanics", "Develop AI-driven race dynamics."),
    ("Beta Launch", "Open beta testing with the community."),
    ("Full Game Release", "Global launch of the game.")
]

for milestone in roadmap:
    st.markdown(f"""
        <div class="roadmap-card">
            <h4 class="neon-text">{milestone[0]}</h4>
            <p>{milestone[1]}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# 4. Contract Address Placeholder
# -------------------------------
st.markdown("<h2 class='neon-text' style='text-align: center;'>Token Contract</h2>", unsafe_allow_html=True)
st.markdown("<div class='contract-box'>Contract Address: <em>Coming Soon</em></div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# 5. Final Call-to-Action Section
# -------------------------------
st.markdown("""
<div style='text-align: center;'>
    <h2 class='neon-text'>Ready to Race?</h2>
</div>
""", unsafe_allow_html=True)
if st.button("Buy Token", key="final-cta", help="Click to purchase tokens"):
    st.info("Token purchase clicked! (Placeholder action)")

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# 6. Footer Section
# -------------------------------
st.markdown("""
<div style='text-align: center;'>
    <p>Follow us on 
        <a style='color: #39ff14;' href='https://discord.com' target='_blank'>Discord</a>, 
        <a style='color: #39ff14;' href='https://twitter.com' target='_blank'>Twitter</a>
    </p>
    <p>&copy; 2025 AI-Powered Racing. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
