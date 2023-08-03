#!/usr/bin/python3
"""" setting de db class"""

import sqlalchemy
from sqlalchemy import create_engine
from os import environ
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models import User, State, City, Amenity, Place, Review


class DBStorage():
    """ this class manage the DB"""

    __engine: None
    __session: None

    def __init__(self):
        """" set the dn engine for swl alchemy
        and erase all tables if test is happening """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            environ["HBNB_MYSQL_USER"],
            environ["HBNB_MYSQL_PWD"],
            environ["HBNB_MYSQL_HOST"],
            environ["HBNB_MYSQL_DB"],
            pool_pre_ping=True))
        if environ["HBNB_ENV"] == "test":
            meta = sqlalchemy.MetaData(self.__engine)
            meta.reflect()
            meta.drop_all()

    def all(self, cls=None):
        """" list all tables or all from one specific askedd in cls"""
        classes = ["BaseModel", "City", "Place",
                   "Amenity", "Review", "State", "User"]
        result_dict = {}
        if cls:
            result = self.__session.query(cls).all()
            key = ""
            for r in result:
                key = str(result.name) + '.' + str(result.id)
                result_dict.update({key: r})
            return result_dict
        else:
            for c in classes:
                result = self.__session.query(c).all()
                key = str(r[0].name) + '.' + str(r[0].id)
                result_dict.update({key: result})

            return result_dict

    def new(self, obj):
        """" add an object to the database """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """ commit all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current database obj if nnot one"""
        if obj:
            self.__session.delete(obj)
            self.__session.save()

    def reload(self):
        """ create tables in DB and session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
