from random import choice
from flask import current_app as app, render_template

from sqlalchemy.orm import joinedload, subqueryload, load_only
from sqlalchemy.sql import and_, or_, func
from sqlalchemy.exc import IntegrityError

from . import db
from .models import User, Post


@app.get('/')
def home():
    return render_template('home.html')


@app.get('/login-register')
def login_register():
    return render_template('login_register.html')


@app.get('/profile/')
@app.get('/profile/<username>')
def profile(username=None):
    return render_template('profile.html')


@app.get('/queries')
def queries():
    barry = User.query.filter_by(username='barry78').one()

    User.query.filter(or_(User.username == 'barry78', User.username == 'barry79')).one()
    User.query.filter(User.email.endswith('example.org')).all()
    Post.query.filter(Post.body.like('%notice%')).all()

    Post.query.order_by(Post.created_at.desc()).limit(10).offset(10).all()
    Post.query.order_by(Post.created_at.desc()).slice(21, 31).all()

    User.query.with_entities(User.username).group_by(User.username).all()
    User.query.options(load_only(User.username)).group_by(User.username).all()

    Post.query.options(joinedload(Post.author)).order_by(Post.created_at.desc()).limit(10).all()
    Post.query.options(subqueryload(Post.author)).order_by(Post.created_at.desc()).limit(10).all()

    if barry is not None:
        Post.query.with_parent(barry).order_by(Post.title).all()

    try:
        user1 = User(username='Test4', password="1234", firstname='Test', lastname='Test', email='example4@example.com')
        user2 = User(username='Test5', password="1234", firstname='Test', lastname='Test', email='example5@example.com')
        user3 = User(username='Test6', password="1234", firstname='Test', lastname='Test', email='example6@example.com')
        # user.posts.append(...)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)

        barry.email = 'new@example.com'
        barry.followees.append(user1)
        barry.followers.append(user2)

        db.session.commit()

        # db.session.delete(user1)

        db.session.commit()
    except IntegrityError as ex:
        app.logger.debug(ex)
        db.session.rollback()

    return '<html><body><h1>Queries</h1></body></html>'


@app.get('/more-queries')
def more_queries():
    users_alphabetically = User.query.order_by(User.lastname, User.firstname).all()
    random_user = choice(users_alphabetically)

    post_count_sub = Post.query.filter(Post.author_id == User.id).with_entities(
        func.count(Post.id).label('post_count')).scalar_subquery()
    last_post_per_user_sub = Post.query.with_entities(Post.author_id, func.max(
        Post.created_at).label('last_post_ts')).group_by(Post.author_id).subquery()

    context = {
        'first_user': User.query.first(),
        'users_alphabetically': users_alphabetically,
        'user_posts': Post.query.with_parent(random_user).all(),
        'user_post_count': Post.query.with_parent(random_user).with_entities(func.count(Post.id).label('post_count')).scalar(),
        'usernames': User.query.options(load_only(User.username)).order_by(User.username).all(),
        'login_user': User.query.filter(and_(User.username == random_user.username, User.password == random_user.password)).one_or_none(),
        'ten_latest_posts': Post.query.options(joinedload(Post.author)).with_entities(Post, User).order_by(Post.created_at.desc()).limit(10).all(),
        'first_post_from_search': Post.query.filter(or_(Post.title.like('%est%'), Post.body.like('%est%'))).first(),
        # Here be dragons
        'user_with_post_count_1': User.query.join(Post).group_by(User).with_entities(User, func.count(Post.id).label('post_count')).all(),
        'user_with_post_count_2': User.query.with_entities(User, post_count_sub.label('post_count')).all(),
        'users_with_their_latest_post_1': User.query.join(Post).with_entities(User, Post).filter(and_(User.id == last_post_per_user_sub.c.author_id, Post.created_at == last_post_per_user_sub.c.last_post_ts)).all(),
        'users_with_their_latest_post_2': User.query.join(Post).join(last_post_per_user_sub, and_(User.id == last_post_per_user_sub.c.author_id, Post.created_at == last_post_per_user_sub.c.last_post_ts)).with_entities(User, Post).all(),
    }

    return render_template('test.html', context=context)
