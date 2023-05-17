"""Blogly App"""


from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Users, Posts, Tags, Tag_Posts
from datetime import datetime
from forms import SnackForm

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

@app.route('/tags')
def tag_list():
    tags = Tags.query.all()
    return render_template('list_tags.html', tags=tags)

@app.route('/tags/<tag_id>')
def tag_detail(tag_id):
    tags = Tags.query.get_or_404(tag_id)
    return render_template('tag_detail.html',tags = tags)

@app.route('/tags/new')
def add_tag_form():
    return render_template('add_tag.html')

@app.route('/tags/new', methods=["POST"])
def add_tag_post():
    name = request.form['tag_name']
    tag_name = Tags(tag_name=name)
    db.session.add(tag_name)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<tag_id>/edit')
def edit_tag(tag_id):
    tags = Tags.query.get(tag_id)
    return render_template('edit_tag.html',tags=tags)


@app.route('/tags/<tag_id>/edit', methods=["POST"])
def edit_tag_post(tag_id):
    tag = Tags.query.get_or_404(tag_id)
    tag.tag_name = request.form['tag_name']
    # db.session.add(tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<tag_id>/delete')
def delete_tag(tag_id):

    Tags.query.filter_by(id=tag_id).delete()
    db.session.commit();
    return redirect ('/tags')

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
    
@app.route('/users/<user_id>/posts/new')
def new_post(user_id):
    user = Users.query.get(user_id)
    tags = Tags.query.all()
    return render_template('add_post.html', user = user, tags = tags)

@app.route('/users/<user_id>/posts/new', methods=["POST"])
def add_post_to_db(user_id):
    title = request.form['title']
    content = request.form['content']
    time_stamp = date = datetime.now()
    
    tag_list = request.form.getlist("tags")
    tag_ids = [int(num) for num in tag_list]
    tags = Tags.query.filter(Tags.id.in_(tag_ids)).all()
    print(tags)
    p = Posts(title=title, content=content,created_at = time_stamp, user = user_id, tags=tags )

    db.session.add(p)
    db.session.commit()
    user = Users.query.get(user_id)
    return render_template('usr_detail.html', user = user)

@app.route('/posts/<post_id>')
def view_post(post_id):
    post = Posts.query.get(post_id)
    tags = post.tags
    return render_template('post.html',post=post, tags=tags)

@app.route('/posts/<post_id>/edit')
def edit_post(post_id):
    post = Posts.query.get(post_id)
    tags = Tags.query.all()
    return render_template('edit_post.html',post=post, tags=tags)

@app.route('/posts/<post_id>/edit', methods=["POST"])
def update_posts_table(post_id):
    post= Posts.query.get(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    post.created_at = datetime.now()

    tag_list = request.form.getlist("tags")
    tag_ids = [int(num) for num in tag_list]
    post.tags = Tags.query.filter(Tags.id.in_(tag_ids)).all()

    db.session.add(post)
    db.session.commit()
    return redirect(f'/posts/{post_id}')

@app.route('/posts/<post_id>/delete', methods=["POST"])
def delete_post(post_id):
    user = Posts.query.get(post_id).usr.id
    Posts.query.filter_by(id=post_id).delete()
    db.session.commit();
    return redirect (f'/users/{user}')
    

