#!/usr/bin/python3
from sqlalchemy import create_engine
from core.config import Config
from app.models.base_model import Base


class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                    format(Config.HBNB_MYSQL_USER,
                                            Config.HBNB_MYSQL_PWD,
                                            Config.HBNB_MYSQL_HOST,
                                            Config.HBNB_MYSQL_DB))
        if Config.HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
