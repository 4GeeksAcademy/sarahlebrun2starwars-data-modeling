import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name =Column(String(250), nullable=False)
    hair_color =Column(String(250), nullable=True)
    birth_year =Column(String(250), nullable=True)
    gender =Column(String(250), nullable=True)
    eye_color =Column(String(250), nullable=True)
    height =Column(String(250), nullable=True)
    mass =Column(String(250), nullable=True)
    skin_color =Column(String(250), nullable=True)
class Plante (Base):
    __tablename__ = 'plante'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter =Column(String(250), nullable=False)
    rotation_period =Column(String(250),nullable=True)
    gravity =Column(String(250), nullable=True)
    population =Column(String(250), nullable=True)
    climate =Column(String(250), nullable=True)
    surface_water =Column(String(250), nullable=True)
    orbital_period =Column(String(250), nullable=True)



class User(Base):
    __tablename__="user"
    id =Column(Integer, primary_key=True)
    username =Column(String(250), nullable=False)
    firstname =Column(String(250), nullable=False)
    lastname =Column(String(250), nullable=True)
    email =Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__="favorites"
    id = Column(Integer, primary_key=True)
    user=relationship(User)
    user_id=Column(Integer, ForeignKey("user.id"))
    character=relationship(Character)
    character_id=Column(Integer, ForeignKey("character.id"))
    plante=relationship(Plante)
    plante_id=Column(Integer, ForeignKey("plante.id"))
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
