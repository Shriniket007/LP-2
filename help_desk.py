categories = {
    "Computer": "Hardware",
    "Printer": "Hardware",
    "Scanner": "Hardware",
    "Keyboard": "Hardware",
    "Application": "Software",
    "Operating system": "Software",
    "Connectivity": "Network",
    "Internet": "Network",
    "Server": "Network"
}

solutions = {
    "Hardware": {
            "High": "Replace faulty hardware component", 
            "Medium": "Check cables and connections",
            "Low": "Check hardware settings"
        },
    "Software":
        {
            "High": "Reinstall the software", 
            "Medium": "Restart computer or application", 
            "Low": "Check software settings"
         },
    "Network": {
            "High": "Reset network devices",
            "Medium": "Check network cables and connections",
            "Low": "Check network settings"
        },
    "Other": {
            "High": "Refer to senior support staff", 
            "Medium": "Refer to senior support staff",
            "Low": "Refer to senior support staff"
        }
}

ticket_description = input("Enter the problem description: ")
ticket_priority = input("Enter the problem priority (Low, Medium, High): ")

category = "Other"
for keyword, cat in categories.items():
    if keyword in ticket_description.title():
        category = cat
        break
solution = solutions[category][ticket_priority.capitalize()]

print("Recommended solution:", solution)
