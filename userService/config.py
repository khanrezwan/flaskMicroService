class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    #JSONIFY_MIMETYPE = True
    SECRET_KEY = 'My Precious'
    #MONGO_URI = 'mongodb://localhost:27017/userService'
    @staticmethod
    def init_app(app):
        pass

class DevConfigDocker(BaseConfig):
    """Development configuration for Docker"""
    MONGO_HOST = 'userservice-mongo'
    MONGO_PORT = 27017
    DEBUG = True
    MONGO_DBNAME = 'userServiceDev'

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    DEBUG = True
    MONGO_DBNAME = 'userServiceDev'


class TestingConfig(BaseConfig):
    """Testing configuration"""
    MONGO_HOST = 'localhost'
    DEBUG = True
    TESTING = True
    MONGO_DBNAME = 'userServiceTest'

class TestingConfigDocker(BaseConfig):
    """Testing configuration for Docker"""
    MONGO_HOST = 'userservice-mongo'
    MONGO_PORT = 27017
    DEBUG = True
    TESTING = True
    MONGO_DBNAME = 'userServiceTest'

class ProductionConfig(BaseConfig):
    """Production configuration"""
    MONGO_HOST = 'localhost'
    DEBUG = False
    MONGO_DBNAME = 'userService'

class ProductionConfigDocker(BaseConfig):
    """Production configuration"""
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    DEBUG = False
    MONGO_DBNAME = 'userService'

config_prefix = 'MONGO'

config = {
    'development': DevelopmentConfig,
    'developmentDocker': DevConfigDocker,
    'testing': TestingConfig,
    'testingDocker': TestingConfigDocker,
    'production': ProductionConfig,
    'productionDocker':ProductionConfigDocker,
    'default': DevConfigDocker
}