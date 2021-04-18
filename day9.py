=============================================================================
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key]>90:
        student_grades[key]="Outstanding"
        continue
    elif student_scores[key]>80:
        student_grades[key]="Exceesds Expectation"
        continue
    if student_scores[key]>70:
        student_grades[key]="Acceptable"
        continue
    if student_scores[key]<70:
        student_grades[key]="Fail"
        continue
                
    

# 🚨 Don't change the code below 👇
print(student_grades)



=============================================================================
=============================================================================
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(ctry,tms,plce):
    new={}
    new["country"]=ctry
    new["visits"]=tms
    new["cities"]=plce
    travel_log.append(new)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
    =============================================================================
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
def finder(file):
    high=0
    name=""
    for key in file:
        if high<file[key]:
            high=file[key]
            name=key
    print(f"the winner is {name} with {high} $")
    
print(logo)
print("Welcome to the secret ouction program. ")
flag=True
file={}
while flag is True:
    name=input("what is your name? :")
    bit=int(input("what is your bit ammount $ ? :"))
    decison=input("Anyone else want to take part say 'yes' or 'no' :").lower()
    file[name]=bit
    if decison=='no':
        flag=False
    else:
        os.system('clear')
finder(file)
