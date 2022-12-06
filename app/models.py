from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security  import generate_password_hash

db = SQLAlchemy()

# catch_pokemon = db.Table(
#     'catch_pokemon':
#     db.Column('user_pokemon_id', db.Integer, db.ForeignKey('user.id'), nullable = False)
#     db.Column('catch_pokemon_id', db.Integer, db.ForeignKey('data.id'), nullable = False)
# )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    last_name= db.Column(db.String(50), nullable=False, unique=True)
    email= db.Column(db.String(250), nullable=False, unique=True)
    password= db.Column(db.String(250), nullable=False)
    post= db.relationship('Post', backref='Author', lazy=True)
    # catch_pokemon = db.relationship('User',
    #     primaryjoin = (catch_pokemon.columns.user_pokemon_id=id),
    #     secondaryjoin= (catch_pokemon.columns.catch_pokemon_id=id),
    #     secondary= catch_pokemon,
    #     backref= db.backref('catch_pokemon', lazy='dynamic'),
    #     lazy='dynamic'
    # )
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name= last_name
        self.email = email
        self.password= generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Post(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(), nullable=False)
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    front_shiny= db.Column(db.String)
    ability = db.Column(db.String(250))
    attack_base_stat= db.Column(db.Integer)
    hp_base_stat= db.Column(db.Integer)
    defense_base_stat= db.Column(db.Integer)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __init__(self, name, front_shiny, ability, attack_base_stat, hp_base_stat, defense_base_stat, user_id):
        self.name = name
        self.front_shiny = front_shiny
        self.ability= ability
        self.attack_base_stat = attack_base_stat
        self.hp_base_stat = hp_base_stat
        self.defense_base_stat = defense_base_stat
        self.user_id = user_id


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_db(self):
        db.session.commit()

class Data(db.Model):
    __tablename__ = 'data'
    pokemon_id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250))
    front_shiny= db.Column(db.String)
    ability = db.Column(db.String(250))
    attack_base_stat= db.Column(db.Integer)
    hp_base_stat= db.Column(db.Integer)
    defense_base_stat= db.Column(db.Integer)

    def __init__(self, name, ability, front_shiny, attack_base_stat, hp_base_stat, defense_base_stat):
        self.name = name
        self.ability= ability
        self.front_shiny = front_shiny
        self.attack_base_stat = attack_base_stat
        self.hp_base_stat = hp_base_stat
        self.defense_base_stat = defense_base_stat

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

