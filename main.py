import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN =  'c1272f4ba10b668cc614e1da48985748'
HEADER ={'Content-Type': 'application/json', 'trainer_token': TOKEN}

requests.post(url=f'{URL}/pokemons', headers=HEADER)
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create )
print(response_create.text)
