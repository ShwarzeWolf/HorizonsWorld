from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Battle(Base):
    __tablename__ = 'battles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_id_1 = Column(Integer, ForeignKey('heroes.id'))
    hero_id_2 = Column(Integer, ForeignKey('heroes.id'))
    moto_1_id = Column(Integer, ForeignKey('motos.id'))
    moto_2_id = Column(Integer, ForeignKey('motos.id'))
    winner = Column(Integer)


class Hero(Base):
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    birthday = Column(String)
    tribe = Column(String)
    side = Column(String, nullable=False)
    power = Column(Integer)

    story = relationship('Story', back_populates='hero', uselist=False)
    mottos = relationship('Moto', back_populates='hero')

    def __repr__(self):
        return f'{self.__class__.__name__}:{self.id}:{self.name}'


class Story(Base):
    __tablename__ = 'stories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    story = Column(String, unique=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))

    hero = relationship('Hero', back_populates='story')


class Moto(Base):
    __tablename__ = 'motos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    moto_id = Column(Integer, nullable=False)
    moto = Column(String, unique=True)

    hero = relationship('Hero', back_populates='mottos')





