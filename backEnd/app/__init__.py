#!/usr/bin/python3

from crud.crud import new, save, delete, reload, close, get, count
from core.database import DBStorage

storage = DBStorage()
reload()
