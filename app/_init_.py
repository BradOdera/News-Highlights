# from app import views
# from flask import Flask

# app = Flask(__name__)

from app import views
from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)
