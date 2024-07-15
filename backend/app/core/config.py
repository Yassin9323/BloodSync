#!/usr/bin/python3
from os import getenv

class Config:
    
    if getenv('SYNC_ENV') == 'test':
        SYNC_MYSQL_USER = "sync_test"
        SYNC_MYSQL_PWD = "sync_test_pwd"
        SYNC_MYSQL_HOST = "localhost"
        SYNC_MYSQL_DB = "sync_test_db"
        SYNC_ENV = "test"
    else:
        SYNC_MYSQL_USER = "sync_dev"
        SYNC_MYSQL_PWD = "sync_dev_pwd"
        SYNC_MYSQL_HOST = "localhost"
        SYNC_MYSQL_DB = "sync_dev_db"
        SYNC_ENV = "dev"
