"""
    Delete Habit Graph
    https://docs.pixe.la/entry/delete-pixel
"""
import datetime

import requests

USERNAME = "brucewyne" # the user name that you pick from main_01_<...>.py
TOKEN = "1C51KQ8653Z3Z5ccWMIEBbb8w4I" # same token as you created from main_01_<...>.py
GRAPH_ID = "mycyclinghabit" # the graph id that you pick from main_02_<...>.py

#today = datetime.datetime.now()
today = datetime.datetime(year=2022, month=4, day=25)
#date_text = "20220421"
date_text = today.strftime("%Y%m%d")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_END_POINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_text}"

headers = {
    "X-USER-TOKEN": TOKEN
}

print(GRAPH_END_POINT)
response = requests.delete(url=GRAPH_END_POINT, headers=headers)
print(response.text)

# after successfully execute above code please open browser : https://pixe.la/v1/users/brucewyne/graphs/mycyclinghabit.html
