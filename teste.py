import json
import requests

URL = 'http://127.0.0.1:5000'

body = {"nome": "ABC Palace", "avaliacao": 5.0,"diaria": 450, "cidade": "São Paulo - SP"}

#POST
novo_hotel = requests.post(URL + '/hoteis/abc_palace', data=body)

#GET
hoteis = requests.get(URL + '/hoteis')
if hoteis.status_code == 200:
    hoteis = hoteis.json()
    print('Total de hoteis cadastrados: ', len(hoteis['hoteis']))
    print('\nPrimeiro hotel da lista: ', hoteis['hoteis'][0], '\n')
    for indice, hotel in enumerate(hoteis['hoteis']):
        print(indice + 1, ' - ', hotel['nome'])

orlando_hotel = requests.request('GET', URL + '/hoteis/orlando').json()
print('\n Hotel: ', orlando_hotel['nome'])
print(' Avaliação: ', orlando_hotel['avaliacao'])
print(' Diária: ', orlando_hotel['diaria'])
print(' Cidade: ', orlando_hotel['cidade'])

#DELETE
requests.delete(URL + '/hoteis/abc_palace')
hoteis = requests.get(URL + '/hoteis').json()
print('\nTotal de hoteis cadastrados: ', len(hoteis['hoteis']))
