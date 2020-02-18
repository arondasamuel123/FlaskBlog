import os
class Config:
    '''
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:123456@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
    '''
    Development config class
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:123456@localhost/blog'
    DEBUG = True
class ProdConfig(Config):
    '''
    '''
class TestConfig(Config):
    '''
    '''
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
    
}