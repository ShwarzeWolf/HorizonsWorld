import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Text, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Sides(enum.Enum):
    """Enum to store sides names from horizons world"""
    WHITE_CARCHA = 0
    DARK_CARCHA = 1


Battle = Table(
    'battles', Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('hero_1_id', Integer, ForeignKey('heroes.id')),
    Column('hero_2_id', Integer, ForeignKey('heroes.id')),
    Column('motto_1_id', Integer, ForeignKey('mottos.id')),
    Column('motto_2_id', Integer, ForeignKey('mottos.id')),
    Column('winner', Integer, nullable=False))


class Hero(Base):
    """A Base class to story info about main heroes"""
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    birthday = Column(Date())
    tribe = Column(String(50))
    side = Column(Enum(Sides), nullable=False)
    power = Column(Integer)

    story = relationship('Story', back_populates='hero', uselist=False)
    mottos = relationship('Motto', back_populates='hero')
    battles = relationship('Hero', secondary=Battle,
                           primaryjoin=id == Battle.c.hero_1_id,
                           secondaryjoin=id == Battle.c.hero_2_id,
                           )

    def __repr__(self):
        return f'{self.__class__.__name__}:{self.id}:{self.name}:{self.side}\n' \
               f'birthday: {self.birthday}\n' \
               f'tribe: {self.tribe}\n'


class Story(Base):
    """A class to store short story of hero life, without spoilers"""
    __tablename__ = 'stories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    story = Column(Text, unique=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))

    hero = relationship('Hero', back_populates='story')

    def __repr__(self):
        return f'{self.hero_id}:{self.story}'


class Motto(Base):
    """A class to store heroes mottos"""
    __tablename__ = 'mottos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    motto_id = Column(Integer, nullable=False)
    motto = Column(String(255), unique=True, nullable=False)

    hero = relationship('Hero', back_populates='mottos')

    def __repr__(self):
        return f'{self.hero_id}:{self.motto_id}:{self.motto}'