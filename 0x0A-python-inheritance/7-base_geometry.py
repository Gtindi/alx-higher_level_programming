#!/usr/bin/python3

"""This module contains the `BaseGeometry` class."""


class BaseGeometry:
    """The base class of all `Geometry`"""

    def area(self):
        """Computes the `area` of a `Geometry`"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates a value.

        Args:
            name(str): The `name` of the `value`
            value(int): The `value` to be stored with the given `name`
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
