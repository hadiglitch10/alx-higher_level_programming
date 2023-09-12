#!/usr/bin/python3
"""
lookup - returns the list of available attributes and methods of an object
@obj: object
Return: list object
"""


def lookup(obj):
    """
    Return list of attributes and methods

    :param obj: the object to look in
    :return: list
    """
    return dir(obj)
