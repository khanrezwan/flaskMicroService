from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from config import config, config_prefix

pyMongo = PyMongo()
restAPI = Api()


def createApp(config_name, config_prefix_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    from userServiceApp import userMicroService as userServiceBlueprint
    app.register_blueprint(userServiceBlueprint)

    #pyMongo.init_app(app=app, config_prefix=config_prefix_name)
    pyMongo.init_app(app=app, config_prefix=config_prefix_name)
    restAPI.init_app(app)

    return app

