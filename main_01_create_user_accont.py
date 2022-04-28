"""
    Utilize pixela API for Habit Tracker
    https://docs.pixe.la/

    Create a user in Pixela
    https://docs.pixe.la/entry/post-user
"""
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "1C51KQ8653Z3Z5ccWMIEBbb8w4I", # [required] A token string used to authenticate as a user to be created. The token string is hashed and saved.
    "username": "brucewyne", # [required] User name for this service.
    "agreeTermsOfService": "yes", # 	[required] Specify yes or no whether you agree to the terms of service.
    "notMinor": "yes" # [required] Specify yes or no as to whether you are not a minor or if you are a minor and you have the parental consent of using this service.
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)
# If Success return : {"message":"Success. Let's visit https://pixe.la/@brucewyne , it is your profile page!","isSuccess":true}
# If Fail return {"message":"This user already exist.","isSuccess":false}