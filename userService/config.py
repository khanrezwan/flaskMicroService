class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    #JSONIFY_MIMETYPE = True
    SECRET_KEY = 'My Precious'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017

    #MONGO_URI = 'mongodb://localhost:27017/userService'
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    MONGO_DBNAME = 'userServiceDev'


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    MONGO_DBNAME = 'userServiceTest'


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    MONGO_DBNAME = 'userService'

config_prefix = 'MONGO'
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}