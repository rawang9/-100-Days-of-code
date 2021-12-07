##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
email="akarshitg9@gmail.com"
passw="yourpass"
# 1. Update the birthdays.csv
csv=pandas.read_csv("birthdays.csv")
dict=csv.to_dict(orient="records")

#2at lst

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def latterpick(name):
    type = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    with open(f"letter_templates/{random.choice(type)}") as format:
        text = format.read()
    return text.replace("[NAME]", name)
# 4. Send the letter generated in step 3 to that person's email address.
def sendmail(naam,to_Send):
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=passw)
            body=latterpick(naam)
            connection.sendmail(from_addr=email,to_addrs=to_Send,msg=f"Happy Birthday darling\n\n{body}")
# 2. Check if today matches a birthday in the birthdays.csv
today=dt.datetime.now()
for i in range(len(dict)):
    if today.month==dict[i]["month"] and today.day==dict[i]["day"]:
        birdy=dict[i]["name"]
        to=dict[i]["email"]
        sendmail(birdy,to)

