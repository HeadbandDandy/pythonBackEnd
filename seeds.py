# This file uses Base class with engine connection to drop all existing tables
# Secondly this file will create any file that Base mappped

from app.models import User, Post, Comment, Vote
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


# below are inserted Post Seeds
db.add_all([
  Post(title='Donec posuere metus vitae ipsum', post_url='https://buzzfeed.com/in/imperdiet/et/commodo/vulputate.png', user_id=1),
  Post(title='Morbi non quam nec dui luctus rutrum', post_url='https://nasa.gov/donec.json', user_id=1),
  Post(title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', post_url='https://europa.eu/parturient/montes/nascetur/ridiculus/mus/etiam/vel.aspx', user_id=2),
  Post(title='Nunc purus', post_url='http://desdev.cn/enim/blandit/mi.jpg', user_id=3),
  Post(title='Pellentesque eget nunc', post_url='http://google.ca/nam/nulla/integer.aspx', user_id=4)
])

db.commit()


# below are to test comments in SQL
db.add_all([
  Comment(comment_text='nahhhhhhhhh.', user_id=1, post_id=2),
  Comment(comment_text='yaahhhhaahahahahahahahahaha.', user_id=1, post_id=3),
  Comment(comment_text='boooooooooogggggeeeeerrrrrsssssss', user_id=2, post_id=1),
  Comment(comment_text='eeeeeeeeeeeeeeeeeeeeeeee', user_id=2, post_id=3),
  Comment(comment_text='In hadgafghjdbfa agdhaf dha dhafjl;we dhaj', user_id=3, post_id=3)
])

db.commit()


# below contains tests for votes in SQL
db.add_all([
  Vote(user_id=1, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])

db.commit()

db.close()