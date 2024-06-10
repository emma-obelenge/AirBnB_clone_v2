#!/usr/bin/python3
"""
The database storage engine
    Attributes:
        __engine
        __session
    Methods:
        __init__(self)
        all(self, cls==None)
        new(self, obj)
        save(self)
        delete(self, obj=None)
        reload(self)
"""


from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.review import Review
from models.state import State
from models.user import User
from models.city import City
from models. amenity import Amenity
from models.place import Place
from os import getenv


class DBStorage:
    """
    DataBase storage class
    Attributes:
        __engine
        __session
    Methods:
        __init__(self)
        all(self, cls==None)
        new(self, obj)
        save(self)
        delete(self, obj=None)
        reload(self)
    """
    __engine = None
    __session = None

    def __init__(self):
        """The init method for instantiation purpose"""
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')

        if self.__engine is None:
            db_link = "mysql+mysqldb://{}:{}@{}/{}".format(username, password, host, db_name)
            self.__engine = create_engine(db_link, pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """
        method created to query on the current database session based
        on the class name (argument 'cls')
        """
        objs_bank = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objs_bank = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                objs_bank.extend(self.__session.query(subclass).all())
        obj_dict = {}
        for obj in objs_bank:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            try:
                """if obj.__class__.__name__ == 'State':"""
                del obj.sa_instance_state
                obj_dict[key] = obj
            except Exception:
                pass
        return (obj_dict)

    def new(self, obj):
        """ would add the obj to the current db session (self.__session)"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """deletes from the current db session obj if its not None"""
        if obj != None:
            self.__session.delete(obj)

    def save(self):
        """commit all changes of the db session (self.__session)"""
        self.__session.commit()

    def reload(self):
        """refreshes the database session for optimum performance"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(session_factory)
