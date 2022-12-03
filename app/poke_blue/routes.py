from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .forms import PostForm
from app.models import Post

poke_blue = Blueprint('poke_blue', __name__, template_folder= 'poke_templates')

@poke_blue.route('/posts/create', methods = ['GET', 'POST'])
@login_required
def create_post():
    form= PostForm()
    if request.method == 'POST':
        if form.validate():
            title=  form.title.data
            img_url= form.img_url.data
            caption= form.caption.data

            post = Post(title, img_url, caption, current_user.id)

            post.save_to_db()
            return redirect(url_for('poke_blue.feed'))
    return render_template('create_post.html', form=form)

@poke_blue.route('/posts')
def view_posts():
    posts = Post.query.all()
    return render_template('feed.html', posts=posts)