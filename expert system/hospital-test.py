categories = {
    "Emergency": "Hospital",
    "Specialized Treatment": "Hospital",
    "Routine Check-up": "Clinic",
    "General Consultation": "Clinic"
}

solutions = {
    "Hospital": {
        "High": "Visit the nearest hospital immediately for emergency care.",
        "Medium": "Book an appointment with a specialist at a hospital.",
        "Low": "Contact the hospital for general inquiries and information."
    },
    "Clinic": {
        "High": "Visit a clinic for immediate medical attention.",
        "Medium": "Schedule an appointment with a specialized clinic if required.",
        "Low": "Contact a nearby clinic for general consultations and routine check-ups."
    }
}

print("Welcome to the Hospital and Medical Facility Expert System!")
print("Please provide some information to recommend a facility and solution.")
print("--------------------------------------------------------------")

ticket_description = input("Enter the reason for your visit: ")
ticket_priority = input("Enter the priority level (Low, Medium, High): ")

category = "Clinic"
for keyword, cat in categories.items():
    if keyword in ticket_description.title():
        category = cat
        break

solution = solutions[category][ticket_priority.capitalize()]

print("--------------------------------------------------------------")
print("Based on your inputs, we recommend visiting a", category + ".")
print("Recommended solution:", solution)
print("Thank you for using the Hospital and Medical Facility Expert System!")
