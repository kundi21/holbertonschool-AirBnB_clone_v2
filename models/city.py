#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy as db
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .state import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    name = Column(String(128), unique=True, nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    state = relationship(State, back_populates="cities",
                         cascade="all, delete-orphan")
