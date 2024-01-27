import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_by_level():
    '''
    AT-1 Get trainers code 200
    '''
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code==200, 'Positive status code'

def test_get_trainers_by_id():
    '''
    AT-2 Get trainers my id
    '''
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3592}, timeout=5)
    assert response.json()['city'] == 'Самара', 'Coreect city'
    assert response.json()['trainer_name'] == 'Антон', 'Coreect name'