categories = {
    "Long-term Investment": "Buy and Hold Strategy",
    "Short-term Trading": "Technical Analysis",
    "Day Trading": "Intraday Trading"
}

solutions = {
    "Buy and Hold Strategy": {
        "High": "Research and identify fundamentally strong companies for long-term investment.",
        "Medium": "Diversify your portfolio with a mix of stocks from different sectors.",
        "Low": "Monitor the market trends and review your portfolio periodically."
    },
    "Technical Analysis": {
        "High": "Learn and apply technical indicators and chart patterns for entry and exit points.",
        "Medium": "Set stop-loss orders and profit targets to manage risk and capture gains.",
        "Low": "Stay updated with market news and events that impact stock prices."
    },
    "Intraday Trading": {
        "High": "Focus on highly liquid stocks and use technical indicators for short-term trades.",
        "Medium": "Set strict entry and exit rules and adhere to them to minimize losses.",
        "Low": "Practice risk management techniques and keep emotions in check while trading."
    }
}

print("Welcome to the Stock Market Trading Expert System!")
print("Please provide some information to recommend a trading strategy and solution.")
print("--------------------------------------------------------------")

trade_description = input("Enter your trading objective or style: ")
trade_priority = input("Enter the priority level (Low, Medium, High): ")

category = "Buy and Hold Strategy"
for keyword, cat in categories.items():
    if keyword in trade_description.title():
        category = cat
        break

solution = solutions[category][trade_priority.capitalize()]

print("--------------------------------------------------------------")
print("Based on your inputs, we recommend the", category + ".")
print("Recommended solution:", solution)
print("Thank you for using the Stock Market Trading Expert System!")
