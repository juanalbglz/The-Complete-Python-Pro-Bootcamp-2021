#TODO 1 If the bill was $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6
#TODO 2 Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Wellcome to the tip calculator.")
bill_amount = float(input("Total bill amount: "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
splitted_people = int(input("How many people to split the bill?\n"))
splitted_amount = (bill_amount * ((100 + tip_percentage) / 100)) / splitted_people
print(f"Each person should pay ${'{:.2f}'.format(splitted_amount)}")
print(f"${'{:.2f}'.format(splitted_amount)} x {splitted_people} = ${'{:.2f}'.format(splitted_amount*splitted_people)}")
print(f"{tip_percentage}% tip of ${'{:.2f}'.format(bill_amount)} is {(bill_amount * (tip_percentage/ 100))}")
print(f"The solution is {(splitted_amount*splitted_people) >= (bill_amount * ((100 + tip_percentage) / 100))}")