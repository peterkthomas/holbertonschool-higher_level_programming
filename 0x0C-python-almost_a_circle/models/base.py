#!/usr/bin/python3
"""
File: base.py
"""
import json


class Base(object):
    """Base: Definition for the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string represntation to file"""
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as fd:
            if list_objs is None:
                fd.write('[]')
            else:
                fd.write(cls.to_json_string([x.to_dictionary()
                                             for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns list representation"""
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set"""
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        if cls.__name__ == "Square":
            tmp = cls(1)
        cls.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """function that creates obj from file"""
        try:
            filename = cls.__name__ + ".json"
            with open(filename, encoding="utf-8") as fd:
                return cls.create(cls.from_json_string(fd))
        except BaseException:
            return []
