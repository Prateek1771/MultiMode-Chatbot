# Main file 
# V2.0

import os
from dotenv import load_dotenv
import streamlit as st
import speech_recognition as sr
import pyttsx3
import time
import threading
from groq import Groq

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speech speed
engine.setProperty("volume", 1.0)  # Set volume to max

# Streamlit App Title
st.title("MultiMode chatbot")

# Mode Selection
mode = st.radio("Select Mode", ("Chat Mode", "Voice Mode", "Build Mode"))

# Function to generate response using Groq API
def get_groq_response(prompt, system_message):
    client = Groq(api_key=API_KEY)
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content

# Function to speak in a separate thread
def speak_text(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    
    # Start speaking in a new thread
    speech_thread = threading.Thread(target=run)
    speech_thread.start()

# Chat Mode
if mode == "Chat Mode":
    query = st.chat_input("Enter your question")
    if query:
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            response = get_groq_response(
                query, "Always respond with concise and clear answers. Keep it natural, conversational, and friendly."
            )
            st.write(response)

# Voice Mode
elif mode == "Voice Mode":
    st.write("Click the button and speak...")

    if st.button("Start Listening"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                st.write(f"**You said:** {text}")

                # Get response from Groq API
                bot_response = get_groq_response(
                    text, "Always respond in short and clear sentences. Keep responses natural."
                )

                # Display response
                with st.chat_message("assistant"):
                    st.write(bot_response)

                # Speak response
                speak_text(bot_response)

            except sr.UnknownValueError:
                st.write("Sorry, I couldn't understand.")
            except sr.RequestError:
                st.write("Could not request results, check your internet connection.")

# Build Mode
elif mode == "Build Mode":
    st.write("Enter a project idea, and I'll generate the code and step-by-step instructions.")

    project_idea = st.text_area("Describe your project idea")
    if st.button("Generate Code & Steps"):
        if project_idea:
            with st.chat_message("user"):
                st.write(project_idea)
            with st.chat_message("assistant"):
                response = get_groq_response(
                    project_idea,
                    "Generate a step-by-step guide to building this project, including technologies to use and code snippets where necessary."
                )
                st.write(response)
