import requests

print(requests.get("http://www.boredapi.com/api/activity/").json()["activity"])