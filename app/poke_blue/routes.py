from flask import Blueprint, render_template, request, redirect, url_for, request, flash
from flask_login import current_user, login_required
from .forms import PostForm
from app.models import Post, User
import requests

poke_blue = Blueprint('poke_blue', __name__, template_folder= 'poke_templates')

@poke_blue.route('/posts/create', methods = ['GET', 'POST'])
@login_required
def create_post():
    form= PostForm()
    if request.method == 'POST':
        if form.validate():
            pokemon= form.pokemon.data.lower()
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
            response = requests.get(url)
            if response.ok:
                new_response = response.json()
                name = new_response["forms"][0]["name"]
                front_shiny = new_response["sprites"]["front_shiny"]
                ability= new_response["abilities"][0]["ability"]["name"]
                attack_base_stat= new_response["stats"][1]["base_stat"]
                hp_base_stat = new_response["stats"][0]["base_stat"]
                defense_base_stat = new_response["stats"][2]['base_stat']
                post = Post(name, front_shiny, ability, attack_base_stat, hp_base_stat, defense_base_stat, current_user.id)
                count_user_id = Post.query.filter_by(user_id = current_user.id).count()
                check_name = Post.query.filter_by(name = name).count()
                if check_name < 1 and count_user_id < 5:
                    post.save_to_db()
                    return redirect(url_for('poke_blue.view_posts'))
                else:
                    return redirect(url_for('poke_blue.create_post'))
    return render_template('create_post.html', form=form)



@poke_blue.route('/posts') 
def view_posts():
    posts = Post.query.all()
    user = User.query.all()
    return render_template('feed.html', posts=posts[::-1], user=user)



@poke_blue.route('/posts/<int:post_id>')
def view_single_post(post_id):
    post=Post.query.get(post_id)
    if post:
        return render_template('single_post.html', post=post)
    else:
        return redirect(url_for('poke_blue.view_posts'))

@poke_blue.route('/posts/delete/<int:post_id>')
def delete_pokemone(post_id):
    post = Post.query.get(post_id)
    if post:
        post.delete_from_db()
    return redirect(url_for('poke_blue.view_posts'))

@poke_blue.route("/attack/<int:user_id>")
@login_required
def attack_user(user_id):
    user = User.query.get(user_id)
    post = Post.query.filter_by(user_id=user_id)

    if user:
        current_user.attack(user)
    else:
        flash('User does not exist')
    
    return render_template('view_opps_pokemon.html', post = post, user = user)    


    # return redirect(url_for('poke_blue.view_posts'))

@poke_blue.route("/attack/<int:user_id>/battle")
@login_required
def results(user_id):
    user = User.query.get(user_id)
    post= Post.query.filter_by(user_id = user_id)
    post_2 = Post.query.filter_by(user_id = current_user)

    if user and sum(post.defense_base_stat) < sum(post_2.attack_base_stat):
        return render_template('battle_winner.html', post=post, post_2=post_2)
    else:
        return redirect(url_for('poke_blue.view_posts'))
    







# @poke_blue.route("/endattack/<int:user_id>")
# @login_required
# def end_attack(user_id):
#     user = User.query.get(user_id)
#     if user:
#         current_user.end_attack(user)
#     return redirect(url_for('poke_blue.view_posts'))



# @poke_blue.route('/posts/update/<int:post_id>' methods=['GET', 'POST'])
# def upgrade_post(post_id):
#     form=Post
#     post=Post.query.get()

