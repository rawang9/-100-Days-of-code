import requests
import os
import smtplib
KEY=os.environ.get("WFR_API_KEY")#using invernment variable for keys in termainal |--/export VARIABLE_NAME=KEY
email="akarshitg9@gmail.com"
passw=os.environ.get("PASSW")
to_Send="akarshitgupta29@gmail.com"
para={
    "lat":14.749186
    ,"lon":78.553162
    ,"appid":KEY
    ,"exclude": "current,minutely,daily"
    }
response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=para)
response.raise_for_status()
data=response.json()['hourly'][:12]


def sendmail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=passw)
            connection.sendmail(from_addr=email,to_addrs=to_Send,msg=f"today is a rainy day carry the umberella!!")


for i in range(12):
    id=data[i]["weather"][0]["id"]
    print(id)
    if id <700:
        print("Bring your amberala")
        sendmail()
        break
