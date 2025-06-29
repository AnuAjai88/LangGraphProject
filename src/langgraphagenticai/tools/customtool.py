# Custom tools for LangGraph Agentic AI

class APPOINTMENTS:
    """Custom tool for handling appointments"""
    
    def __init__(self):
        self.name = "appointments"
        self.description = "Tool for managing appointments"
    
    def schedule_appointment(self, date, time, description):
        """Schedule a new appointment"""
        return f"Appointment scheduled for {date} at {time}: {description}"
    
    def get_appointments(self):
        """Get all appointments"""
        return "No appointments found" 