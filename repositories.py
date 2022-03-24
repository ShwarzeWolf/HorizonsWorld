import random
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions, Insert

from models import Hero, Sides, Motto, Story, Battle

engine = create_engine('postgresql+psycopg2://postgres_user:rootroot@localhost:5000/horizons_world')
Session = sessionmaker(bind=engine)
session = Session()


def add_hero(name: str,
             birthday: datetime,
             tribe: str,
             side: Sides,
             power: int) -> None:
    """Adds new hero to the database"""
    new_hero = Hero(name=name, birthday=birthday, tribe=tribe, side=side, power=power)
    session.add(new_hero)
    session.commit()


class HeroNotFoundException(Exception):
    pass


def add_motto(hero_id: int, motto: str) -> None:
    """Adds motto from hero to database"""
    hero = session.query(Hero).get(hero_id)

    if hero:
        motto_id = len(hero.mottos) + 1
        hero.mottos.append(Motto(motto_id=motto_id, motto=motto))

        session.commit()
    else:
        raise HeroNotFoundException


def add_story(hero_id: int, story: str) -> None:
    """Adds story to hero. If story exists, overrides it"""
    hero = session.query(Hero).get(hero_id)

    if hero:
        if hero.story:
            hero.story.story = story
        else:
            hero.story = Story(story=story)

        session.commit()
    else:
        raise HeroNotFoundException


def delete_hero(hero_id) -> None:
    """Deletes hero from table. With hero deletes users story and all mottos"""
    hero = session.query(Hero).get(hero_id)
    session.delete(hero)
    session.commit()


def add_battle() -> None:
    """Randomly chooses heroes from sides, their mottos and winners"""
    first_warrior = session.query(Hero).order_by(functions.random()).first()
    second_warrior = session.query(Hero).filter(Hero.side != first_warrior.side).order_by(functions.random()).first()

    first_warrior_motto = random.choice(first_warrior.mottos)
    second_warrior_motto = random.choice(second_warrior.mottos)

    winner = random.choice([0, 1, 2])

    new_battle = Battle(hero_id_1=first_warrior.id,
                        hero_id_2=second_warrior.id,
                        motto_id_1=first_warrior_motto.motto_id,
                        motto_id_2=second_warrior_motto.motto_id,
                        winner=winner)

    session.add(new_battle)
    session.commit()
