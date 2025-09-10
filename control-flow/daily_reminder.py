task = input("What is your task?: ")
priority = input("How urgent is your task? (high, medium, low): ")
time_bound = input(f"Is {task} time-bound? (yes, no): ")

match priority:
    case "high":
        reminder = f"{task} is a high priority task "
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task}  is a low priority task"
    case _:
        reminder = f"{task} has an unknown priority level"

if time_bound == "yes":
    reminder += "that requires immediate attention today.")
else:
    reminder += ". Consider completing it when you have free time.")
print(f"\n Reminder: {reminder}")
    