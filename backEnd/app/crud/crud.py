#!/usr/bin/python3
from sqlalchemy.orm import scoped_session, sessionmaker
import app
from core.database import DBStorage

classes = {}
storage = app.storage()

class Crud(DBStorage):
    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database"""
        self.__Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

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
        instances = self.all(cls)
        return len(instances)
