#!/usr/bin/python3
""" Module for testing db storage"""


import unittest
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

class TestDBStorage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """ Set up test environment """
        cls.engine = create_engine("sqlite:///test_db_storage.db", echo=True)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    def setUp(self):
        """ Set up a clean database before each test """
        self.engine.execute("CREATE TABLE IF NOT EXISTS states (id INTEGER PRIMARY KEY, name TEXT);")
        self.engine.execute("CREATE TABLE IF NOT EXISTS cities (id INTEGER PRIMARY KEY, state_id INTEGER, name TEXT);")
        self.engine.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT);")
        self.engine.execute("CREATE TABLE IF NOT EXISTS places (id INTEGER PRIMARY KEY, user_id INTEGER, city_id INTEGER, name TEXT);")
        self.engine.execute("CREATE TABLE IF NOT EXISTS amenities (id INTEGER PRIMARY KEY, name TEXT);")
        self.engine.execute("CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, text TEXT, user_id INTEGER, place_id INTEGER);")
        self.db = DBStorage()
        self.db._DBStorage__engine = self.engine
        self.db.reload()

    def tearDown(self):
        """ Remove the session after each test """
        self.session.close()
        self.engine.execute("DROP TABLE IF EXISTS states;")
        self.engine.execute("DROP TABLE IF EXISTS cities;")
        self.engine.execute("DROP TABLE IF EXISTS users;")
        self.engine.execute("DROP TABLE IF EXISTS places;")
        self.engine.execute("DROP TABLE IF EXISTS amenities;")
        self.engine.execute("DROP TABLE IF EXISTS reviews;")

    def test_all(self):
        """ Test the all method of DBStorage """
        new_state = State(name="California")
        self.session.add(new_state)
        self.session.commit()

        all_objs = self.db.all(State)
        self.assertEqual(type(all_objs), dict)
        self.assertIn("State." + new_state.id, all_objs)

    def test_new(self):
        """ Test the new method of DBStorage """
        new_city = City(name="Los Angeles")
        self.db.new(new_city)
        self.assertIn(new_city, self.session.new)

    def test_save(self):
        """ Test the save method of DBStorage """
        new_user = User(email="test@test.com", password="testpass")
        self.db.new(new_user)
        self.db.save()
        user_from_db = self.session.query(User).filter_by(email="test@test.com").first()
        self.assertIsNotNone(user_from_db)

    def test_delete(self):
        """ Test the delete method of DBStorage """
        new_review = Review(text="Great place!")
        self.db.new(new_review)
        self.db.save()
        review_id = new_review.id
        self.db.delete(new_review)
        review_from_db = self.session.query(Review).filter_by(id=review_id).first()
        self.assertIsNone(review_from_db)

    def test_reload(self):
        """ Test the reload method of DBStorage """
        self.engine.execute("DROP TABLE IF EXISTS states;")
        self.db.reload()
        states = self.session.query(State).all()
        self.assertEqual(len(states), 0)

if __name__ == '__main__':
    unittest.main()
