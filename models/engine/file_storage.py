#!/usr/bin/python3
"""Defines A FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State


class FileStorage():
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    Attributes:
        __file_path (string): path to the JSON file.
        __objects (dictionary): empty but will store all objects
                        by <class name>.id.
        classes_dict (dictionary): A dictionary of all the classes.
    """
    __file_path = "file.json"
    __objects = {}
    classes_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                    "City": City, "Review": Review, "State": State}

    def all(self, cls=None):
        """Returns the dictionary __objects
        Returns the list of objects of one type of class. Example below with
        State - it’s an optional filtering"""
        if cls is not None:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (object): object to write.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            data = {k: v.to_dict() for k, v in self.__objects.items()}
            file.write(json.dumps(data))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                for k, v in data.items():
                    new_obj = self.classes_dict[v['__class__']](**v)
                    self.__objects[k] = new_obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """ call reload() method for deserializing the
        JSON file to objects """
        self.reload()
