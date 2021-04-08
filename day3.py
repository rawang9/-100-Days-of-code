#=============================================================================
# =============================================================================
print("Welcome to the love calculator")
name1=input("enter you name ")
name2=input("enter her name ")
l=name1.lower().count('l')
o=name1.lower().count('o')
v=name1.lower().count('v')
e=name1.lower().count('e')

t=name2.lower().count('t')
r=name2.lower().count('r')
u=name2.lower().count('u')
e=name2.lower().count('e')
boy=t+r+u+e
grl=l+o+v+e
lov=int(str(boy)+str(grl))
print(lov)
if lov<=10 or lov>90:
    print(f"your score is {lov} , you go together like coke and mintos")
if lov>40 and lov<50:
    print(f"your score is {lov} , you are alright")
else:
    print("you are all right")

# main project the tresure hunt game =============================================================================
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Tresure island,\n Your mission is to find the tresure")
step1=input("You're at a cross road,Where do you want to go? Type 'left' or 'right' \n")
if step1=="left":
    step2=input("you came on a middle of a lake you like to 'wait' for boat or like to 'swim' \n")
    if step2=='wait':
        step3=input("you arrive at islan,there is a house with one 'Red' door,'Yellow' and one 'Blue door' \n")
        if step3=='Yellow':
            print("Hurray!  you won the game and tresure")
        else:
            print("there is a lion ")
    else:
        print("shark will eat you fool ")
else:
    print("killed by a car ")
#=============================================================================
