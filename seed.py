
from models import Users, Posts, db, Tags
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

fun = Tags(tag_name ="fun")
sad = Tags(tag_name = "sad")



db.session.rollback()
db.session.add(ari)
db.session.add(ali)
db.session.add(jonah)
db.session.add(fun)
db.session.add(sad)

db.session.commit()

p1 = Posts(title='the rainbows', content = 'Have destroyed humanity',created_at = datetime.now(),user = 1)


p2 = Posts(title='making money', content = 'There is alot of money to be made',created_at = datetime.now(),user = 2)



db.session.add(p1)
db.session.add(p2)

db.session.commit()
