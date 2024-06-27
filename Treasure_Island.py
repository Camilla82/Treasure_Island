```python
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
print("You are at a crossroads. Do you want to go left or right?")

choice1 = input("Type 'left' or 'right': ") 
choice1 = choice1.lower()
if choice1 == "left":
          print("You fell into a hole. Game Over.")
if choice1 == "right":
                  print("You jump into a river.")
print("You follow the river to a clear. Do you want to swim to the bank or to wait in the water?")
choice2 = input("Type 'swim' or 'wait': ") 
choice2 = choice1.lower()
if choice2 == "swim":
          print("Game over. You fell into a hole.")
if choice2 == "wait":
                  print("You get attacked by a ferocious trout. Game Over")

print("You find a house. The house has two doors, one red, one blue, and one yellow. Which door do you want to open?")
choice3 = input("Type 'red' or 'blue' or 'yellow': ") 
choice3 = choice3.lower()
if choice3 == "red":
          print("Burned by fire. Game Over.")
elif choice3 == "blue":
                  print("Eaten by beasts. Game Over")
elif choice3 == "yellow":
          print("You Win!")
else:
          print("Game Over")

```
