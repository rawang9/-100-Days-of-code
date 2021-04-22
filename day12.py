#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
print('''____                                                   ______    __                             __  __                            __                       
/\  _`\                                                /\__  _\  /\ \                           /\ \/\ \                          /\ \                      
\ \ \L\_\   __  __     __     ____    ____             \/_/\ \/  \ \ \___       __              \ \ `\\ \    __  __    ___ ___    \ \ \____     __    _ __  
 \ \ \L_L  /\ \/\ \  /'__`\  /',__\  /',__\               \ \ \   \ \  _ `\   /'__`\             \ \ , ` \  /\ \/\ \ /' __` __`\   \ \ '__`\  /'__`\ /\`'__\
  \ \ \/, \\ \ \_\ \/\  __/ /\__, `\/\__, `\               \ \ \   \ \ \ \ \ /\  __/              \ \ \`\ \ \ \ \_\ \/\ \/\ \/\ \   \ \ \L\ \/\  __/ \ \ \/ 
   \ \____/ \ \____/\ \____\\/\____/\/\____/                \ \_\   \ \_\ \_\\ \____\              \ \_\ \_\ \ \____/\ \_\ \_\ \_\   \ \_,__/\ \____\ \ \_\ 
    \/___/   \/___/  \/____/ \/___/  \/___/                  \/_/    \/_/\/_/ \/____/               \/_/\/_/  \/___/  \/_/\/_/\/_/    \/___/  \/____/  \/_/ 
    
    ''')
cpu=random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm taking a number between 1 and 100. ")
level=input("Choose a difficulty. Type'easy' or 'hard': ")
if level=='hard':
    n=5
else:
    n=10
flag=False
def checker(guesses):
    if guesses>cpu:
        print("Too high. ")
        return False
    elif guesses<cpu:
        print("Too LOW. ")
        return False
    elif guesses==cpu:
        print("you got correct this time")
        return True
for i in range(n):
    print(f"you have {n-i} attemp left ")
    guess=int(input("Make a guess :"))
    flag=checker(guess)
    if flag==True:
        break
    print("Guess again")