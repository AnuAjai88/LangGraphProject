import streamlit as st
import json

from src.langgraphagenticai.ui.steeamlitui.loadui import loadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.Graph_builder import GraphBuilder

#MAIN FUNCTION START
def load_langgraph_agenticai_app():
    """
    loads and runs thLanGraph Agentic AI application with Streamlit UI.
    This function initialises the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while implementing exception handling for robustness.
    """

    #Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input from the UI")
        return

    #Text input for user mssage
    if st.session_state.state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            #configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialised ")
                return

            #Initialize and set up the graph based on use case
            usecase = user_input.get('selected_usecase')

            if not usecase:
                st.error("Error: No use case selected.")
                return

            ###Grpah Builder
            graph_builder = GraphBuilder(model)
            
        except Exception as e:
            raise ValueError(f"Error occurred with exception: {e}")
  