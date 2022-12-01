from os import getenv
from flask import g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# below connects to database using env variable

engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()


# below is where Flask will be set up

# initializes database
def init_db():
    Base.metadata.create_all(engine)

# gets the database
def get_db():
  if 'db' not in g:
    # stores database connection in application context
    g.db = Session()

  return g.db


