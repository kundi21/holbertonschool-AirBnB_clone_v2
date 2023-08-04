#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
import os
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary='place_amenity',
                                   viewonly=False)
    else:
        name = ""
