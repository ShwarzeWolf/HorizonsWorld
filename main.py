from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Sides
from repositories import add_motto, add_story, add_battle, delete_hero, add_hero

engine = create_engine('postgresql+psycopg2://postgres_user:rootroot@localhost:5000/horizons_world')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

add_hero(name='Eloy', tribe='Nora', power=0, side=Sides.WHITE_CARCHA, birthday=datetime.now())
add_hero(name='Varl', tribe='Nora', power=10, side=Sides.WHITE_CARCHA, birthday=datetime.now())
add_hero(name='Erend', tribe='White carcha', power=20, side=Sides.WHITE_CARCHA, birthday=datetime.now())
add_hero(name='Gellis', tribe ='Dark carcha', power = 0, side=Sides.DARK_CARCHA, birthday=datetime.now())
add_hero(name='Olin', tribe ='Dark carcha', power = 2, side=Sides.DARK_CARCHA, birthday=datetime.now())
add_hero(name='Silence', power = 4, side=Sides.DARK_CARCHA, birthday=datetime.now(), tribe='Unknown')

add_story(hero_id=1, story='Чудо женщина')
add_story(hero_id=2, story='A good guy from tribe')
add_story(hero_id=3, story='A good guy another tribe who likes drink')
add_story(hero_id=4, story='Фанатичный мужик')
add_story(hero_id=5, story='Умный мужик')
add_story(hero_id=6, story='Очень умный мужик')

add_motto(1, "Я молодец")
add_motto(1, "Я Элой")
add_motto(2, "Будь что будет")
add_motto(2, "Будь что было")
add_motto(2, "Будет")
add_motto(3, "Тут")
add_motto(3, "Нет")
add_motto(4, "Хай")
add_motto(4, "Хеллок")
add_motto(5, "туц")
add_motto(5, "цут")
add_motto(6, "ааааа")
add_motto(6, "знания")
add_motto(1, "сила")
add_motto(1, "мощььььь")

for i in range(10):
    add_battle()

delete_hero(hero_id=2)


