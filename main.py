from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai

import os

# Load environment variables from .env fil

# Get the Gemini API key from the environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate text using Gemini
def generate_ethical_ai_text(prompt):
    """Generates text related to ethical AI decision-making using Gemini."""
    model = genai.GenerativeModel('gemini-pro') # Use 'gemini-pro'
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating text: {e}"  # Handle potential errors

# Streamlit app
def main():
    st.title("Ethical AI Decision-Making Text Generator")

    st.write("""
    This app uses the Gemini API to generate text on the topic of ethical AI decision-making.
    Enter a prompt related to the topic below, and the app will generate text based on your prompt.
    """)

    user_prompt = st.text_area("Enter your prompt:", "Explain the importance of fairness in AI decision-making.")

    if st.button("Generate Text"):
        with st.spinner("Generating..."): # Show a spinner while generating
            generated_text = generate_ethical_ai_text(user_prompt)
        st.subheader("Generated Text:")
        st.write(generated_text)

if __name__ == "__main__":
    main()