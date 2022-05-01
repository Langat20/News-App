import os

class Config:
    '''
    Creating configuration main class
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?language=en&apiKey={}'
    # CAT_API_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

#dictionary config_options to help us access different configuration option classes
config_options = {
'development':DevConfig,
'production':ProdConfig
}