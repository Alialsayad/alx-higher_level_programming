#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """
    Custom MyList class
    """
    def print_sorted(self):
        """
        Method for printing sorted list
        """
        print(sorted(self))
