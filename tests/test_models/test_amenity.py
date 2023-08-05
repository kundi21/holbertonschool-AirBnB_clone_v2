#!/usr/bin/python3
"""Module qith tests for Amenity"""

import pep8
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Defining tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.amenity = Amenity()
        self.amenity.name = "an amenity"

    def test_pep8(self):
        """ pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        checking = style.check_files(['models/amenity.py'])
        self.assertEqual(checking.total_errors, 0, "fix pep8")

    def test_name2(self):
        """ the attribute name"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))

    def test_AmenityTypes(self):
        """ attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_type(self):
        """ testing  the type"""
        nre = Amenity()
        self.assertTrue(issubclass(nre.__class__, Amenity), True)


if __name__ == "__main__":
    unittest.main()
