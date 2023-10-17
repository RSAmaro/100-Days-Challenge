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

#Write your code below this line 👇
print("=================")
step1 = input(
    "You're in a dense forest. You come to a fork in the path. Do you want to go 'left' or 'right'? \n"
)

if step1 == "left":
    step2 = input(
        "As you follow the path, you stumble upon a hidden waterfall. Do you 'wait' for a guide to show up or 'climb' down the rocks to explore on your own? \n"
    )
    
    if step2 == "wait":
        step3 = input(
            "The guide arrives and leads you to a mysterious cave entrance. You enter the cave, and inside, you see three tunnels. One is illuminated with a soft 'red' glow, the second one has a 'yellow' light, and the third is 'blue' and shrouded in darkness. Which tunnel do you choose? \n"
        )

        if step3 == "red":
            print("You've awakened a fiery dragon! Game over!")
        elif step3 == "yellow":
            print("You've fallen into a pit of quicksand. Game over!")
        elif step3 == "blue":
            print("Congratulations! You've discovered a hidden treasure chest. You win the game!")
        else:
            print("Invalid choice. Game over!")

    elif step2 == "climb":
        print("You slipped and got injured while climbing down the rocks. Game over!")

    else:
        print("Invalid choice. Game over!")

else:
    step4 = input("You take the right path and end up in a vast desert. You have no water and soon succumb to the scorching heat. Game over!")



