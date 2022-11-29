from typing_extensions import assert_type
from app.db import Base
from sqlalchemy import Column, Integer, String
# below allows for validation of user data before acceptance
from sqlalchemy.orm import validates




# class for user placed below

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

# below validates for emails and ensures the @ is included
    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email 

        return email


