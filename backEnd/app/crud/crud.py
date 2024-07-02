#!/usr/bin/python3
from sqlalchemy.orm import scoped_session, sessionmaker
import app

classes = {}
storage = app.storage()

def all(cls=None):
    """Query on the current database session"""
    new_dict = {}
    for clss in classes:
        if cls is None or cls is classes[clss] or cls is clss:
            objs = storage.__session.query(classes[clss]).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
    return new_dict

def new(obj):
    """Add the object to the current database session"""
    storage.__session.add(obj)

def save():
    """Commit all changes of the current database session"""
    storage.__session.commit()

def delete(obj=None):
    """Delete from the current database session obj if not None"""
    if obj is not None:
        storage.__session.delete(obj)

def reload():
    """Reload data from the database"""
    storage.__Base.metadata.create_all(storage.__engine)
    sess_factory = sessionmaker(bind=storage.__engine, expire_on_commit=False)
    Session = scoped_session(sess_factory)
    storage.__session = Session

def close():
    """Call remove() method on the private session attribute"""
    storage.__session.remove()

def get(cls, id):
    """Get a specific object by class and ID"""
    instances = storage.all(cls)
    for key, value in instances.items():
        key = key.split(".")
        if key[1] == id:
            return value
    return None

def count(cls=None):
    """Count the number of objects in storage"""
    instances = storage.all(cls)
    return len(instances)
