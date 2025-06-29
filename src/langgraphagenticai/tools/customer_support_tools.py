# Customer support tools for LangGraph Agentic AI

# Mock customer database
customers_database = {
    "customers": [
        {"id": 1, "name": "John Doe", "email": "john@example.com", "status": "active"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "status": "active"},
        {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "status": "inactive"}
    ]
}

# Data protection checks
data_protection_checks = {
    "gdpr_compliant": True,
    "data_retention_days": 30,
    "encryption_enabled": True,
    "access_logs": True
}

def get_customer_info(customer_id):
    """Get customer information by ID"""
    for customer in customers_database["customers"]:
        if customer["id"] == customer_id:
            return customer
    return None

def check_data_protection():
    """Check data protection compliance"""
    return data_protection_checks 