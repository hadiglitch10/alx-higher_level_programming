#!/usr/bin/python3
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    Returns true if instance

    :param obj: obj to check
    :param a_class: class to check
    :return: true if yes false if no
    """
    return type(obj) is a_class
