print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
game = True
print("You walk on the docks and you see the lights of a ship on your side.\nYou find yourself on board, left is the captain cabin, right is the cellar")
answer = input("Where do you chose to go? (left / right)").lower()
if answer != 'left':
    print("You fall on the cellar due to some inconsistent wood flooring, you hit your head and died")
    game = False
if game:
    print("You entered the captain cabin, no one is on board but you. you get to her desk and there you find the treasure map.\n You make a photo with your phone when you realize that the ship is sinking")
    answer = input("What do you choose, swim to the dock or wait there? (swim / wait)").lower()
    if answer != 'wait':
        game = False
        print("You get attacked by a trout")
    if game:
        print("After waiting on board, the ship gets captured by a UFO.\n You find yourself in a extremly lighted room, and you see two doors.\nA Red, a Yellow and a Blue one")
        answer = input("Which door do you choose? (red / blue)").lower()
        if answer != 'yellow':
            game = False
        if answer == 'red':
            print("you enter the room and when you close it and turn yourself you find yourself in a fire. You try to open the door again but it is locked")
        elif answer == 'blue':
            print("you enter the blue door. Everything is dark around you. You hear some metal sound. you're going to be the meal of a beast")
if game:
    print("Congratulations!, you win! you found the biggest treasure, remaining alive")
else:
    print("Game Over")
