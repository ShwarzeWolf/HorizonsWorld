from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Hero

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

Eloy = Hero(name='Eloy', tribe='Nora', power=0, side='WhiteCarcha')
session.add(Eloy)
session.commit()

print(session.query(Hero).get(1))