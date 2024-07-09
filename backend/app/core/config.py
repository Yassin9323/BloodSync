#!/usr/bin/python3
from os import getenv

class Config:
    # HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
    # HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
    # HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
    # HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
    # HBNB_ENV = getenv('HBNB_ENV')
    
    HBNB_MYSQL_USER = "sync_dev"
    HBNB_MYSQL_PWD = "sync_dev_pwd"
    HBNB_MYSQL_HOST = "localhost"
    HBNB_MYSQL_DB = "sync_dev_db"
    HBNB_ENV = "dev"
