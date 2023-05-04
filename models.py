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



    


    

    # @classmethod
    # def get_by_species(cls, species):
    #     return cls.query.filter_by(species=species).all()
        
    # @classmethod
    # def get_hungry(cls, species):
    #     return cls.query.filter(cls.hunger > 40)

    # def greet(self):
    #     return f'Hi, I am  {self.name} the {self.species}'
        
    # def __repr__(self):
    #     """show info about pet"""
    #     p = self
    #     return f"<Pets id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"

    


    

    

