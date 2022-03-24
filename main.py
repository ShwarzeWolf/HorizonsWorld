from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker

from models import Hero
from repositories import add_motto, add_story, add_battle, delete_hero

engine = create_engine('postgresql+psycopg2://postgres_user:rootroot@localhost:5000/horizons_world')

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Eloy = Hero(name='Eloy', tribe='Nora', power=0, side=Sides.WHITE_CARCHA)
# Varl = Hero(name='Varl', tribe='Nora', power=10, side=Sides.WHITE_CARCHA)
# Erend = Hero(name='Erend', tribe='White carcha', power=20, side=Sides.WHITE_CARCHA)
# Gelis = Hero(name='Gellis', tribe ='Dark carcha', power = 0, side=Sides.DARK_CARCHA)
# Olin = Hero(name='Olin', tribe ='Dark carcha', power = 2, side=Sides.DARK_CARCHA)
# Silence = Hero(name='Silence', power = 4, side=Sides.DARK_CARCHA)

# session.add_all(Silence)
# session.commit()
# story2 = Story(hero_id=2, story='A good guy from tribe')
# story3 = Story(hero_id=3, story='A good guy another tribe who likes drink')
# session.add(story2, story3)
# session.commit()

#add_battle()
delete_hero(hero_id=6)


