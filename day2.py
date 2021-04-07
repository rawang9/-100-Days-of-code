#add the nuber digit
#=============================================================================
num=input("enter the no.")
print(int(num[0])+int(num[1]))

#=============================================================================
#project 1 a BMI calculator
#=============================================================================
weight=input("Enter your hieght in kg: ")
height=input("Enter your hieght in m: ")
print(int(int(weight)//(float(height)**2)))

#=============================================================================
print(round(8/3, 2))
score=21
print(f"your score is {score}")
#days left on this planet
#=============================================================================
ag=input("enter you age ")
year=90
age=year-int(ag)
month=int(age)*12
week=round(int(age)*(365/7))
days=365*int(age)
print(f"you have {month} months , {week} weeks and {days} days left on this planet")
#=============================================================================
#final project od day to a payment cal clulator
print("Welcome to the tip calculator.")
total=int(input("What was the total bill ?"))
tip=int(input("What % of tip you like to give 10 ,15, 30 ?"))
people=int(input("No of people "))
print("%.2f" % round((total+(total*(tip/100)))/people, 2))

