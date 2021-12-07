import requests
import datetime
import smtplib
#current time
curr_hr=datetime.datetime.now().hour
#my country night time
my_lat=26.846708
my_long=80.946159
#night time
def istime():

    print("istime")
    given_data = {"lat": my_lat,"lng": my_long,"formatted": 0}
    data = requests.get("https://api.sunrise-sunset.org/json", params=given_data)
    dict = data.json()["results"]
    sunrise = int(dict['sunrise'].split("T")[1].split(":")[0]) + 5
    sunset = int(dict['sunset'].split("T")[1].split(":")[0]) + 5
    if curr_hr>=sunset or curr_hr<=sunrise:
        return True
#iss  loaction
def issloc():
    print("iss")

    response=requests.get("http://api.open-notify.org/iss-now.json")
    iss_lat=float(response.json()["iss_position"]["latitude"])
    iss_lng=float(response.json()["iss_position"]["longitude"])
    if my_lat+5 >= iss_lat >= my_lat-5 and my_long + 5 >= iss_lng >= my_long - 5:
        return True
#cooking
while True:
    if issloc() and istime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="akarshitg9@gmail.com",password=yourpass)
            connection.sendmail(from_addr="akarshitg9@gmail.com",to_addrs="akarshitgupta29@gmail.com",msg="iss on your top\n\nlook up now")
            print("done")
            break

