from models import Base, Sides
from scripts import engine, add_hero, add_story, add_motto, add_battle


def create_database():
    """Drops all data, created new data"""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def fill_database():
    """ Database filling
     - Adds 6 heroes to the database,
     - Adds stories for all of them,
     - Adds mottos for all heroes,
     - Generates 10 battles"""

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


if __name__ == '__main__':
    create_database()
    fill_database()
