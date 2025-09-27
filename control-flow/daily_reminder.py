# daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case based on priority
match priority:
    case "high":
        reminder = f"Reminder: {task} (Priority: high)"
    case "medium":
        reminder = f"Reminder: {task} (Priority: medium)"
    case "low":
        reminder = f"Reminder: {task} (Priority: low)"
    case _:
        reminder = f"Reminder: {task} (Priority: unspecified)"

# If task is time-bound, modify reminder
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the final customized reminder
print(reminder)

