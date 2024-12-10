"""Boxes to hold grids, hexadecimal integers, et cetera"""
from collections import UserList, UserDict
from paradict import misc


__all__ = ["Grid", "Obj", "HexInt", "OctInt", "BinInt"]


class Grid(UserList):
    """
    Box to hold a grid. A grid is made of numbers and should
    be consistent (rows should be of same size)

    Example:
    ```
    # a grid with 2 rows and 3 columns
    my_grid = Grid([(0, 1, 0),
                    (1, 0, 1)])
    ```
    """
    pass


class Obj(UserDict):
    """
    Box to hold an Extension Object. Such objects behave like a dictionary.
    An object builder is passed as argument to the right functions, thus,
    the object is consumed/used to build a new valid data value
    """
    pass


class HexInt(int):
    """Box to hold hexadecimal integer"""

    def __new__(cls, x):
        width = 0
        if isinstance(x, str):
            parts = misc.split_int(x)
            if parts.prefix == "0x":
                width = len(parts.leading_zeros) + len(parts.val)
        instance = super().__new__(cls, str(x), base=misc.get_int_base(x))
        x = hex(instance)
        x = misc.left_pad_int(x, width) if width else x
        instance.__x = misc.tidy_up_int(x, width=4)
        return instance

    def __str__(self):
        return self.__x


class OctInt(int):
    """Box to hold octal integer"""

    def __new__(cls, x):
        width = 0
        if isinstance(x, str):
            parts = misc.split_int(x)
            if parts.prefix == "0o":
                width = len(parts.leading_zeros) + len(parts.val)
        instance = super().__new__(cls, str(x), base=misc.get_int_base(x))
        x = oct(instance)
        x = misc.left_pad_int(x, width) if width else x
        instance.__x = misc.tidy_up_int(x, width=3)
        return instance

    def __str__(self):
        return self.__x


class BinInt(int):
    """Box to hold binary integer"""

    def __new__(cls, x):
        width = 0
        if isinstance(x, str):
            parts = misc.split_int(x)
            if parts.prefix == "0b":
                width = len(parts.leading_zeros) + len(parts.val)
        instance = super().__new__(cls, str(x), base=misc.get_int_base(x))
        x = bin(instance)
        x = misc.left_pad_int(x, width) if width else x
        instance.__x = misc.tidy_up_int(x, width=4)
        return instance

    def __str__(self):
        return self.__x
