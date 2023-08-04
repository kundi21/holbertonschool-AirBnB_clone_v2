#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
import os


class Amenity(BaseModel, Base):

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"

        name = Column(String(128), unique=True,
                      primary_key=True, nullable=False)
    else:
        name = ""
