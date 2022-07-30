from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(30), unique=True)
    password = db.Column(String(16))
    email = db.Column(String, unique=True)
    firstname = db.Column(String)
    lastname = db.Column(String)

    def serialize():
        return{
            "username": self.username
        }

class Character(db.model):
    __tablename__ = "character"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    haircolor = db.Column(String)
    eyecolor = db.Column(String)

class Planet(db.model):
    __tablename__ = 'planet'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    climate = db.Column(String)
    

class Favorites(db.model):
    __tablename__ = "favorite"
    id = db.Column(Integer, primary_key=True)
    character = relationship(Character)
    character_id = db.Column(Integer, ForeignKey("character.id"), nullable=True)
    planet = relationship(Planet)
    planet_id = db.Column(Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship(User)
    user_id = db.Column(Integer, ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }