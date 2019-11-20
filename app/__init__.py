# from flask import Flask
# from config import DevConfig


# app = Flask(__name__)

# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# from app import views

from flask import Flask
from config import config_options

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions

    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app