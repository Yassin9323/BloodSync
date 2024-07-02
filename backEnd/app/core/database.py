#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from core.config import Config



class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None
    __Base = declarative_base()

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(Config.HBNB_MYSQL_USER,
                                             Config.HBNB_MYSQL_PWD,
                                             Config.HBNB_MYSQL_HOST,
                                             Config.HBNB_MYSQL_DB))
        if Config.HBNB_ENV == "test":
           self.__Base.metadata.drop_all(self.__engine)
