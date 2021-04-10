=============================================================================
=============================================================================
# 🚨to calculate the average of student height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total=sum(student_heights)
average=round(total/len(student_heights))
print(average)

=============================================================================
#find highest score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
high_score=max(student_scores)
print(f"this high score is {high_score}")

=============================================================================
#carl gauss formula for adding 1 to 100  is everse it and add 1st element of
#both list and multiply it with len(list)/2 = sum form 1 to 100
Write your code below this row 👇
#sum the even no
sum_of_even_no=(sum(list(i for i in range(2,101,2))))
print(sum_of_even_no)
=============================================================================
# Write your code below this row 👇 (THE fizz BUZZ game)
for i in range(1,100):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
        continue
    elif i%5==0:
        print("Buzz")
        continue
    else:
        print(i)
=============================================================================
Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passl=[]
for i in range(nr_letters):
    passl.append(random.choice(letters))
for times in range(nr_numbers):
    passl.append(random.choice(numbers))
for times in range(nr_symbols):
    passl.append(random.choice(symbols))

random.shuffle(passl)
password=''.join(passl)
print(password)
=============================================================================
