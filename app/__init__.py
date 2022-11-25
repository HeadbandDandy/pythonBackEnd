# below imports the routes
from app.routes import home
from app.routes import home, dashboard

# below imports the flask package
from flask import Flask

def create_app(test_config=None):
      # sets up application configuration
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  # below registers the "home, dashboard routes" blueprint 
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
# contains display from routing
  @app.route('/hello')
  def hello():
    return 'hello world'


  return app
