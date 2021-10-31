import requests

dog = None

while dog == None:
    dog = requests.get(
        "https://api.thedogapi.com/v1/images/search").json()[0]["breeds"]
    dog = dog[0] if len(dog) != 0 else None

print(f'{dog["name"]}: {dog["temperament"]}')
