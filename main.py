from sqlalchemy import create_engine

from interaction_scripts import functionality_preview
from models import Base

engine = create_engine('postgresql+psycopg2://postgres_user:rootroot@localhost:5000/horizons_world')

Base.metadata.create_all(engine)

functionality_preview()
