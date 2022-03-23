from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Hero(Base):
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    birthday = Column(String)
    tribe = Column(String)
    side = Column(String, nullable=False)
    power = Column(Integer)

    def __repr__(self):
        return f'{self.__class__.__name__}:{self.id}:{self.name}'


class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    story = Column(String, unique=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))

