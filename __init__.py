from flask import Flask
from appconfig import Config

app = Flask(__name__)
app.config.from_object(Config)

import hello
