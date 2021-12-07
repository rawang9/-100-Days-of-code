import requests
import os
os.environ["APP_ID"]="962529b0"
os .environ["API_KEY"]="110b4530d35247eaa910c70188f52721"
NUTAPI_KEY=os.getenv("API_KEY")
ID=os.environ.get("APP_ID")
URL="https://trackapi.nutritionix.com/v2/natural/exercise"

quer=input("Tell me which exercises you did: ")
para={
    "query":quer,
    "gender":"male",
    "weight_kg":80,
    "height_cm":172,
    "age":21
}

head={
 "x-app-id":ID,
 "x-app-key":NUTAPI_KEY,
}

response=requests.post(URL,json=para,headers=head)
result=response.json()


#working with sheets
from datetime import *
os.environ["SHEET_URL"]="https://api.sheety.co/faa4625b2c3b38e4724d2d7b6a2e5546/newProject/workouts"
Sheet_url=os.getenv("SHEET_URL")
today=datetime.now().strftime(f"%d/%m/%Y")
time=datetime.now().strftime("%X")
os.environ["TOKEN"]="Basic YWthcnNoaXRnMTpha2Fyc2hpdGc5"
head={
    "Authorization": os.getenv("TOKEN")
}
for exercise in result["exercises"]:
    sheet_inp={
      "workout":{
          "date":today,
          "time":time,
          "exercise":exercise["name"].title(),
          "duration":exercise["duration_min"],
          "calories":exercise["nf_calories"],
      }
    }
    print(sheet_inp)
    sheet_res=requests.post(Sheet_url,json=sheet_inp,headers=head)
    print(sheet_res.text)
40264


