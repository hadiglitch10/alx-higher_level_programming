#!/usr/bin/python3
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance


    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a_class
    """
    return isinstance(obj, a_class)
