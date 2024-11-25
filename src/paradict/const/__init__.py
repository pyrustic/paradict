# general constants
from enum import unique, Enum


@unique
class Datatype(Enum):
    DICT = 1
    LIST = 2
    SET = 3
    OBJ = 4
    GRID = 5
    BOOL = 6
    STR = 7
    BIN = 8
    INT = 9
    FLOAT = 10
    COMPLEX = 11
    DATE = 12
    TIME = 13
    DATETIME = 14


# Indent
INDENT_WIDTH = 4  # Four spaces
INDENT_STR = " " * INDENT_WIDTH

# Paradict Epoch: 2020-01-01T00:00:00Z
COVID_YEAR = 2020

# modes for Textual Paradict
DATA_MODE = "d"
CONFIG_MODE = "c"
