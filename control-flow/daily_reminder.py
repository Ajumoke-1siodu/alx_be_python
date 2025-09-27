task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process based on priority
match priority:
        case "high":
                reminder = f"Reminder: '{task}' is a HIGH priority task."
                    case "medium":
                            reminder = f"Reminder: '{task}' is a medium priority task."
                                case "low":
                                        reminder = f"Reminder: '{task}' is a low priority task."
                                            case _:
                                                    reminder = f"Reminder: '{task}' has an unknown priority."

                                                    # Modify reminder if task is time-sensitive
                                                    if time_bound == "yes":
                                                        reminder += " This task requires immediate attention today!"

                                                        # Print the customized reminder
                                                        print(reminder)


