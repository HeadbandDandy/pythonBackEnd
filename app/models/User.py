from app.db import Base
from sqlalchemy import Column, Integer, String
# below allows for validation of user data before acceptance
from sqlalchemy.orm import validates
# below contains encryption import
import bcrypt
salt = bcrypt.gensalt()




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

# below validates for passwords over the length of 5 characters

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 5
        # below encrypts password
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    # below verifies the password
    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )
