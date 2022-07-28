from datetime import datetime
from sqlalchemy import event
from sqlalchemy.sql import func
from sqlalchemy.engine import Engine

from . import db


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(conn, _):
    '''
    Enables foreign key constraints, on every connection
    '''
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.close()


friendships = db.Table(
    'friendships',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), primary_key=True),
    db.Column('followee_id', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(24), nullable=False)
    joined_at = db.Column(db.DateTime(timezone=True), server_default=func.now())    # default is handled by DB

    posts = db.relationship(
        'Post', lazy=True,
        back_populates='author',
        passive_deletes=True,
        # If you use `backref`, instead of `back_populates`, you don't need to define the relationship on the other end
        # backref=db.backref('author', cascade="all, delete"),
    )

    comments = db.relationship(
        'Comment', lazy='raise',
        back_populates='author',
        passive_deletes=True,
        # backref=db.backref('author', cascade="all, delete"),
    )

    followers = db.relationship(
        'User',
        secondary=friendships,
        primaryjoin=(id == friendships.c.follower_id),
        secondaryjoin=(id == friendships.c.followee_id),
        backref="followees",
        cascade="all, delete",
        lazy='subquery'
    )

    def __repr__(self):
        return f'<User {self.id=} {self.username=}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), index=True,
                           default=datetime.utcnow)     # default is handled by Python
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), index=True, nullable=False)
    author = db.relationship(
        'User', lazy=False,
        back_populates='posts',
        # SQlAlchermy will auto-determine the foreign key name.
        # If there are multiple foreign keys, poimnting to the same table,
        # you need to specify the foreign key name youself, using `foreign_keys`.
        # NOTE: it accepts a list of columns, not a single column
        # foreign_keys=[author_id]
    )

    comments = db.relationship('Comment', lazy=True, back_populates='post')

    def __repr__(self):
        return f'<Post {self.title=} {self.author_id=}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)     # default is handled by Python

    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), index=True, nullable=False)
    author = db.relationship('User', lazy=False, back_populates='comments')

    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), index=True, nullable=False)
    post = db.relationship('Post', lazy=False, back_populates='comments')

    def __repr__(self):
        return f'<Post {self.title=} {self.author_id=}>'
