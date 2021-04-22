from random import randint
import os
import day14_art
print(day14_art.logo)
size=len(day14_art.data) - 1
def display(n):
    print(day14_art.data[n]['name'],', a ',day14_art.data[rand1]['description'],', from ',day14_art.data[rand1]['country'])
count=0
flag=''
while True:
    if flag!='same':
        rand1=randint(0,size)
    print("Compare A: ",end=' ')
    display(rand1)
    print(day14_art.vs)
    rand2=randint(0,size)
    print("Compare B: ",end=' ')
    display(rand2)
    ask=input("Who has more followers ? Type 'A' or 'B': ")
    if ask=='A':
        if day14_art.data[rand1]['follower_count'] >day14_art.data[rand2]['follower_count']:
            count+=1
            print(f"You're right! Current score : {count} ")
            flag='same'
            os.system('clear')
        else:
            print(f"Sorry, that's wrong, final score: {count}")
            break
    elif ask=='B':
        if day14_art.data[rand2]['follower_count'] >day14_art.data[rand1]['follower_count']:
            count+=1
            print(f"You're right! Current score : {count} ")
            flag='same'
            rand1=rand2
            os.system('clear')
        else:
            print(f"Sorry, that's wrong, final score: {count}")
            break
    
    print(day14_art.logo)
# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.