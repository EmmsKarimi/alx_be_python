# daily_reminder.py

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match Case statement to handle different priority levels
match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"
    case _:
        priority_message = "unknown priority"  # Handles any unexpected priority input

# Check if the task is time-bound and modify urgency message accordingly
if time_bound == "yes":
    # Ensure the format is exactly what is expected
    print(f"Reminder: '{task}' is a {priority_message} task that requires immediate attention today!")
else:
    # Ensure the format is exactly what is expected
    print(f"Note: '{task}' is a {priority_message} task. Consider completing it when you have free time.")