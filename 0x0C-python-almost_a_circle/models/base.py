#!/usr/bin/python3
"""
base module
"""
import json
import os
import csv
import turtle


class Base:
    """
    base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - constructor
        Args:
            id: object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert to json string
        Args:
            list_dictionaries: list

        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json to a file
        Args:
            cls: the class it self
            list_objs: list of instances
        """
        class_name = cls.__name__
        file_name = f"{class_name}.json"

        if list_objs is None or list_objs == []:
            list_objs = "[]"
        else:
            json_list = []

            for obj in list_objs:
                json_list.append(obj.to_dictionary())

        with open(file_name, mode='w') as file:
            file.write(cls.to_json_string(json_list))

        return json_list

    @staticmethod
    def from_json_string(json_string):
        """
        returns converted json to dic
        Args:
            json_string: json file to convert

        """
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance easily already settled
        Args:
            cls: class to create
            dictionary: attributes values
         """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        file_name = f"{cls.__name__}.json"
        lst = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                data = file.read()
                list_dicts = cls.from_json_string(data)
                for dic in list_dicts:
                    lst.append(cls.create(**dic))
            return lst
