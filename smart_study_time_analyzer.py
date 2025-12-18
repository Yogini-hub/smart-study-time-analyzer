days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
study_hours = []

print("Smart Study Time Analyzer\n")

for day in days:
    hours = float(input(f"Enter study hours for {day}: "))
    study_hours.append(hours)

total_hours = sum(study_hours)
average_hours = total_hours / 7

max_hours = max(study_hours)
best_day = days[study_hours.index(max_hours)]

print("\n--- Study Analysis ---")
print(f"Total study hours in a week: {total_hours}")
print(f"Average study hours per day: {average_hours:.2f}")
print(f"Most productive day: {best_day}")

if average_hours >= 6:
    print("Excellent! You have a strong study routine.")
elif average_hours >= 4:
    print("Good job! Try to be more consistent.")
else:
    print("You should improve your study consistency.")

