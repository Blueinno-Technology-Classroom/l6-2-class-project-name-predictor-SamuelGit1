import requests

name = input('Your name: ')

response = requests.get(f'https://api.agify.io?name={name}')

data = response.json()
age = data['age']

response = requests.get(f'https://api.genderize.io?name={name}')

data = response.json()
gender = data['gender']

response = requests.get(f'https://api.nationalize.io?name={name}')

data = response.json()

max_probability = 0
country_with_max_probability = ""

for country in data["country"]:
    if country["probability"] > max_probability:
        max_probability = country["probability"]
        country_with_max_probability = country["country_id"]

print(f'You are probably a {age} years old {gender} from {country_with_max_probability}.')