from configparser import ConfigParser

class Config:
    def __init__(self, config_file: str = "./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ") #this is getting the default LM option, and also seperates it if a list seperated by comma is specified
    
    def get_usecase_option(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_option(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")