#!/usr/bin/python3
""" """
from console import HBNBCommand
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Removes the file.json"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8(self):
        """Tests pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        checking = style.check_files(['models/base_model.py'])
        self.assertEqual(checking.total_errors, 0, "fix pep8")

    def test_default(self):
        """Tests for the type of instances"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Tests the kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Tests the kwargs passing ints"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Tests the correct value returned by str"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Tests to_dict() method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Tests for None key and value"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Tests for one key"""
        n = {'Name': 'test'}
        new = self.value(**n)

    def test_id(self):
        """Tests the attribute id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Tests the attribute created_at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Tests the attribute updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at != new.updated_at)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Won't pass")
    def test_save(self):
        """test if save method works"""
        new = BaseModel()
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)

    def test_BaseModelAttrs(self):
        """Tests the attrs of BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_type(self):
        """Tests for the type"""
        new = BaseModel()
        self.assertTrue(issubclass(new.__class__, BaseModel), True)

    def test_docs(self):
        """Tests for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)


if __name__ == "__main__":
    unittest.main()
