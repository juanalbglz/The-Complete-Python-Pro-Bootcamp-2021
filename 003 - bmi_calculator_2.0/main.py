# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#TODO 1 BMI = height / weight^2

#TODO 1.3 Remember PEMDAS (Parenthesis (P)/ Exponents (E)/ Multiplication or Division (MD)/ Addition or Substraction (AS)
bmi = float("{:.1f}".format(weight / (height ** 2)))


if bmi < 18.5:
    message = "you are underweight"
elif bmi < 25:
    message = "you have a normal weight"
elif bmi <30:
    message = "you are slightly overweight"
elif bmi < 35:
    message = "you are obese"
else:
    message = "you are clinically obese"

print(f"Your BMI is {bmi} kg/m2, {message}.")