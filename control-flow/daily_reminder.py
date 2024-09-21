task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time_bounded(yes/no): ")
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task ", end="")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task ", end="")
    case "low":
        print(f"Note: '{task}' is a low priority task ", end="")
if time_bound.lower() == "yes":
    print("that requires immediate action today!")
else:
    print(". Consider completing it when you have free time.")
