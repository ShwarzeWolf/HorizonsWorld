from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Hero, Story

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

Eloy = Hero(name='Eloy', tribe='Nora', power=0, side='good guys')
session.add(Eloy)
session.commit()

story = Story(hero_id=1, story='born as an outcast, she was destined to save the world...')
session.add(story)
session.commit()