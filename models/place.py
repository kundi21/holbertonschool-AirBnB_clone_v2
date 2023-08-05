#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """

    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey(
                              'amenities.id'), primary_key=True, nullable=False)
                          )

    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all,delete", backref="place")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """"append cities that share state.id"""
            from models import storage

            reviewsOfPlace = []
            for obj in storage.all(Review).values():
                if obj.place_id == self.id:
                    reviewsOfPlace.append(obj)
                return reviewsOfPlace

        @property
        def amenities(self):
            """Getter attribute """
            from models import storage
            list_of_amenities = []
            all_amenities = storage.all(Amenity)
            for key, obj in all_amenities.items():
                if key in self.amenity_ids:
                    list_of_amenities.append(obj)
            return list_of_amenities

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
