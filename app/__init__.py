# below imports the routes as well as databse
from app.routes import home, dashboard, api
from app.db import init_db
from app.utils import filters
# below imports the flask package
from flask import Flask

def create_app(test_config=None):

      # sets up application configuration
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
# contains display from routing
  @app.route('/hello')
  def hello():
    return 'hello world'


  # below registers the "home, dashboard routes" blueprint 
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  app.register_blueprint(api)   
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural_words'] = filters.format_plural_words

  init_db(app)
  
  return app
