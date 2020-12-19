# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#TODO 1 BMI = height / weight^2
#TODO 1.2 change type to allow mathematical operations
height = float(height)
weight = float(weight)
#TODO 1.3 Remember PEMDAS (Parenthesis (P)/ Exponents (E)/ Multiplication or Division (MD)/ Addition or Substraction (AS)
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi} kg/m2")
