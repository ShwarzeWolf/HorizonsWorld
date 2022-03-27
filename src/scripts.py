from datetime import date
from random import choice

import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions

from logging_setup import logging
from exceptions import HeroNotFoundException
from models import Hero, Sides, Motto, Story, Battle

import os
DB_URI = os.getenv("DATABASE_URL")

engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
session = Session()

# adding interface to work with command line
app = typer.Typer(help="Small simulation for horizons_universe")


@app.command()
def add_hero(name: str,
             side: str = Sides.SUN_CARCHA.name,
             birthday: str = None,
             tribe: str = None,
             power: int = 0) -> None:
    """Adds new hero to the database"""
    if birthday:
        birthday = date.fromisoformat(birthday)

    new_hero = Hero(name=name, birthday=birthday, tribe=tribe, side=side, power=power)
    session.add(new_hero)
    session.commit()

    logging.info(f"Hero was created: {new_hero}")


@app.command()
def add_motto(hero_id: int,
              motto: str) -> None:
    """Adds motto from hero to database"""
    hero = session.query(Hero).get(hero_id)

    if hero:
        motto_id = len(hero.mottos) + 1
        hero.mottos.append(Motto(motto_id=motto_id, motto=motto))

        session.commit()
        logging.info(f"Motto {motto} for hero {hero_id} was added")
    else:
        logging.critical(f"Hero with id {hero_id} not found")
        raise HeroNotFoundException


@app.command()
def add_story(hero_id: int,
              story: str) -> None:
    """Adds story to hero. If story exists, overrides it"""
    hero = session.query(Hero).get(hero_id)

    if hero:
        if hero.story:
            hero.story.story = story
            logging.info(f"story {story} for hero {hero_id} was updated")
        else:
            hero.story = Story(story=story)
            logging.info(f"Story {story} for hero {hero_id} was added")

        session.commit()
    else:
        logging.critical(f"Hero with id {hero_id} not found")
        raise HeroNotFoundException


@app.command()
def delete_hero(hero_id: int,
                force: bool = typer.Option(
                    ...,
                    prompt="Are you sure you want to delete this hero?",
                    help="Force deletion without confirmation",
                ),
                ) -> None:
    """Deletes hero from table. With hero deletes users story and all mottos"""

    hero = session.query(Hero).get(hero_id)

    if hero:
        if force:
            session.delete(hero)
            session.commit()
            logging.info(f"Hero {hero_id} successfully deleted")
        else:
            logging.debug(f"Deletion of {hero_id} cancelled")
    else:
        logging.warning(f"Hero {hero_id} doesn't exist - probably as you wanted")


@app.command()
def add_battle(number_of_battles=1) -> None:
    """Randomly chooses heroes from sides, their mottos and winners"""
    first_warrior = session.query(Hero).order_by(functions.random()).first()
    second_warrior = session.query(Hero).filter(Hero.side != first_warrior.side).order_by(functions.random()).first()

    first_warrior_motto = first_warrior.get_random_motto()
    second_warrior_motto = second_warrior.get_random_motto()

    winner = choose_winner(first_warrior, second_warrior)

    for battle in range(number_of_battles):
        new_battle = Battle(hero_id_1=first_warrior.id,
                            hero_id_2=second_warrior.id,
                            motto_id_1=first_warrior_motto.id,
                            motto_id_2=second_warrior_motto.id,
                            winner=winner)

        session.add(new_battle)
        session.commit()

    logging.info(f"Battle between {first_warrior.name} and {second_warrior.name} happened. Winner: {winner}")


def choose_winner(hero_1: Hero, hero_2: Hero) -> int:
    """Chooses who will win in the battle"""
    return choice([0, 1, 2])


if __name__ == '__main__':
    app()

