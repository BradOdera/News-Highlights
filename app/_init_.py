from flask import Flask
from .config import DevConfig


app = Flask(__name__, instance_path='/home/moringa/Documents/Flask-Core/News-Highlights/app/instance', instance_relative_config=True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
