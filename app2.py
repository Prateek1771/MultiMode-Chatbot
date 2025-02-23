# Voice activated chatbot - voice activated + text based + image generation
# V1.1

import os
from dotenv import load_dotenv
import ollama
import streamlit as st
import speech_recognition as sr
import pyttsx3
import os
from groq import Groq
import time

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Streamlit App Title
st.title("Voice-Activated Chatbot")

# Mode Selection: Chat Mode or Voice Mode
mode = st.radio("Select Mode", ("Chat Mode", "Voice Mode"))

# Chat Mode
if mode == "Chat Mode":
    query = st.chat_input("Enter your question")
    if query:
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            client = Groq(
                api_key=API_KEY,
            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "Always respond with concise reponses. keep it crisp and clear to the point."
                    },
                    {
                        "role": "user",
                        "content": query,
                    }
                ],
                model="llama-3.3-70b-versatile",
                stream=False,
            )
            def stream_response():
                for content in chat_completion.choices[0].message.content.split(" "):
                    yield content + " "
                    time.sleep(0.02)
            st.write_stream(stream_response(),)

        #     response = ollama.generate(model="llama3.2", prompt=query)
        #     st.write(response["response"])
            
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

                # Generate response from Ollama
                response = ollama.generate(model="llama3.2", prompt=text)
                bot_response = response["response"]

                # Display response
                with st.chat_message("assistant"):
                    st.write(bot_response)

                # Convert response to speech
                engine.say(bot_response)
                engine.runAndWait()

            except sr.UnknownValueError:
                st.write("Sorry, I couldn't understand.")
            except sr.RequestError:
                st.write("Could not request results, check your internet connection.")