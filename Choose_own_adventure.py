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



#Write your code below this line 👇

#choice1
print("You were betrayed and are run for your life from vicious hunting dogs.You are forced to run into a cave. There are two tunnels ahead.") 
choice1 = input('Which tunnel? "R" for right or "L" for left ')
lower_choice1 = choice1.lower()
if lower_choice1 == "r":
  print("There is a large gap ahead with total darkness below. Do you try to jump to safety or try to run on the ledge of the hole.")

  
  
  
  #choice2 
  choice2 = input('Which choice? "J" for jump or "L" for ledge ') 
  lower_choice2 = choice2.lower()
  if lower_choice2 == "j":
    print("You jump just short and are about to fall. There is something that looks like a rope hanging on the other side of the cliff.")

    
    #choice3
    choice3 = input('Do you grab or not? "G" for grab or "N" for no ')  
    lower_choice3 = choice3.lower()
    if lower_choice3 == "n":
      print("Turned out not to be a far fall and the dogs do not follow you. You see a light in a hole and climb through it. You fall into a large room with no exits and  three doors. You have to chose a door.")
      
      
      
      
      #choice4
      choice4 = input('Which door? "R" for right, "M" for middle and "L" for left ')
      lower_choice4 = choice4.lower()
      if lower_choice4 == "r":
        print("The right door turned out to be a trap set up by the ancient civilization to stop people from stealing their treasure. You got crushed to death\nGame Over")

      elif lower_choice4 == "m":
        print("You ended up meeting the second half of the group that betrade you that stayed behind to look for the treasure. You are shot on the spot\nGame Over")

      else:
        print("You found the treasure took it and escape through a hidden door in the room\nYou Win!")
        
      


      








      
    #choice3
    else:
      print("Turned out to be a poisonous snake. You die instantly.\nGame Over.")


    
  #choice2
  else:
    print("Hunting dogs caught up\nGame Over.")



#choice1    
else:
  print("Tunnel leads to a large hole that you couldn't see in the dark. You fall in.\nGame Over")