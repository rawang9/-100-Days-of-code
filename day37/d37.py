import requests
from _datetime import *
TOOKEN="akdsjlkj1lkjj231j1k24jl1k"
USER="akarshitg9"
para={
    "token":TOOKEN
    ,"username":USER
    ,"agreeTermsOfService":"yes"
    ,"notMinor":"yes"
}

pixela_endp="https://pixe.la/v1/users"
#for creating id
# response=requests.post(url=pixela_endp,json=para)
# print(response.text)

#graph
g_para={
    "id":"graph1",
    "name":"coding",
    "unit":"min",
    "type":"int",
    "color":"momiji",
}
head={
    "X-USER-TOKEN":TOOKEN
}
grph_end=f"{pixela_endp}/{USER}/graphs"
#response=requests.post(url=grph_end,json=g_para,headers=head)
#print(response.text)


#todays date
today = datetime.now()
todays_date=today.strftime("%Y%m%d")
graph_data={
     "date":todays_date,
     "quantity":input("How many min you code today? "),
 }

update_graph=f"{grph_end}/graph1"
update=requests.post(url=update_graph,json=graph_data,headers=head)
print(update.text)
#update
update_end=f"{update_graph}/20210516"
# need_to_up={
#     "quantity":input("How many min you code today? "),
# }
# update_current=requests.put(url=update_end,json=need_to_up,headers=head)
# print(update_current.text)
#delete on date=20210518
del_pix=f"{update_graph}/20210518"
#dele=requests.delete(url=del_pix,headers=head)
#print(dele.text)

#angela code
# import requests
# from datetime import datetime
#
# USERNAME = "YOUR USERNAME"
# TOKEN = "YOUR SELF GENERATED TOKEN"
# GRAPH_ID = "YOUR GRAPH ID"
#
# pixela_endpoint = "https://pixe.la/v1/users"
#
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# ## POST
# # response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
#
# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# today = datetime.now()
# # print(today.strftime("%Y%m%d"))
#
# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": input("How many kilometers did you cycle today? "),
# }
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
#
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "4.5"
# }
#
# ## PUT
# # response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# # print(response.text)
#
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
#
# ## DELETE
# # response = requests.delete(url=delete_endpoint, headers=headers)
# # print(response.text)