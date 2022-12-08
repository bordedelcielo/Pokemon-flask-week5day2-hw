from app import app
from flask import render_template
from .models import User, Post
from flask_login import current_user


@app.route('/home')
def home():
    users= User.query.all()
    posts= Post.query.all()
    attack_user = set()
    # if current_user.isauthenticated():
    for user in current_user.battled.all():
        attack_user.add(user.id)

    for user in users:
        if user.id in attack_user:
            user.isBattling = True


    return render_template('find_users.html', users=users, posts=posts)





