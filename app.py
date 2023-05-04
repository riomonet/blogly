"""Blogly App"""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Users

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "thesecretekey898912"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
with app.app_context():
    connect_db(app)

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users', methods=["POST","GET"])
def user_list():
    """route main user list"""
    users = Users.query.all()
    return render_template('list_users.html',users = users)

@app.route('/users/new')
def add_user_form():
    return render_template('add_usr.html')

@app.route('/users/new', methods=["POST"])
def add_user_post():
    first = request.form['first']
    last = request.form['last']
    url = request.form['image_url']
    user = Users(first=first, last=last, image_url=url)
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<user_id>')
def user_detail(user_id):
    user = Users.query.get_or_404(user_id)
    return render_template('usr_detail.html', user = user)

@app.route('/users/<user_id>/edit')
def edit_user(user_id):
    user = Users.query.get(user_id)
    return render_template('edit_usr.html',user=user)

@app.route('/users/<user_id>/edit', methods=["POST"])
def edit_user_post(user_id):
    user = Users.query.get(user_id)
    user.first = request.form['first']
    user.last = request.form['last']
    user.url = request.form['image_url']
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<user_id>/delete', methods=["POST","GET"])
def delete_user(user_id):

    Users.query.filter_by(id=user_id).delete()
    db.session.commit();
    return redirect ('/users')
    
