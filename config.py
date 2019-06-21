import os 
class Config:
    '''
    Main configuration parent class
    '''
    NEWSHIGHLIGHTS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWSHIGHLIGTS_API_KEY = os.environ.get('NEWSHIGHLIGHT_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        config: The parent configuration
    '''
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        config:The parent configuration class
    '''
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}


