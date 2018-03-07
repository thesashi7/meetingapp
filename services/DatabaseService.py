from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import app_config


class DatabaseService:
    global ENGINE
    ENGINE = app_config['development'].SQLALCHEMY_DATABASE_URI

    def __init__(self):
        """
        :param engine: The engine route and login details
        :return: a new instance of DAL class
        :type engine: string
        """

        if not ENGINE:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = ENGINE
        db_engine = DatabaseService.DBEngine(self.engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        # init_database(self.engine)

    pass

    @staticmethod
    def DBEngine(engine=ENGINE):
        db_engine = create_engine(engine)
        return db_engine
