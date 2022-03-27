import enum
from random import choice

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Sides(enum.Enum):
    """Enum to store sides names from horizons world"""
    SUN_CARCHA = 0
    SHADOW_CARCHA = 1


class Battle(Base):
    """A class to store battles between different sides in the Universe"""
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_id_1 = Column(Integer, nullable=False)
    hero_id_2 = Column(Integer, nullable=False)
    motto_id_1 = Column(Integer, nullable=False)
    motto_id_2 = Column(Integer, nullable=False)
    winner = Column(Integer, nullable=False)

    hero1 = relationship("Hero", foreign_keys=hero_id_1, primaryjoin="Battle.hero_id_1==Hero.id")
    hero2 = relationship("Hero", foreign_keys=hero_id_2, primaryjoin="Battle.hero_id_2==Hero.id")

    motto1 = relationship("Motto", foreign_keys=motto_id_1, primaryjoin="Battle.motto_id_1==Motto.id")
    motto2 = relationship("Motto", foreign_keys=motto_id_2, primaryjoin="Battle.motto_id_2==Motto.id")

    def __repr__(self):
        return f"{self.__class__.__name__}|" \
               f"{self.hero_id_1} with motto {self.motto_id_1} against {self.hero_id_2} with motto {self.motto_id_2}"


class Hero(Base):
    """A Base class to story info about main heroes"""
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    birthday = Column(Date())
    tribe = Column(String(50))
    side = Column(Enum(Sides), nullable=False)
    power = Column(Integer)

    story = relationship("Story", back_populates="hero", uselist=False, cascade="all, delete-orphan")
    mottos = relationship("Motto", back_populates="hero", cascade="all, delete-orphan")

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.id}:{self.name}|{self.side}|" \
               f"birthday:{self.birthday}|" \
               f"tribe:{self.tribe}"

    def get_random_motto(self) -> "Motto":
        """Returns random motto from hero gor the battle"""
        return choice(self.mottos)


class Story(Base):
    """A class to store short story of hero life, without spoilers"""
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    story = Column(Text)
    hero_id = Column(Integer, ForeignKey("heroes.id"))

    hero = relationship("Hero", back_populates="story")

    def __repr__(self):
        return f"{self.hero_id}:{self.story}"


class Motto(Base):
    """A class to store heroes mottos"""
    __tablename__ = "mottos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_id = Column(Integer, ForeignKey("heroes.id"))
    motto_id = Column(Integer, nullable=False)
    motto = Column(String(255), unique=True, nullable=False)

    hero = relationship("Hero", back_populates="mottos")

    def __repr__(self):
        return f"{self.hero_id}:{self.motto_id}:{self.motto}"
