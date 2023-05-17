"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text 

db = SQLAlchemy()

def connect_db(app):
        db.init_app(app)

class Users(db.Model):
        """users model"""
    
        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        first = db.Column(db.String(25),nullable = False)
        last = db.Column(db.String(25),nullable = False)
        image_url = db.Column(db.String(40), nullable = True)
        post = db.relationship("Posts", backref="users", cascade="all, delete-orphan")

        @property
        def full_name(self):
                """Return full name of user."""

                return f"{self.first} {self.last}"



class Posts(db.Model):
        """posts"""

        __tablename__ = 'posts'

        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        title = db.Column(db.String(50),nullable = False)
        content = db.Column(db.String(200),nullable = False)
        created_at = db.Column(db.DateTime, nullable = False)
        user = db.Column(db.Integer, db.ForeignKey('users.id'))

        usr = db.relationship('Users',backref = 'posts')


class Tags(db.Model):

        """table of tags"""
        __tablename__ = 'tags'

        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        tag_name = db.Column(db.String(25), nullable = False)
        posts = db.relationship('Posts', secondary='post_tags'
                                ,cascade="all,delete"
                                , backref = 'tags')




class Tag_Posts(db.Model):
        """m2m tag-posts table"""

        __tablename__ = 'post_tags'

        tag_id =  db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key = True)
        post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key = True)

        
