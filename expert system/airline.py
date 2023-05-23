categories = {
    "Passenger Flights": "Airline Schedule",
    "Cargo Flights": "Cargo Schedule"
}

solutions = {
    "Airline Schedule": {
        "High": "Analyze passenger demand and schedule flights accordingly.",
        "Medium": "Optimize flight routes and frequencies based on historical data.",
        "Low": "Monitor and adjust flight schedules to accommodate changes in demand."
    },
    "Cargo Schedule": {
        "High": "Ensure efficient cargo handling and loading procedures for timely delivery.",
        "Medium": "Optimize cargo routing and prioritize high-value shipments.",
        "Low": "Monitor cargo demand and adjust schedules to meet customer requirements."
    }
}

print("Welcome to the Airline and Cargo Scheduling Expert System!")
print("Please provide some information to recommend a scheduling approach and solution.")
print("--------------------------------------------------------------")

schedule_description = input("Enter the type of schedule required (Passenger Flights, Cargo Flights): ")
schedule_priority = input("Enter the priority level (Low, Medium, High): ")

category = "Airline Schedule"
for keyword, cat in categories.items():
    if keyword in schedule_description.title():
        category = cat
        break

solution = solutions[category][schedule_priority.capitalize()]

print("--------------------------------------------------------------")
print("Based on your inputs, we recommend the", category + ".")
print("Recommended solution:", solution)
print("Thank you for using the Airline and Cargo Scheduling Expert System!")
