"""This module exposes the split function that will parse a valid key-value string"""
import re
from paradict import errors, const
from collections import namedtuple


__all__ = ["Info", "split"]


Info = namedtuple("Info", ["key", "val", "sep", "mode"])


def split(val):
    """
    Split a non-empty string into key val.
    The string should follow one of these format:
    - data_mode format: key: value
    - config_mode format: key = value

    [param]
    - val: non-empty string

    [return]
    Return an Info namedtuple made of: key, val, sep, and mode attributes.
    The key and val are strings. The sep is either ":" or "=".
    The mode is either paradict.const.DATA_MODE or paradict.const.CONFIG_MODE.
    Note that if the sep is a colon, it means that the mode is DATA_MODE.
    """
    if not val or not isinstance(val, str):
        msg = "Only non-empty strings can be split"
        raise errors.Error(msg)
    r = _parse(val)
    if not r or len(r) != 3:
        raise errors.Error("Parsing error")
    left, sep, right = r
    key = left.strip().replace(r"\'", "'").replace(r'\"', '"')
    val = right.strip()
    if sep == "=":
        mode = const.CONFIG_MODE
    elif sep == ":":
        mode = const.DATA_MODE
    else:
        raise errors.Error("Missing separator character")
    return Info(key, val, sep, mode)


def _parse(val):
    """regex parse"""
    match_obj = re.fullmatch(KEY_VAL_PATTERN, val)
    groups_list = list()
    if not match_obj:
        return groups_list
    for group in match_obj.groups():
        if group is not None:
            groups_list.append(group)
    return groups_list


# double-quoted key pattern (left side of colon sign)
KEY_PATTERN_1 = r'''^(?<!\\)("[^"](?:[^"]*?(?:\\")*?)+(?<!\\)")\s*'''

# single-quoted key pattern (left side of colon sign)
KEY_PATTERN_2 = r"""^(?<!\\)('[^'](?:[^']*?(?:\\')*?)+(?<!\\)')\s*"""

# unquoted key pattern (left side of colon or equal sign)
KEY_PATTERN_3 = r"""^(.+?)\s*"""

# key pattern for config mode
KEY_PATTERN_4 = r"""^([a-zA-Z0-9_-]*)\s*"""

# value pattern (right side of colon or equal sign)
VALUE_PATTERN = r"""(.*)$"""


# Mode-based key-val patterns
DATA_MODE_PATTERN_1 = KEY_PATTERN_1 + "(:)" + VALUE_PATTERN
DATA_MODE_PATTERN_2 = KEY_PATTERN_2 + "(:)" + VALUE_PATTERN
DATA_MODE_PATTERN_3 = KEY_PATTERN_3 + "(:)" + VALUE_PATTERN
CONFIG_MODE_PATTERN = KEY_PATTERN_4 + "(=)" + VALUE_PATTERN

# Multi-mode key-val pattern
KEY_VAL_PATTERN = "|".join((CONFIG_MODE_PATTERN,
                            DATA_MODE_PATTERN_1,
                            DATA_MODE_PATTERN_2,
                            DATA_MODE_PATTERN_3))
