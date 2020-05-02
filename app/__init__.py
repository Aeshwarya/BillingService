import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

def create_app(config=None):
    from . import DmModels, Models, controllers, services, settings, resources

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['JWT_DECODE_AUDIENCE'] = settings.SECRET_KEY
    app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
    app.config['JWT_IDENTITY_CLAIM'] = 'jti'

    jwt = JWTManager(app)
    app.config.from_object('app.settings')

    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    DmModels.init_app(app)
    controllers.init_app(app)
    services.init_app(app)
    return app
