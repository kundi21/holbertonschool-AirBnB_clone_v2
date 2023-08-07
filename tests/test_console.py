#!/usr/bin/python3
"""
Unittests for the console
"""
from typing import Any
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from contextlib import redirect_stdout
import io



class TestConsole(unittest.TestCase):
    """Console tests"""

    @classmethod
    def setUpClass(cls):
        """Set up class test"""
        cls.console = HBNBCommand()
    
    def setUp(self):
        """Set up test"""
        FileStorage.__objects = {}

    def test_quit(self):
        """Test quit"""
        self.assertEqual(self.console.onecmd("quit"), None)

    def test_EOF(self):
        """Test EOF"""
        self.assertEqual(self.console.onecmd("EOF"), None)
    
class TestYourClass(unittest.TestCase):
    def test_create(self):
        state_name = "California"
        
        with io.StringIO() as state_output, redirect_stdout(state_output):
            self.console.onecmd(f"create State name='{state_name}'")
            state_id = state_output.getvalue()

        with io.StringIO() as city_output, redirect_stdout(city_output):
            self.console.onecmd(
                "create City state_id='{}' name='San_Francisco_is_super_cool'".format(state_id))
            city_id = city_output.getvalue()

        print("State ID: {}, City ID: {}".format(state_id, city_id))
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

