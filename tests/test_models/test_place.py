#!/usr/bin/python3
"""Tests for the Place  module."""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test for the Place class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_class_attributes(self):
        """Test the class attributes"""
        place1 = Place()
        place2 = Place("welcome", "hi", "think")
        key = f"{type(place1).__name__}.{place1.id}"
        self.assertIsInstance(place1.name, str)
        self.assertIn(key, storage.all())
        self.assertEqual(place2.name, "")
        self.assertIsInstance(place1.name, str)
        self.assertIsInstance(place1.user_id, str)
        self.assertIsInstance(place1.city_id, str)
        self.assertIsInstance(place1.description, str)
        self.assertIsInstance(place1.number_bathrooms, int)
        self.assertIsInstance(place1.number_rooms, int)
        self.assertIsInstance(place1.price_by_night, int)
        self.assertIsInstance(place1.max_guest, int)
        self.assertIsInstance(place1.longitude, float)
        self.assertIsInstance(place1.latitude, float)
        self.assertIsInstance(place1.amenity_ids, list)

    def test_initialization(self):
        """Test Place instances"""
        place1 = Place()
        place2 = Place(**place1.to_dict())
        self.assertIsInstance(place1.id, str)
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)
        self.assertEqual(place1.updated_at, place2.updated_at)

    def test_str_method(self):
        """Test the str method"""
        place1 = Place()
        string = f"[{type(place1).__name__}] ({place1.id}) {place1.__dict__}"
        self.assertEqual(place1.__str__(), string)

    def test_save_method(self):
        """Test the save method"""
        place1 = Place()
        prev_update = place1.updated_at
        place1.save()
        self.assertNotEqual(place1.updated_at, prev_update)

    def test_todict_method(self):
        """Test the to_dict method"""
        place1 = Place()
        place2 = Place(**place1.to_dict())
        place_dict = place2.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], type(place2).__name__)
        self.assertIn('created_at', place_dict.keys())
        self.assertIn('updated_at', place_dict.keys())
        self.assertNotEqual(place1, place2)


if __name__ == "__main__":
    unittest.main()
