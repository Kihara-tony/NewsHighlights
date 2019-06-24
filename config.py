import os 
class Config:
    '''
    Main configuration parent class
    '''
    NEWSHIGHLIGHT_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWSHIGHLIGHT_API_ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWSHIGHLIGHT_API_KEY = os.environ.get('NEWSHIGHLIGHT_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        config: The parent configuration
    '''
    pass
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


