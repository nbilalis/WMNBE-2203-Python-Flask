from os import environ
from flask import Flask, render_template
from models import db, User, Post

from datetime import datetime, timedelta
from random import randint, choice, sample
from lorem import sentence, paragraph

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/flask-book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# db = SQLAlchemy(app)
db.init_app(app)


@app.get('/')
def home():
    return 'Welcome to Flask-book!'


@app.get('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()


'''
Here be dragons!!!
'''


@app.cli.command('add-data')
def add_data():
    User.query.delete()

    db.session.commit()

    users = [
        User(username='stevie', lastname='Copeland', firstname='Stephen', email="stevie@sae.edu", password="123"),
        User(username='aias', lastname='Paraskevopoulos', firstname='Aias', email="aias@sae.edu", password="123"),
        User(username='fotis', lastname='Zachopoulos', firstname='Fotis', email="fotis@sae.edu", password="123"),
        User(username='nikos', lastname='Bilalis', firstname='Nikos', email="nikos@sae.edu", password="123")
    ]

    for u in users:
        u.followers = [f for f in sample(users, randint(1, 4)) if f != u]
        db.session.add(u)

    ts = datetime.now() - timedelta(weeks=9*4)    # .utcnow()

    for _ in range(50):
        p = Post(title=sentence(), body=paragraph(), time_created=ts)
        u = choice(users)
        u.posts.append(p)
        ts += timedelta(microseconds=randint(1, 10**12))

    db.session.commit()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(environ.get("SERVER_PORT", 8081)))
