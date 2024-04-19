#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
import os
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    
    def test_creat_for_errors(self):
        """
        Checks for create command errors. If class name
        is missing or does'nt exist
        """
        with patch("sys.stdout", new=StrigIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd("create fake_class")
                self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_create_command_validity(self):
        """ Would test the create command"""
        with patch("sys.stdout", newStringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            bmodel = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            usr = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            t_state = f.getvalue().strip()
        
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            plc = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            citi = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Review")
            rev = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            ameni = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Basemodel")
            self.assertIn(bmodel, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            self.assertIn(usr, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertIn(t_state, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Amenity")
            self.assertIn(ameni, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            self.assertIn(plc, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all City")
            self.assertIn(citi, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Review")
            self.assertIn(rev, f.getvalue())
            
    def test_create_command_with_kwargs(self):
        """would run check on the create command with kwargs"""
        with patch("sys.stdout", new=StringIO()) as f:
            call = (f'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            self.HBNB.onecmd(call)
            plc = f.getvalue().strip()
        
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(plc, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My house'", output)
            self.assertIn("'number_rooms: '4'", output)
            self.assertIn("'latitude': '37.77'", output)
            self.assertIn("'longitude': '43.434'", output)
            

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")