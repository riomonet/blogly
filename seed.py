
from models import Users, Posts, db
from app import app
from datetime import datetime


db.drop_all()
db.create_all()

# empyt the table
Users.query.delete()
Posts.query.delete()

# add some pets to the sessoin by declearing pet objecsts and
# then doing db.add
ari = Users(first ="ariel", last="zablozki")
ali = Users(first ="ali", last="scheingoltz")
jonah = Users(first ="Jonah", last="mac")


db.session.rollback()
db.session.add(ari)
db.session.add(ali)
db.session.add(jonah)

db.session.commit()

p1 = Posts(title='post 1 user 1', content = 'this is post 1, nice to see you',created_at = datetime.now(),user = 1)


p2 = Posts(title='post 1 user 2', content = 'this is post 2, nice to see you',created_at = datetime.now(),user = 2)

db.session.add(p1)
db.session.add(p2)

db.session.commit()
