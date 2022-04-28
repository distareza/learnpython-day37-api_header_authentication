"""
    Create a new pixelation graph definition.
    https://docs.pixe.la/entry/post-graph
"""
import requests

USERNAME = "brucewyne" # the user name that you pick from main_01_<...>.py
TOKEN = "1C51KQ8653Z3Z5ccWMIEBbb8w4I" # same token as you created from main_01_<...>.py

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_END_POINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "mycyclinghabit",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai" # The color you specify must be one of the following: shibafu / momiji / sora / ichou / ajisai / kuro"
}

print(GRAPH_END_POINT)
response = requests.post(url=GRAPH_END_POINT, json=graph_config, headers=headers)
print(response.text)

# after successfully execute above code please open browser : https://pixe.la/v1/users/brucewyne/graphs/mycyclinghabit.html
