from flask import current_app as app
from werkzeug.security import generate_password_hash

from datetime import datetime, timedelta
from random import randint, choice, sample

from faker import Faker
from mdgen import MarkdownPostProvider

from . import db
from .models import User, Post


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()


'''
Here be dragons!!!
'''


@app.cli.command('add-data')
def add_data():
    faker = Faker()
    faker.add_provider(MarkdownPostProvider)

    User.query.delete()

    db.session.commit()

    users = [User(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        email=faker.email(),
        username=faker.user_name(),
        password_hash=generate_password_hash('1234')
    ) for _ in range(5)]

    for u in users:
        u.followers = [f for f in sample(users, randint(1, 4)) if f != u]
        db.session.add(u)

    ts = datetime.utcnow()

    posts = []
    for _ in range(50):
        p = Post(title=faker.sentence(), body=faker.post(size='small'), created_at=ts)
        posts.append(p)
        ts -= timedelta(microseconds=randint(1, 10**11))

    for p in sorted(posts, key=lambda p: p.created_at):
        u = choice(users)
        u.posts.append(p)

    db.session.commit()
