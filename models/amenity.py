#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):

    __tablename__ = "amenities"

    name = Column(String(128), unique= nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        
        place_amenities = relationship("Place", secondary='place_amenity',
                                   viewonly=False)
    else:
        name = ""
