from flask import Blueprint, render_template, request

from app.auth.forms import UserCreationForm

import requests

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/pokemon1')
def pokemon1():
    return render_template('pokemon1.html',)

@auth.route('/')
@auth.route('/home', methods=['GET', 'POST'])
def home():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            user_input = form.user_input.data
            url_four = 'https://pokeapi.co/api/v2/pokemon/mew'
            response_four = requests.get(url_four)
            new_response_four = response_four.json()
            def get_info(data):
                pokemon_data = []
                for pokemon in data:
                    new_pokemon = {}
                    name = data["forms"][0]["name"]
                    pokemon_key = name
                    new_pokemon[pokemon_key] = {
                        'ability' : data["abilities"][0]["ability"]["name"],
                        'url_sprite': data["sprites"]["front_shiny"],
                        'attack_base_state': data["stats"][1]["base_stat"],
                        'hp_base_stat': data["stats"][0]["base_stat"],
                        'defense_base_stat': data["stats"][2]['base_stat'],
                        'Ability' : data["abilities"][0]['ability']['name']
                    }
                pokemon_data.append(new_pokemon)
                return pokemon_data
            get_info(new_response_four)
    # pokemon = 'Mew'
    return render_template('index.html', form=form) #poke = pokemon, form=form)

