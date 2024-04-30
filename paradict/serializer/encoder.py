import re
import base64
from textwrap import dedent
from collections import namedtuple
from paradict import errors, misc, const, box
from paradict.typeref import TypeRef


Context = namedtuple("Context", ["name", "collection", "indents"])


class Encoder:
    """Convert a Python dictionary object to Paradict text format"""
    def __init__(self, mode=const.DATA_MODE, type_ref=None,
                 skip_comments=False, skip_bin_data=False):
        """
        Init

        [param]
        - mode: either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.
        - type_ref: optional TypeRef object
        - skip_comments: boolean to tell whether comments should be ignored or not
        - skip_bin_data: boolean to tell whether bin data should be ignored or not
        """
        self._mode = mode
        self._type_ref = type_ref if type_ref else TypeRef()
        self._skip_comments = skip_comments
        self._skip_bin_data = skip_bin_data
        self._stack = list()
        self._converters = {"dict": self._encode_dict,
                            "list": self._encode_list,
                            "set": self._encode_set,
                            "obj": self._encode_obj,
                            "grid": self._encode_grid,
                            "bool": self._encode_bool,
                            "str": self._encode_str,
                            "comment": self._encode_comment,
                            "bin": self._encode_bin,
                            "int": self._encode_int,
                            "hex_int": self._encode_hex_int,
                            "oct_int": self._encode_oct_int,
                            "bin_int": self._encode_bin_int,
                            "float": self._encode_float,
                            "complex": self._encode_complex,
                            "datetime": self._encode_datetime,
                            "date": self._encode_date,
                            "time": self._encode_time}

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, val):
        self._mode = val

    @property
    def type_ref(self):
        return self._type_ref

    @type_ref.setter
    def type_ref(self, val):
        self._type_ref = val

    @property
    def skip_comments(self):
        return self._skip_comments

    @skip_comments.setter
    def skip_comments(self, val):
        self._skip_comments = val

    @property
    def skip_bin_data(self):
        return self._skip_bin_data

    @skip_bin_data.setter
    def skip_bin_data(self, val):
        self._skip_bin_data = val

    def encode(self, data):
        """Generator for iteratively encoding data by yielding lines of Paradict text format"""
        data = self._type_ref.adapt(data)
        if type(data) not in self._type_ref.dict_types:
            msg = "The root data structure should be a dict"
            raise errors.Error(msg)
        g = self._encode(data)
        next(g)
        yield from g

    def _encode(self, data, indents=-1):
        if data is None:
            yield from self._encode_null(data, indents)
            return
        datatype = type(data)
        type_name = self._type_ref.check(datatype)
        try:
            converter = self._converters[type_name]
        except KeyError as e:
            msg = "Unknown datatype '{}'".format(datatype)
            raise errors.Error(msg)
        yield from converter(data, indents)

    def _check_key(self, key):
        type_name = self._type_ref.check(type(key))
        if (type_name == "str"
                or (self._mode == const.DATA_MODE
                    and type_name in ("int", "hex_int", "oct_int",
                                      "bin_int", "float", "complex"))):
            pass
        else:
            msg = ("In CONFIG_MODE, a key should be either str or raw"
                   " without whitespace. "
                   "In DATA_MODE, a key should be one of: str, raw, "
                   "int, hex_int, oct_int, bin_int, float, complex.")
            raise errors.Error(msg)
        if type_name == "str":  # TODO
            key = key.replace("\\", "\\\\")
            key = key.replace("\n", "\\n")
            r = '"{}"'.format(key)
        else:
            r = next(self._encode(key))
        # ensure that key doesn't contain whitespace or "=" symbol
        # if CONFIG_MODE is on
        if self._mode == const.CONFIG_MODE:
            r = r.strip("'").strip('"')
            pattern = r'^[a-zA-Z0-9_-]*$'
            if not re.match(pattern, r):
                msg = ("Keys in CONFIG_MODE must contain "
                       "only alphanumeric characters"
                       " (a-z, A-Z, 0-9), underscore and hyphen characters.")
                raise errors.Error(msg)
        # replace newline with
        else:
            r = r.replace("\n", "\\n")
        return r

    def _encode_dict(self, data, indents):
        yield from self._encode_dict_and_obj("dict", data, indents)

    def _encode_obj(self, data, indents=0):
        yield from self._encode_dict_and_obj("obj", data, indents)

    def _encode_list(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + "(list)"
        # iterate list
        for val in data:
            val = self._type_ref.adapt(val)
            # process val as comment if needed
            if type(val) in self._type_ref.comment_types:
                try:
                    yield from self._encode(val, indents+1)
                except errors.CommentSkip as e:
                    pass
                continue
            g = self._encode(val, indents+1)
            val = next(g)
            yield val
            yield from g

    def _encode_set(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + "(set)"
        # iterate set
        for val in data:
            val = self._type_ref.adapt(val)
            valid_types = ("int", "hex_int", "oct_int", "bin_int",
                           "float", "complex", "str", "bin",
                           "datetime", "date", "time", "comment")
            if self._type_ref.check(type(val)) not in valid_types:

                msg = "The set container can contain these types: {}"
                msg = msg.format(", ".join(valid_types))
                raise errors.Error(msg)
            # process val as comment if needed
            if type(val) in self._type_ref.comment_types:
                try:
                    yield from self._encode(val, indents+1)
                except errors.CommentSkip as e:
                    pass
                continue
            g = self._encode(val, indents + 1)
            val = next(g)
            yield val
            yield from g

    def _encode_dict_and_obj(self, tag, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + "({})".format(tag)
        # iterate dict
        for key, val in data.items():
            key, val = self._type_ref.adapt(key), self._type_ref.adapt(val)
            # process key and val as comment if needed
            if type(key) in self._type_ref.comment_id_types \
                    and type(val) in self._type_ref.comment_types:
                try:
                    yield from self._encode(val, indents + 1)
                except errors.CommentSkip as e:
                    pass
                continue
            # process key and val
            key = self._check_key(key)
            sep = ": " if self._mode == const.DATA_MODE else " = "
            g = self._encode(val, indents + 1)
            val = dedent(next(g))
            indent_str = misc.make_indent_str(indents + 1)
            yield "{indent}{key}{sep}{val}".format(indent=indent_str,
                                                   key=key, sep=sep,
                                                   val=val)
            yield from g

    def _encode_grid(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + "(grid)"
        # iterate grid
        n = 0
        rows = list()
        # stringify
        for row in data:
            # check row consistency
            if n and len(row) != n:
                raise errors.Error("Inconsistent grid size")
            else:
                n = len(row)
            # iterate over the row
            cache = list()
            for val in row:
                val = self._type_ref.adapt(val)
                type_name = self._type_ref.check(type(val))
                if type_name not in ("int", "hex_int", "oct_int", "bin_int",
                                     "float", "complex"):
                    msg = "A Grid should be made of numbers only (integer, float, complex)"
                    raise errors.Error(msg)
                g = self._encode(val, indents + 1)
                val = dedent(next(g))
                cache.append(val)
            rows.append(cache)
        pretty_grid = misc.prettify_grid(rows)
        # padding
        for row in pretty_grid:
            line = " ".join(row)
            indent_str = misc.make_indent_str(indents+1)
            yield indent_str + line

    def _encode_null(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + encode_null(data)

    def _encode_bool(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + encode_bool(data)

    def _encode_str(self, data, indents=0):
        #data = data.replace("\\", "\\\\")
        indent_str = misc.make_indent_str(indents)
        if "\n" in data:
            tag = "(raw)" if "\\" in data else "(text)"
            yield indent_str + tag
            indent_str = misc.make_indent_str(indents+1)
            for line in encode_multiline_str(data):
                yield indent_str + line
            yield indent_str + "---"
        else:
            val = encode_str(data)
            yield indent_str + val

    def _encode_bin(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + "(bin)"
        if self._skip_bin_data:
            return
        indent_str = misc.make_indent_str(indents + 1)
        for line in encode_bin(data):
            yield indent_str + line

    def _encode_comment(self, data, indents=0):
        if self._skip_comments:
            raise errors.CommentSkip
        indent_str = misc.make_indent_str(indents)
        for line in data.split("\n"):
            if not line or line.isspace():
                line = "#"
            else:
                line = "# " + line
            yield indent_str + line

    def _encode_int(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        r = encode_int(data)
        if len(r) > 42:
            yield indent_str + "(int)"
            indent_str = misc.make_indent_str(indents + 1)
            for line in misc.make_multiline(r):
                yield indent_str + line
        else:
            yield indent_str + r

    def _encode_hex_int(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        r = encode_hex_int(data)
        if len(r) > 42:
            yield indent_str + "(int)"
            indent_str = misc.make_indent_str(indents + 1)
            for line in misc.make_multiline(r):
                yield indent_str + line
        else:
            yield indent_str + r

    def _encode_oct_int(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        r = encode_oct_int(data)
        if len(r) > 42:
            yield indent_str + "(int)"
            indent_str = misc.make_indent_str(indents + 1)
            for line in misc.make_multiline(r):
                yield indent_str + line
        else:
            yield indent_str + r

    def _encode_bin_int(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        r = encode_bin_int(data)
        if len(r) > 42:
            yield indent_str + "(int)"
            indent_str = misc.make_indent_str(indents + 1)
            for line in misc.make_multiline(r):
                yield indent_str + line
        else:
            yield indent_str + r

    def _encode_float(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        r = encode_float(data)

        if len(r) > 42:
            yield indent_str + "(float)"
            indent_str = misc.make_indent_str(indents + 1)
            for line in misc.make_multiline(r):
                yield indent_str + line
        else:
            yield indent_str + r

    def _encode_complex(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + encode_complex(data)

    def _encode_datetime(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + encode_datetime(data)

    def _encode_date(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + encode_date(data)

    def _encode_time(self, data, indents=0):
        indent_str = misc.make_indent_str(indents)
        yield indent_str + encode_time(data)


def encode_null(val):
    return "null"


def encode_bool(val):
    if val:
        return "true"
    return "false"


def encode_bin(val):
    if not val:
        return list()
    r = base64.b16encode(val)
    s = r.decode("utf-8")
    return misc.prettify_base16(s)


def encode_str(val):
    quote = "'" if "\\" in val else '"'
    # indent_str = misc.make_indent_str(0)
    return "{quote}{data}{quote}".format(data=val, quote=quote)


def encode_multiline_str(val):
    return val.split("\n")


def encode_int(val):
    return misc.tidy_up_int(val, width=3)


def encode_hex_int(val):
    return misc.tidy_up_int(val, width=4)


def encode_oct_int(val):
    return misc.tidy_up_int(val, width=3)


def encode_bin_int(val):
    return misc.tidy_up_int(val, width=4)


def encode_float(val):
    return misc.tidy_up_float(val)


def encode_complex(val):
    real, imag = val.real, val.imag
    #real = int(real) if real.is_integer() else real
    #imag = int(imag) if imag.is_integer() else imag
    # tidy up real part
    if misc.is_whole_number(real):
        tidy_real = misc.tidy_up_int(int(real))
    else:
        tidy_real = misc.tidy_up_float(real)
    # tidy up imaginary part
    if misc.is_whole_number(imag):
        tidy_imag = misc.tidy_up_int(int(imag))
    else:
        tidy_imag = misc.tidy_up_float(imag)
    return "{}{}{}i".format(tidy_real, "" if imag < 0 else "+", tidy_imag)


def encode_datetime(val):
    value = val.isoformat()
    if value.endswith("+00:00"):
        value = value.replace("+00:00", "Z")
    return str(value)


def encode_date(val):
    """Parse date and time with the ISO 8601 format"""
    # date ISO format
    return str(val)


def encode_time(val):
    # time ISO format
    return str(val)
