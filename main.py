# main.py
import streamlit as st
import datetime
import os
import requests
from dotenv import load_dotenv

st.set_page_config(
    page_title="RishtaGPT: DilSe 💖",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables from .env file
load_dotenv()

st.markdown("""
<style>
    .main {
        background-color: #FFF5F5;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    
    }
    .stButton>button:hover {
        background-color: black;
        transform: scale(1.05);
    }
    .stRadio>div {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stSelectbox>div {
        background-color: white;
        border-radius: 10px;
    }
    .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #FF4B4B;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .sidebar .sidebar-content {
        background-color: #FFF0F0;
    }
    .feature-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .result-box {
        background-color: #FFF0F0;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        border: 2px solid #FF4B4B;
    }
</style>
""", unsafe_allow_html=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_text(prompt):
    if not OPENROUTER_API_KEY:
        st.error("OpenRouter API key not found. Please check your .env file.")
        return "Error: API key not configured"
        
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://github.com/FatimaNazeer777/AI-Agents-first",
        "X-Title": "RishtaGPT"
    }
    
    json_data = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [
            {"role": "system", "content": "You are a fun and witty AI expert in desi rishtas."},
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=json_data)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.HTTPError as e:
        error_message = f"API Error: {str(e)}"
        if response.text:
            try:
                error_details = response.json()
                error_message += f"\nDetails: {error_details}"
            except:
                error_message += f"\nResponse: {response.text}"
        st.error(error_message)
        return "Error: Could not generate response"
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "Error: Could not generate response"

# Header
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='font-size: 3em; margin-bottom: 10px;'>💖 RishtaGPT: DilSe 💖</h1>
    <p style='font-size: 1.2em; color: #666;'>Tumhari qismet likhne aaye hain hum</p>
</div>
""", unsafe_allow_html=True)

# Sidebar 
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2 style='color: #FF4B4B;'>✨ Features ✨</h2>
    </div>
    """, unsafe_allow_html=True)
    
    pages = st.radio("Select Feature", [
        "🌸 Manifestation Generator",
        "🧕 Bio Beautifier",
        "🎭 Rishta Quiz",
        "🎬 Shaadi Drama Generator",
        "📸 Rishta DP Frame",
        "🎯 Pickup Lines",
        "🗓️ Shaadi Planner",
    ])

st.markdown("<div style='padding: 20px;'></div>", unsafe_allow_html=True)  
# 1. Manifestation Generator
if pages == "🌸 Manifestation Generator":
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2>🌸 Rishta Manifestation Generator</h2>
        <p>Create your perfect rishta manifestation with AI magic!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        nature = st.selectbox("Select rishta nature", ["Caring", "Confident", "Funny", "Namazi", "Mature", "Artistic"])
    with col4:
        style = st.selectbox("Select style", ["Poetry", "Duaa", "Shayari", "Romantic"])
    
    if st.button("✨ Generate Manifestation ✨", key="manifest"):
        with st.spinner("Manifesting your dream rishta..."):
            prompt = f"Write a {style} Urdu rishta manifestation dua for a {nature} girl with Pakistani cultural flavor. Make it poetic, emotional, and Instagram caption friendly."
            st.markdown("### 💫 Your Manifestation 💫")
            st.markdown(f"<div class='result-box'>{generate_text(prompt)}</div>", unsafe_allow_html=True)

# 2. Bio Beautifier
elif pages == "🧕 Bio Beautifier":
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2>🧕 Rishta Bio Beautifier</h2>
        <p>Transform your bio into a masterpiece!</p>
    </div>
    """, unsafe_allow_html=True)
    
    bio_input = st.text_area("Paste your current bio (in Urdu, Roman Urdu or English)", height=150)
    if st.button("✨ Beautify My Bio ✨", key="bio"):
        with st.spinner("Enhancing your bio with AI..."):
            prompt = f"Improve the following rishta bio in Urdu and English. Make it engaging, sincere, and reflect personality, hobbies, and values:\n\n{bio_input}"
            st.markdown("### ✨ Beautified Bio ✨")
            st.markdown(f"<div class='result-box'>{generate_text(prompt)}</div>", unsafe_allow_html=True)

# 3. Rishta Quiz
elif pages == "🎭 Rishta Quiz":
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2>🎭 Fun Rishta Personality Quiz</h2>
        <p>Discover your rishta personality type!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        q1 = st.radio("Your ideal rishta partner is:", ["Introvert", "Extrovert", "Balanced"])
        q2 = st.radio("What's most important to you?", ["Trust", "Humor", "Looks", "Religion"])
    with col4:
        q3 = st.radio("Pick a shaadi function:", ["Mehndi", "Baraat", "Valima"])
        q4 = st.radio("Your ideal date would be:", ["Coffee Shop", "Restaurant", "Park", "Home"])
    
    if st.button("✨ Show My Rishta Persona ✨", key="quiz"):
        with st.spinner("Analyzing your vibe..."):
            prompt = f"Based on these preferences: {q1}, {q2}, {q3}, {q4}, describe the user's rishta personality with humor and a desi twist. Suggest a nickname and ideal match type."
            st.markdown("### 💃 Your Rishta Persona")
            st.markdown(f"<div class='result-box'>{generate_text(prompt)}</div>", unsafe_allow_html=True)

# 4. Shaadi Drama Generator
elif pages == "🎬 Shaadi Drama Generator":
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2>🎬 Shaadi Drama Script Generator</h2>
        <p>Create your own desi drama scene!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        scene = st.selectbox("Choose a rishta drama scene", [
            "Saas-Bahu Argument",
            "Rishta Interview",
            "Dance Practice Gone Wrong",
            "Mehndi Night Drama",
            "Baraat Arrival Chaos"
        ])
    with col4:
        style = st.selectbox("Choose drama style", ["Comedy", "Romantic", "Dramatic", "Family Drama"])
    
    if st.button("✨ Generate Drama Script ✨", key="drama"):
        with st.spinner("Lights... Camera... Rishta!"):
            prompt = f"Write a funny short script for a Pakistani shaadi drama scene: {scene} in {style} style. Make it suitable for TikTok reels, include characters with dialogues and emotions."
            st.markdown("### 🎭 Your Drama Script")
            st.markdown(f"<div class='result-box'>{generate_text(prompt)}</div>", unsafe_allow_html=True)

# 5. Rishta DP Frame
elif pages == "📸 Rishta DP Frame":
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2>📸 Rishta DP Caption & Frame Suggestion</h2>
        <p>Get the perfect frame and caption for your rishta profile!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        vibe = st.selectbox("Pick your selfie vibe", ["Simple", "Glamorous", "Traditional", "Cute", "Professional"])
        occasion = st.selectbox("Select occasion", ["Casual", "Wedding", "Party", "Travel", "Family"])
    with col4:
        style = st.selectbox("Choose caption style", ["Poetic", "Funny", "Romantic", "Professional", "Desi"])
    
    if st.button("✨ Get Frame & Caption ✨", key="dp"):
        with st.spinner("Creating your perfect frame..."):
            prompt = f"Suggest a creative photo frame idea and 3 desi-style captions for a {vibe} {occasion} selfie. Style: {style}. Include both Urdu and English mix."
            st.markdown("### 🖼️ Your DP Style")
            st.markdown(f"<div class='result-box'>{generate_text(prompt)}</div>", unsafe_allow_html=True)

# 6. Pickup Lines
elif pages == "🎯 Pickup Lines":
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2>🎯 Rishta Pickup Line Generator</h2>
        <p>Get the perfect conversation starter!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        tone = st.selectbox("Select tone", ["Romantic", "Funny", "Flirty", "Respectful", "Poetic"])
        gender = st.radio("You are:", ["Boy", "Girl"])
    with col4:
        style = st.selectbox("Choose style", ["Modern", "Traditional", "Mix", "Poetic", "Fun"])
    
    if st.button("✨ Generate Pickup Line ✨", key="pickup"):
        with st.spinner("Cooking up a chat opener..."):
            prompt = f"Write a {tone} {style} Urdu + English mix pickup line for a {gender} to use on rishta apps. Keep it desi, respectful, and fun."
            st.markdown("### 💌 Your Line")
            st.markdown(f"<div class='result-box'>{generate_text(prompt)}</div>", unsafe_allow_html=True)

# 7. Shaadi Planner
elif pages == "🗓️ Shaadi Planner":
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2>🗓️ Shaadi Countdown & Checklist</h2>
        <p>Plan your perfect wedding!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        date = st.date_input("Select your shaadi date")
        budget = st.selectbox("Select budget range", ["Economy", "Standard", "Premium", "Luxury"])
    with col4:
        style = st.selectbox("Wedding style", ["Traditional", "Modern", "Mix", "Luxury", "Simple"])
        guest_count = st.number_input("Expected guest count", min_value=50, max_value=1000, step=50)
    
    if st.button("✨ Plan My Shaadi ✨", key="planner"):
        days_left = (date - datetime.date.today()).days
        with st.spinner("Creating your wedding plan..."):
            prompt = f"Create a detailed shaadi prep checklist for a {style} wedding with {budget} budget and {guest_count} guests. Wedding is {days_left} days away. Include mehndi, baraat, valima, shopping, salon, decor, and cultural elements."
            st.markdown(f"### ⏳ {days_left} Days Left! Here's Your Checklist")
            st.markdown(f"<div class='result-box'>{generate_text(prompt)}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; padding: 20px; margin-top: 50px;'>
    <p style='color: #666;'>Made with 💖 for desi rishtas by Fatima Nazeer</p>
</div>
""", unsafe_allow_html=True)
