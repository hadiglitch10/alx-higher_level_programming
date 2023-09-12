#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    Checks object belongs to a class that inherited from the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :return: True if obj's class is a subclass of a_class; False otherwise.
    """
    return issubclass(type(obj), a_class)
