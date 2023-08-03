#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy as db
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):

    __tablename__ = "amenities"

    name = Column(String(128), unique=True, nullable=False)
