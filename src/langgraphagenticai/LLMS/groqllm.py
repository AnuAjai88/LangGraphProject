from langchain_groq import ChatGroq
from pydantic import SecretStr
import os
import streamlit as st

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            
            # Validate API key
            if not groq_api_key or groq_api_key.strip() == '':
                if not os.environ.get("GROQ_API_KEY"):
                    st.error("Please enter the Groq API key")
                    raise ValueError("Groq API key is required")
                groq_api_key = os.environ["GROQ_API_KEY"]

            llm = ChatGroq(api_key=SecretStr(groq_api_key), model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error occurred with exception: {e}")
        return llm
        