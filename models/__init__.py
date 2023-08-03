#!/usr/bin/python3
""" sets storage bwtween db and filstorage """

from models.engine.file_storage import FileStorage
from os import environ


if environ["HBNB_TYPE_STORAGE"] == "db":
    from db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
