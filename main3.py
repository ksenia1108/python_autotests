import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN =  'c1272f4ba10b668cc614e1da48985748'
HEADER ={'Content-Type': 'application/json', 'trainer_token': TOKEN}

requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER)
body_create = {
    "pokemon_id": "280093"
}
responce_create = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_create)
print(responce_create.text)