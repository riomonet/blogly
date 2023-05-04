from models import Users, db
from app import app

db.drop_all()
db.create_all()

# empyt the table
Users.query.delete()

# add some pets to the sessoin by declearing pet objecsts and
# then doing db.add
ari = Users(first ="ariel", last="zablozki")
ali = Users(first ="ali", last="scheingoltz")
jonah = Users(first ="Jonah", last="mac")

db.session.add(ari)
db.session.add(ali)
db.session.add(jonah)
db.session.commit()
