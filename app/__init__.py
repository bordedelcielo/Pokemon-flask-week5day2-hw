from flask import Flask
from config import Config
from .auth.routes import auth
app = Flask(__name__)

app.config.from_object(Config)

#register blueprint
app.register_blueprint(auth)

from . import routes