import logging
import random
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions

from models import Hero, Sides, Motto, Story, Battle

engine = create_engine('postgresql+psycopg2://postgres_user:rootroot@localhost:5000/horizons_world')
Session = sessionmaker(bind=engine)
session = Session()

# Требования к logging:
#  - минимум 1 фильтр на события (например, не писать лог если бой закончился вничью).

#  - один хендлер с отправкой части логов в консоль.
#  - один хендлер с отправкой части логов в другой файл.
#
#  - НЕОБЯЗАТЕЛЬНО: хендлер с отправкой error & critical логов в телеграмм бота с помощью telegram api.
#    Бот сразу пишет сообщение либо в группу, id которой указан в env, либо в личку пользователю, id которого указан в env. Я должен быть добавлен в эту группу: @rioran

logging.basicConfig(
    format="%(asctime)s => %(filename)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

#01:24:09
console = logging.StreamHandler()
console.setLevel(logging.ERROR)

def add_hero(name: str,
             birthday: datetime,
             tribe: str,
             side: Sides,
             power: int) -> None:
    """Adds new hero to the database"""
    new_hero = Hero(name=name, birthday=birthday, tribe=tribe, side=side, power=power)
    session.add(new_hero)
    session.commit()

    logging.info(f'Hero was created: {new_hero}')


class HeroNotFoundException(Exception):
    pass


def add_motto(hero_id: int, motto: str) -> None:
    """Adds motto from hero to database"""
    hero = session.query(Hero).get(hero_id)

    if hero:
        motto_id = len(hero.mottos) + 1
        hero.mottos.append(Motto(motto_id=motto_id, motto=motto))

        session.commit()
        logging.info(f'Motto {motto} for hero {hero_id} was added')
    else:
        logging.critical(f'Hero not found')
        raise HeroNotFoundException


def add_story(hero_id: int, story: str) -> None:
    """Adds story to hero. If story exists, overrides it"""
    hero = session.query(Hero).get(hero_id)

    if hero:
        if hero.story:
            hero.story.story = story
            logging.info(f'story {story} for hero {hero_id} was updated')
        else:
            hero.story = Story(story=story)
            logging.info(f'Story {story} for hero {hero_id} was added')

        session.commit()
    else:
        logging.critical(f'Hero not found')
        raise HeroNotFoundException


def delete_hero(hero_id: int) -> None:
    """Deletes hero from table. With hero deletes users story and all mottos"""
    hero = session.query(Hero).get(hero_id)

    if hero:
        session.delete(hero)
        session.commit()
        logging.info(f'Hero {hero_id} successfully deleted')
    else:
        logging.warning(f'Hero {hero_id} doesn\'t exist - probably as you wanted')


def add_battle() -> None:
    """Randomly chooses heroes from sides, their mottos and winners"""
    first_warrior = session.query(Hero).order_by(functions.random()).first()
    second_warrior = session.query(Hero).filter(Hero.side != first_warrior.side).order_by(functions.random()).first()

    first_warrior_motto = random.choice(first_warrior.mottos)
    second_warrior_motto = random.choice(second_warrior.mottos)

    winner = random.choice([0, 1, 2])

    new_battle = Battle(hero_id_1=first_warrior.id,
                        hero_id_2=second_warrior.id,
                        motto_id_1=first_warrior_motto.id,
                        motto_id_2=second_warrior_motto.id,
                        winner=winner)

    session.add(new_battle)
    session.commit()
    logging.info(f'Battle between {first_warrior.name} and {second_warrior.name} happened. Winner: {winner}')