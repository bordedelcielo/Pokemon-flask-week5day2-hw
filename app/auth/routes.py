from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from app.auth.forms import UserCreationForm, Signup_Form, Login_Form

import requests

from app.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/pokemon1')
def pokemon1():
    return render_template('pokemon1.html',)


@auth.route('/home', methods=['GET', 'POST'])
def home():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            user_input = form.user_input.data
            url_four = f'https://pokeapi.co/api/v2/pokemon/{user_input}'
            response_four = requests.get(url_four)
            new_response_four = response_four.json()
            pokemon_data = []
            new_pokemon = {}
            name = new_response_four["forms"][0]["name"]
            new_pokemon = {
                'name': new_response_four["forms"][0]["name"],
                'ability' : new_response_four["abilities"][0]["ability"]["name"],
                'url_sprite': new_response_four["sprites"]["front_shiny"],
                'attack_base_state': new_response_four["stats"][1]["base_stat"],
                'hp_base_stat': new_response_four["stats"][0]["base_stat"],
                'defense_base_stat': new_response_four["stats"][2]['base_stat'],
                'Ability' : new_response_four["abilities"][0]['ability']['name']
                }
            pokemon_data.append(new_pokemon)
            return render_template('index.html', form=form)
    return render_template('index.html', poke= pokemon_data, form=form)
            
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form= Signup_Form()
    if request.method == 'POST':
        if form.validate():
            first_name= form.first_name.data
            last_name= form.last_name.data
            email = form.email.data
            password= form.password.data

            user = User(first_name, last_name, email, password)

            user.save_to_db()
            return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form= Login_Form()
    if request.method == 'POST':
        if form.validate():
            email = form.email.data
            password= form.password.data

            user = User.query.filter_by(email=email).first()
            if user:
                if password== user.password:
                    print('Logged in')
                    login_user(user)
                else:
                    print('try again')
            else:
                print('Email does not exist')

    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))





    # return render_template('index.html', poke = pokemon_data, form=form)
            
            
            
            # return redirect(url_for('auth_templates/pokemon1'))

            # print(user_input)
            # print('mew:' 'ability:' 'synchronize,'
            #     'url_sprite:' 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/151.png'
            #     'attack_base_state: 100,'
            #     'hp_base_stat: 100,'
            #     'defense_base_stat: 100,'
            #     'Ability: synchronize')
        # return redirect(url_for('pokemon1'))
            # url_four = 'https://pokeapi.co/api/v2/pokemon/mew'
            # response_four = requests.get(url_four)
            # new_response_four = response_four.json()
            # def get_info(data):
            #     pokemon_data = []
            #     for pokemon in data:
            #         new_pokemon = {}
            #         name = data["forms"][0]["name"]
            #         pokemon_key = name
            #         new_pokemon[pokemon_key] = {
            #             'ability' : data["abilities"][0]["ability"]["name"],
            #             'url_sprite': data["sprites"]["front_shiny"],
            #             'attack_base_state': data["stats"][1]["base_stat"],
            #             'hp_base_stat': data["stats"][0]["base_stat"],
            #             'defense_base_stat': data["stats"][2]['base_stat'],
            #             'Ability' : data["abilities"][0]['ability']['name']
            #         }
            #     pokemon_data.append(new_pokemon)
            #     return pokemon_data
            # get_info(new_response_four)
    # pokemon = 'Mew'


