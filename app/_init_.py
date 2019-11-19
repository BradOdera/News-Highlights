from app import views
from flask import Flask
from .config import DevConfig


app = Flask(__name__)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
