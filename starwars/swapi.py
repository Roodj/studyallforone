from pprint import pprint

import requests

characters = requests.get('https://swapi.dev/api/people/').json()
people = characters.get('results')

...
# character = characters.json()
# planet = character.get('results')[0].get('homeworld')
# planet = requests.get(planet).json().get('diameter')
# pprint(planet)
pprint(people)