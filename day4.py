=============================================================================
import random
rand=random.randint(0,1)
print(rand)
if rand == 0:
    print("head")
else:
    print("tells")
=============================================================================
the london game to pay the bill
people=input("enter the names saperated by ',' : ")
name_list=people.split(',')
import random
print(name_list[random.randint(0,(len(name_list)-1))], "you are a GOAT for today")
=============================================================================
#the treasure hunt game
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

map[int(position[0])-1][int(position[1])-1]=' *'




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
=============================================================================
the rock paper ceser game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user=int(input("What do you choose? Type 0 for rock,1 for paper or 2 for Scissors  "))
object=['rock','paper','scissors']
import random
comp_rand=random.randint(0,2)
def prinf(ro):
    if ro=='rock':
        print(rock)
    elif ro=='paper':
        print(paper)
    elif ro == 'scissors':
        print(scissors)
n=True

prinf(object[user])
print("Computer chose: \n ")
prinf(object[comp_rand])
if user==0 and comp_rand==1:
    print("you lose paper will wrap yr rock")
elif user==0 and comp_rand==2:
    print("you win by brocking the scissor")
elif user==1 and comp_rand==2:
    print("you lose paper will cut down")
elif user==1 and comp_rand==0:
    print("you win paper will wrap yr rock")
elif user==2 and comp_rand==1:
    print("you win paper will cut down")
elif user==2 and comp_rand==0:
    print("you lose yr scissor ge broken by rock")
elif user==comp_rand:
    print("try again draw")
