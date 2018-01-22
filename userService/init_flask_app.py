from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from config import config
from flask_consulate import Consul
import os


pyMongo = PyMongo()
restAPI = Api()
consul = Consul()


def createApp(config_name, config_prefix_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    from userServiceApp import userMicroService as userServiceBlueprint
    app.register_blueprint(userServiceBlueprint)

    #pyMongo.init_app(app=app, config_prefix=config_prefix_name)
    pyMongo.init_app(app=app, config_prefix=config_prefix_name)
    restAPI.init_app(app)
    consul.init_app(app)
    consul.register_service(
        name='userservice-app',
        interval='10s',
        tags=['userservice'],
        port=5000,
        httpcheck='http://'+os.getenv('USER_SERVICE_IP')+':'+os.getenv('USER_SERVICE_PORT')+'/healthcheck'
    )
    return app

#todo check this git https://github.com/subokita/consul-docker-test