
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .config import Config
from .auth import auth
from .models import UserModel

log_manager = LoginManager()
log_manager.login_view = "auth.login"

@log_manager.user_loader
def load_user (email):
    return UserModel.query(email)

def create_app ():
    app = Flask(__name__)
    app.config.from_object(Config)

    log_manager.init_app(app)
    bootstrap = Bootstrap(app)
    app.register_blueprint(auth)

    return app
