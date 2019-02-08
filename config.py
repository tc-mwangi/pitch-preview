import os

class Config:
    '''
    general configurations
    '''


class ProdConfig(Config):
    '''
    configurations used in production.

    Args: Config parent class
    '''
    pass


class DevConfig(Config):
    '''
    configurations used in development.

    Args: Config parent class.
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}