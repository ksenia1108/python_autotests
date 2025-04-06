import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN =  'c1272f4ba10b668cc614e1da48985748'
HEADER ={'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '28464'
TRAINER_NAME = 'Лапулик'

def test_status_code():
    response = requests.get(
        url=f'{URL}/trainers', 
        params={'trainer_id': TRAINER_ID},
        headers=HEADER)
    assert response.status_code == 200

def test_piece_body():
    response = requests.get(
        url=f'{URL}/trainers', 
        params={'trainer_id': TRAINER_ID},
        headers=HEADER)
    assert response.json()['data'][0]['trainer_name'] == 'Лапулик'
    print (response.json())