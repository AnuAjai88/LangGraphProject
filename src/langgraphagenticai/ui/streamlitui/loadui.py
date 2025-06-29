import streamlit as st
import os
from datetime import date


from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config


class loadStreamlitUI:    #default configuration the info that's displayed in the dropbox tc. all hardcoded)
    def __init__(self):
        self.config = Config() #config
        self.user_controls = {}

    def initialize_session(self):
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            'review_feedback': "",
            "decision": None
        }

    def render_requirements(self):
        st.markdown("## 📃 Requirements submission")
        st.session_state.state["requirements"] = st.text_area(
            "Enter your requirements:",
             height=200,
             key = "req_input")

        if st.button("Submit requirements", key= "submit_req"):
            st.session_state.state["current_step"] = "generate_user_stories"
            st.session_state.IsSDLC = True


    def load_streamlit_ui(self):
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            #Get options from config
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_option()


            #LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                #Model selection
                model_options = self.config.get_groq_model_option()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                #API key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                #Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have refer : https://console.groq.com/api-keys")

            
            #Uase case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", usecase_options)

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            

        return self.user_controls