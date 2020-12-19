age = int(input("What is your age?\n"))
max_age = 90
remaining_age = max_age - age
remaining_months = 12 * remaining_age
remaining_weeks = 52 * remaining_age
remaining_days = 365 * remaining_age
print(f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left.")