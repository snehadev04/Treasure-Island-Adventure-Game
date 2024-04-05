print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("welcome to Treasure Island.")
print("your mission is to find the teasure.")
choice_1 = input('you are at a cross road, where do you wanna go? type "Right"or "Left".').lower()
if choice_1 == "left":
  choice_2 = input("You have reached the sea shore, you see a island in the middle of the sea. type 'Swim' to swim across the sea or 'Wait' to wait for the boat ").lower()
  if choice_2 == "wait":
    choice_3 = input("You safely reached the island. now there are 3 doors ahead of you Blue, Red, Yellow ").lower()
    if choice_3 == "yellow":
      print("Hurry!! you found the treasure.")
    elif choice_3 == "red":
       print("The door lead to lava pond. you are dead. Game over!!")
    elif choice_3 == "blue":
      print("You fell into quicksand. Game over!!")
    else:
      print("That door doesn\'t exist. Game over!!")
  else:
    print("you tried swimming across the sea and a shark attacked. you are dead. Game over!!")
else:
  print("you fell into a hole. Game Over!!")