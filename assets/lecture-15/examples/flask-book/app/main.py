from flask import Blueprint, render_template


bp = Blueprint('main', __name__, url_prefix='/')


@bp.get('/')
def home():
    return render_template('home.html')


@bp.get('/login-register')
def login_register():
    return render_template('login_register.html')


@bp.get('/profile/')
@bp.get('/profile/<username>')
def profile(username=None):
    return render_template('profile.html')
