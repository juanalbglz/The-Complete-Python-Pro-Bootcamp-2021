# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
TRUE = "TRUE"
LOVE = "LOVE"
score_for_true = 0
score_for_love = 0
names = (name1 + name2).lower()
print(names)
for c in names:
    if c in TRUE.lower():
        score_for_true += 1
    if c in LOVE.lower():
        score_for_love +=1
love_score = int(str(score_for_true) + str(score_for_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and menthos.")
elif love_score > 39 and love_score < 51:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")