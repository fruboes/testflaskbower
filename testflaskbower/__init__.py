from flask import Flask
from flask_bower import Bower

app = Flask(__name__)
Bower(app)

from testflaskbower import views

