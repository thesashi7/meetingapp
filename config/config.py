
import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY="powerful secretkey"
    WTF_CSRF_SECRET_KEY="a csrf secret key"

class DevelopmentConfig(Config):
    """Configurations for Development."""
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/deliver'
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/test_db'
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://yncnpfsqgbsbxs:fe6c6b6b087d3340b0a4d8deb8ac87ed87b033ff5ac56457954fca6ffa196e29@ec2-54-221-212-208.compute-1.amazonaws.com:5432/de5hkq6361fb1a'

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
app_secret = "something-secret"
SQLALCHEMY_TRACK_MODIFICATIONS = False
