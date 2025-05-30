from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask (__name__)
app.config['SECRET_KEY']='ae55cc2714070645b832bb082177889aea7b6556e0c00e8e01ec94c41f8552e0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kipla.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'





from app import routes  # This ensures routes are registered

