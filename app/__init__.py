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

  return app
