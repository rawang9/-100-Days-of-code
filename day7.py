import random
from hang_day7 import stages,logo
from day_7word import word_list
lis=word_list
cpu=lis[random.randint(0,len(lis)-1)]
guess=[]
print(logo)
for i in range(len(cpu)):
    guess.append("_")
init=0
flag=True
hang=0
while flag!=False and cpu!=''.join(guess): 
    char=input("gess the later ")
    init=0
    for i in cpu:
        if i==char:
            guess[init]=char
            print("you guess the correct one ")
        init+=1
    print(guess)
    if char not in cpu:
        hang+=1
        print(stages[-hang])
        
        if hang==7:
            flag=False
            print("Game over,you loose ...")
if cpu==''.join(guess):\
     print("you won the game  \n\n",logo)
    
