from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'data/flask-book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = environ.get('SECRET_KEY', '6910c3b2348009a76ca995485fd0d499de2b6434d6a544403330c715c65381a7')

db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

# db.init_app(app)
# toolbar.init_app(app)

from . import views     # noqa: F401, E402
from . import filters   # noqa: F401, E402
from . import commands  # noqa: F401, E402
