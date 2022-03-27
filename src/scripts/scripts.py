import logging
import random
from datetime import date

import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions

from Exceptions import HeroNotFoundException
from models import Base
from models import Hero, Sides, Motto, Story, Battle

engine = create_engine('postgresql+psycopg2://postgres_user:rootroot@localhost:5000/horizons_world')


# creating database
def create_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def fill_database():
    """
    Database filling
     - Adds 6 heroes to the database,
     - Adds stories for all of them,
     - Adds mottos for all heroes,
     - Generates 10 battles,
   """

    add_hero(name="Aloy", tribe="Nora", power=120, side=Sides.SUN_CARCHA.name, birthday="3021-04-04")
    add_hero(name="Varl", tribe="Nora", power=80, side=Sides.SUN_CARCHA.name, birthday="3015-01-01")
    add_hero(name="Erend", tribe="Oseram", power=80, side=Sides.SUN_CARCHA.name)
    add_hero(name="Helis", tribe="Carcha", power=100, side=Sides.SHADOW_CARCHA.name, birthday="3000-01-01")
    add_hero(name="Olin", tribe="Oseram", power=50, side=Sides.SHADOW_CARCHA.name, birthday="3015-01-01")
    add_hero(name="Sylence", tribe="Banuk", power=60, side=Sides.SHADOW_CARCHA.name)

    add_story(hero_id=1, story="The main protagonist of Horizon Zero Dawn and Horizon Forbidden West. A Nora Brave, "
                               "Seeker and machine hunter of unparalleled skill. Born as an outcast, she was destined "
                               "to save the dying world...")
    add_story(hero_id=2, story="A brave guy from Nora tribe, the son of War-Chief Sona and the older brother of Vala, "
                               "whom Aloy competed against in the Proving")
    add_story(hero_id=3,
              story="An Oseram tribesman, member, and later the captain, of the Carja Sun-King Avad's Vanguard. "
                    "A good guy who likes to drink")
    add_story(hero_id=4,
              story="The Terror of the Sun among the Carja and Stacker of Corpses by the Oseram, is the leader "
                    "of the Eclipse and the secondary antagonist of Horizon Zero Dawn")
    add_story(hero_id=5,
              story="An Oseram tribesman, skilled scout and delver, experienced in exploration of ancient ruins")
    add_story(hero_id=6, story="At an early age, he became fascinated with the Old Ones, and dedicated his life to "
                               "uncovering their secrets, especially what happened to them.")

    add_motto(1, "Survival Requires Perfection")
    add_motto(1, "Being Smart Will Count For Nothing If You Don't Make The World Better")
    add_motto(1, "Keep Flapping Your Mouth. It Makes A Nice Target!")
    add_motto(2, "Before The World Ends!")
    add_motto(2, "From Death Follows New Life. So It Is With The Land... And It Is With Us")
    add_motto(2, "Confidence Is Quiet")
    add_motto(3, "Try Not To Forget About Me While You're Out There Changing The World")
    add_motto(3, "Think You Can Stop Me?")
    add_motto(4, "Change Will Not Come In A Single Sunrise")
    add_motto(4, "I'll Give You The Death You Didn't Have The Spine To Give Me")
    add_motto(5, "I Just Need To Bury It For A While")
    add_motto(6, "Now Keep Going, And Find Something Interesting")
    add_motto(6, "There's so much to learn, and less time than I'd hoped")

    for i in range(10):
        add_battle()


Session = sessionmaker(bind=engine)
session = Session()

# logging options
logging.basicConfig(
    format="%(asctime)s => %(filename)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="log.txt",
    level=logging.DEBUG
)

# Error and critical logs we will write to console
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")
console.setFormatter(console_formatter)

# And also, to another file
file = logging.FileHandler(filename="import_logs.txt")
file.setLevel(logging.ERROR)
file_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")
console.setFormatter(file_formatter)

# Getting root logger
root_logger = logging.getLogger("")

root_logger.addHandler(console)
root_logger.addHandler(file)


class DrawFilter(logging.Filter):
    def filter(self, record):
        return not (record.msg.startswith("Battle") and record.msg.endswith("0"))


root_logger.addFilter(DrawFilter())

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
    return random.choice([0, 1, 2])

