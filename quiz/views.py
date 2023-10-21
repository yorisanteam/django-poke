from cgi import test
import requests, random, json, os
from django.shortcuts import render
from quiz.forms import PokemonForm
from .models import Pokemon

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'poke.json')

def get_japanese_name(pokemon_id):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for pokemon in data:
            if pokemon['id'] == pokemon_id:
                return pokemon['ja']
    return None

def get_pokemon_data():
    random_pokemon_id = random.randint(1,1010)
    url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}/'
    response = requests.get(url)
    data = response.json()
    name = get_japanese_name(random_pokemon_id)
    return name, data['sprites']['front_default']

def index(request):
    POKE_NAME, POKE_IMAGE = get_pokemon_data()
    name, image_url = POKE_NAME, POKE_IMAGE
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            guessed_name = form.cleaned_data['pokemon_name']
            correct_name = POKE_NAME

    else:
        form = PokemonForm()

    return render(request, 'quiz/index.html', {'name': name, 'image_url': image_url, 'form': form, 'POKE_NAME': POKE_NAME})
