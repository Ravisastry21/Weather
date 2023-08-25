import streamlit as st
import google.generativeai as palm
palm.configure(api_key="AIzaSyBKYstTc4ORS9AqSvQWJGJ-eFZnrp6OwbE")

defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

intro_messages = [
    "hi",
    "Hello! How can I help you today?",
    "what will you do or predict?",
    "Want to know the weather forecast?",
    "Curious about the weather? Ask me!",
    "Looking for weather information? Feel free to ask.",
]

messages = intro_messages.copy()

st.title("Weather Chatbot")

with st.container():
    user_input = st.text_input("You:", "")

if user_input.lower() == "exit":
    st.text("Chatbot: Goodbye!")
else:
    messages.append(user_input)

    weather_keywords = ["weather", "forecast", "temperature", "rain", "sun", "cloud", "wind"]
    is_weather_related = any(keyword in user_input.lower() for keyword in weather_keywords)

    if is_weather_related:
        response = palm.chat(
            **defaults,
            context=user_input,
            examples=[],
            messages=messages
        )
        bot_response = response.last
    else:
        bot_response = "My primary function is to provide weather information. Please ask me a weather-related question."

    st.write("Chatbot: " + bot_response)

    messages.append("User: " + user_input)
    messages.append("Chatbot: " + bot_response)
