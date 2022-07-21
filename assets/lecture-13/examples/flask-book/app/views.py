from flask import render_template
from . import app
from .models import User, Post


@app.get('/')
def home():
    return render_template('home.html')


@app.get('/users')
def users():
    all_users = User.query.all()
    all_posts = Post.query.all()

    return render_template('users.html', users=all_users, posts=all_posts)
