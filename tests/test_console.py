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

if __name__ == '__main__':
    unittest.main()

