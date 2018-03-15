from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import app_config
from sqlalchemy.pool import NullPool

class DatabaseService:
    global ENGINE
    ENGINE = app_config['staging'].SQLALCHEMY_DATABASE_URI
    db_engine = create_engine(ENGINE)
    session = None

    def __init__(self):
        """
        :param engine: The engine route and login details
        :return: a new instance of DAL class
        :type engine: string
        """

        if not ENGINE:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        #self.engine = ENGINE
        #db_engine = DatabaseService.DBEngine(self.engine)
        DatabaseService.createSession()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        #init_database(self.engine)
    pass

    @classmethod
    def createSession(cls):
        print("db_session = "+str(cls.session))
        if cls.session is None:
            db_session = sessionmaker(bind=DatabaseService.db_engine)
            cls.session = db_session()

    @staticmethod
    def DBEngine(engine = ENGINE):
       db_engine = create_engine(engine, poolclass=NullPool)
       return db_engine
