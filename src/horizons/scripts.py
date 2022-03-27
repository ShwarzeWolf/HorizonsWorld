import random
from datetime import date

import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions

from exceptions import HeroNotFoundException
from logging_setup import logging
from models import Hero, Sides, Motto, Story, Battle
