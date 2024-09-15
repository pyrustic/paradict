"""Datatype enum"""
from enum import Enum, unique

# None isn't a datatype. None represents the absence of value.
# Therefore, it isn't part of the Datatype enum.
# Yet it is well handled in this library.


@unique
class Datatype(Enum):
    DICT = 1
    LIST = 2
    SET = 3
    OBJ = 4
    BIN = 5
    BIN_INT = 6
    BOOL = 7
    COMMENT = 8
    COMMENT_ID = 9
    COMPLEX = 10
    DATE = 11
    DATETIME = 12
    FLOAT = 13
    GRID = 14
    HEX_INT = 15
    INT = 16
    OCT_INT = 17
    STR = 18
    TIME = 19
