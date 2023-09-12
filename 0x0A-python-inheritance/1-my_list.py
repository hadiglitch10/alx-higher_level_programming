#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """
    child of list
    """
    def print_sorted(self):
        """
        print sorted list

        """
        print(sorted(self))
