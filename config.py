class Config:
    '''
    '''

class DevConfig(Config):
    '''
    '''
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