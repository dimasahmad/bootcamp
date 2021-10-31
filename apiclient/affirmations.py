import requests

print(requests.get("https://www.affirmations.dev/").json()["affirmation"])