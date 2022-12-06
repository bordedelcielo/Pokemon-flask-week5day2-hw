from flask import Blueprint, render_template, request, redirect, url_for, request
from flask_login import current_user, login_required
from .forms import PostForm
from app.models import Post
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
    return render_template('feed.html', posts=posts[::-1])


@poke_blue.route('/posts/<int:post_id>')
def view_single_post(post_id):
    post=Post.query.get(post_id)
    if post:
        return render_template('single_post.html', post=post)
    else:
        return redirect(url_for('poke_blue.view_posts'))



# @poke_blue.route('/posts/update/<int:post_id>' methods=['GET', 'POST'])
# def upgrade_post(post_id):
#     form=Post
#     post=Post.query.get()

