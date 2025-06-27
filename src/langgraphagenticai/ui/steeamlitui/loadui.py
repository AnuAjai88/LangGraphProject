import streamlit as st
import os
from datetime import date


from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config


class loadStreamlitUI:    #default configuration the info that's displayed in the dropbox tc. all hardcoded)
    def __init__(self):
        self.config = Config() #config
        self.user_controls = {}
