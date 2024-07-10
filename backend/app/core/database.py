#!/usr/bin/python3
from sqlalchemy import create_engine
from app.core.config import Config
from typing import Type
from app.models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models.base_model import BaseModel
from app.models.hospitals import Hospital
from app.models.blood_banks import BloodBank
from app.models.blood_types import BloodType
from app.models.hospitals_Inventory import HospitalInventory
from app.models.bloodBanks_Inventory import BankInventory
from app.models.transactions import Transaction
from app.models.users import User
from app.models.blood_requests import Request


classes = {"Hospital": Hospital, "User": User,
        "BloodBank": BloodBank, "BloodType": BloodType, "HospitalInventory": HospitalInventory,
        "BankInventory": BankInventory, "Request": Request, "Transaction": Transaction}

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
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()


    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
                    # print(new_dict[key])
        # update User c9cc30a1-50c0-41d2-8b56-59963276abba password Yassin
        # x = "c9cc30a1-50c0-41d2-8b56-59963276abba"
        # print(new_dict[User.__class__.__name__ + '.' + x])
        # print(new_dict)
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self, obj=None):
        """Commit all changes of the current database session"""
        if not self.__session.object_session(obj):
            self.__session.add(obj)
        self.__session.commit()
        self.__session.refresh(obj)
    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            try:
                self.__session.delete(obj)
            except Exception as e:
                print(e)

    def reload(self):
        """Reload data from the database"""
        self.__session.close()
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Get a specific object by class and ID"""
        instances = self.all(cls)
        for key, value in instances.items():
            key = key.split(".")
            if key[1] == id:
                return value
        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        print(type(cls))
        instances = self.all(cls)
        return len(instances)

    def get_by_email(self, email: str) -> User:
        return self.__session.query(User).filter(User.email == email).first()
