# This file uses Base class with engine connection to drop all existing tables
# Secondly this file will create any file that Base mappped

from app.models import User
from app.db import Session, Base, engine


# below drops and rebuilds tables as needed
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# dummy data for testing below 

# Session class establishes a temporary connection
db = Session()

db.add_all([
      User(username='googie21', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilldog13', email='rmebes1@sogou.com', password='password123'),
  User(username='sambo12', email='cstoneman2@last.fm', password='password123'),
  User(username='johnnygirl14', email='ihellier3@google.jp', password='password123'),
  User(username='iamsenorfrog4', email='gmidgley4@weather.com', password='password123'),
  User(username='cheeseanddope', email='notvalid@gmail.com', password='cheese12345')
])

db.commit()

db.close()