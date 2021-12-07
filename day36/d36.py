STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import os
s_key="PQNS7SB9PEV7GP5M"
news_key="aac333a97bde4482b8cf51ac7f5db8e7"

import requests
from datetime import *
DATE=str(datetime.now().date())
## STEP 1: Use https://www.alphavantage.co
#When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
para={
    "function":"GLOBAL_QUOTE"
    ,"symbol":STOCK
    ,"apikey":s_key
}
response=requests.get("https://www.alphavantage.co/query",params=para)
response.raise_for_status()
change=response.json()["Global Quote"]["10. change percent"][:-1]


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def headline():
    n_para={
        "q":COMPANY_NAME
        ,"from" :DATE
        ,"sortBy":"popularity"
        ,"apiKey":news_key
    }
    news=requests.get("https://newsapi.org/v2/everything",params=n_para)
    news.raise_for_status()
    tophead=news.json()["articles"][0]["title"]
    return tophead


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
import smtplib
from email.mime.text import MIMEText
def sendmail(new,booli):
    email="akarshitg1@gmail.com"
    passw="your pass"
    to="akarshitgupta29@gmail.com"
    news=str(new)
    text=''
    flag=booli
    if flag:
        text=f"TSLA: Up!{int(float(change))}%"
    else:
        text=f"TSLA:  Down !{int(float(change))}%"
    text=MIMEText(text.encode('utf-8'), _charset='utf-8')
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=passw)
            connection.sendmail(from_addr=email,to_addrs=to,msg=f"Subject:{text}\n\n{news}")


#Optional: Format the SMS message like this: 
if float(change)>5:
    new=headline()
    sendmail(new,True)
elif float(change)<-5:
    new=headline()
    sendmail(new,False)
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or

"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

