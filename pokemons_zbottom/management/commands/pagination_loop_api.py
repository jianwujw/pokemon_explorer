# run through the api to find how many pokemons there are total

import requests

page = 1
batch = 20
num_pokemon = 1

while True:
    url = f'https://pokeapi.co/api/v2/pokemon/?offset={(page-1)*batch}&limit={batch}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemons = data['results']

        if not pokemons:
            break

        for pokemon in pokemons:
            print(num_pokemon ,pokemon['name'],page)
        page +=1
        num_pokemon+=1
    else:
        print("nothing",response.status_code)
        break