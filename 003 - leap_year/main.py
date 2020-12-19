# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#TODO 1 Leap yeas:
# every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400
leap_year = False
if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True
if leap_year:
    leap_year_text = "leap year"
else:
    leap_year_text = "not leap year"

print(f"{year} is {leap_year_text}")
