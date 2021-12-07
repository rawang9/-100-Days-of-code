# import smtplib
# email="akarshitg9@gmail.com"
# passw="yourpass"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email,password=passw)
#     connection.sendmail(to_addrs="akarshitgupta29@gmail.com",from_addr=email,
#                         msg="Subject:Hello\n\nThis is the body of the mail")
# import datetime as dt
# now=dt.datetime.now()
# print(now)
# print(now.day)
# print(now.today())
# my_dob=dt.datetime(year=2001,month=11,day=10,hour=4,minute=30)
# print(my_dob)
import random
import datetime as dt
import smtplib
email="akarshitg9@gmail.com"
passw="yourpass"

with open("quotes.txt") as quot:
    data=quot.readlines()
todays=random.choice(data)
today=dt.datetime.now()
if today.weekday()==2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=passw)
        connection.sendmail(from_addr=email,to_addrs="akarshitgupta29@gmail.com",msg=f"todays quote\n\n{todays}")

