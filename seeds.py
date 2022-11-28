# This file uses Base class with engine connection to drop all existing tables
# Secondly this file will create any file that Base mappped

from app.models import User
from app.db import Session, Base, engine


# below drops and rebuilds tables as needed
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

