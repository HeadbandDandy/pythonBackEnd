# Below contains APi endpoints
import email
import json
import sys
from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()

  try:
    # attempts to create a new User
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )
# below adds data to database 
    db.add(newUser)
    db.commit()
  except:
    # Returns failed message to user
    print(sys.exe_info()[0])

    db.rollback()
        # below is where session object is placed
    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    return jsonify(message = 'Signup failed'), 500

  return jsonify(id = newUser.id)

@bp.route('/users/logout', methods=['POST'])
def logout():
    # below removes session varaibles
    session.clear()
    return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
    data=request.get_json()
    db = get_db()


    try:
            user = db.query(User).filter(User.email == data ['email']).one()
    except:
         print(sys.exc_info()[0])
    if user.verify_password(data['password']) == False:
        # below creates session and sends back response
        session.clear()
        session['user_id'] = user.id
        session['loggedIn'] = True
        
        return jsonify(message = 'Incorrect Credntials'), 400


