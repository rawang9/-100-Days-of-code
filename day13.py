# =============================================================================
# #debug excercise
# number = int(input("Which number do you want to check?"))
# #hear we need to use ==
# #if number % 2 = 0:
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#   print("This is an odd number.")
#   
# =============================================================================
# =============================================================================
# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# =============================================================================
for number in range(1, 101):
    #we need to use and condition
        
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
    #we need to use elif 
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)