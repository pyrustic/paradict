"""Boxes to hold comments, grids, hexadecimal integers, et cetera"""
from paradict import misc
from ustrid import ustrid


class Grid(list):
    """
    Box to hold a grid. A grid is made of numbers and should
    be consistent (rows should be of same size)

    Example:
        # a grid with 2 rows and 3 columns
        my_grid = Grid([(0, 1, 0),
                        (1, 0, 1)])
    """
    pass


class Obj(dict):
    """
    Box to hold an Extension Object. Such objects behave like a dictionary.
    An object builder is passed as argument to the right functions, thus,
    the object is consumed/used to build a new valid data value
    """
    pass


class Raw(str):
    """
    A string defined as Raw doesn't recognize the '\' anti-slash as
    special character (that might be used for unicode codepoint etc)
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


class CommentID(str):
    """
    Box to hold a unique comment id.
    Instantiating this class will generate a new unique string.
    Under the hood, the 'ustrid' library is used.
        CommentID() != CommentID()
    """
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, ustrid())


class Comment(str):
    """Box to hold a comment string"""
    pass
