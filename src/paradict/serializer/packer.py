import math
from paradict.typeref import TypeRef
from paradict import tags
from paradict.const import Datatype
from paradict.tags.mappings import SIZE_TO_PINT, \
    SIZE_TO_NINT, LETTER_TO_TAG, SIZE_TO_STR
from paradict import errors, misc, xtypes

__all__ = ["Packer"]


class Packer:
    """
    Class to convert some binary Python dict into Paradict binary format
    """
    def __init__(self, type_ref=None, dict_only=False, auto_index=False):
        """
        Init

        [param]
        - type_ref: optional TypeRef object
        - dict_only: boolean to enforce dict as root
        """
        self._type_ref = type_ref if type_ref else TypeRef()
        self._dict_only = dict_only
        self._auto_index = auto_index
        self._index_dict = dict()
        self._dict_counter = 0
        self._is_dict = False
        self._field_size = 0
        self._converters = {Datatype.DICT: self._pack_dict,
                            Datatype.LIST: self._pack_list,
                            Datatype.SET: self._pack_set,
                            Datatype.OBJ: self._pack_obj,
                            Datatype.GRID: self._pack_grid,
                            Datatype.BOOL: self._pack_bool,
                            Datatype.STR: self._pack_str,
                            Datatype.BIN: self._pack_bin,
                            Datatype.INT: self._pack_int,
                            Datatype.FLOAT: self._pack_float,
                            Datatype.COMPLEX: self._pack_complex,
                            Datatype.DATETIME: self._pack_datetime,
                            Datatype.DATE: self._pack_date,
                            Datatype.TIME: self._pack_time}

    @property
    def type_ref(self):
        return self._type_ref

    @type_ref.setter
    def type_ref(self, val):
        self._type_ref = val

    @property
    def dict_only(self):
        return self._dict_only

    @property
    def auto_index(self):
        return self._auto_index

    @property
    def index_dict(self):
        """Index dictionary for when the root container is a dict"""
        return self._index_dict

    def pack(self, data):
        """Generator for iteratively packing data by yielding bytes datum forged in
         Paradict binary format"""
        # clear variables
        self._dict_counter = 0
        self._field_size = 0
        self._index_dict = dict()
        # pack data
        data = self._type_ref.adapt(data)
        self._is_dict = type(data) in self._type_ref.dict_types
        if self._dict_only and not self._is_dict:
            msg = "The root data structure should be a dict"
            raise errors.Error(msg)
        yield from self._pack(data)

    def _pack(self, data):
        if data is None:
            yield from self._pack_null(data)
            return
        datatype = type(data)
        type_name = self._type_ref.check(datatype)
        try:
            r = self._converters[type_name](data)
        except KeyError as e:
            msg = "Unknown datatype '{}'".format(datatype)
            raise errors.Error(msg)
        yield from r

    def _pack_dict(self, data):
        if not data:
            yield tags.DICT_EMPTY
            return
        self._dict_counter += 1
        # encode dict head
        yield tags.DICT
        # iterate dict
        for key, val in data.items():
            key, val = self._type_ref.adapt(key), self._type_ref.adapt(val)
            if self._auto_index and self._is_dict and self._dict_counter == 1:
                key_size = val_size = 0
                for r in self._pack(key):
                    key_size += len(r)
                    yield r
                for r in self._pack(val):
                    val_size += len(r)
                    yield r
                start = key_size + 1 if self._field_size == 0 else self._field_size + 1
                self._field_size += key_size + val_size
                stop = self._field_size + 1
                self._index_dict[key] = slice(start, stop)
            else:
                yield from self._pack(key)
                yield from self._pack(val)
        self._dict_counter -= 1
        # encode dict tail
        yield tags.END

    def _pack_list(self, data):
        if not data:
            yield tags.LIST_EMPTY
            return
        # encode list head
        yield tags.LIST
        # iterate list
        for item in data:
            item = self._type_ref.adapt(item)
            yield from self._pack(item)
        # encode list tail
        yield tags.END

    def _pack_set(self, data):
        if not data:
            yield tags.SET_EMPTY
            return
        # encode set head
        yield tags.SET
        # iterate set
        for item in data:
            item = self._type_ref.adapt(item)
            if self._type_ref.check(type(item)) in (Datatype.DICT,
                                                    Datatype.LIST,
                                                    Datatype.SET,
                                                    Datatype.OBJ,
                                                    Datatype.GRID):
                msg = "The set container can't contain a dict, list, set, obj, or grid"
                raise errors.Error(msg)
            yield from self._pack(item)
        # encode set tail
        yield tags.END

    def _pack_obj(self, data):
        if not data:
            yield tags.OBJ_EMPTY
            return
        # encode obj head
        yield tags.OBJ
        # iterate obj
        for key, val in data.items():
            key, val = self._type_ref.adapt(key), self._type_ref.adapt(val)
            yield from self._pack(key)
            yield from self._pack(val)
        # encode obj tail
        yield tags.END

    def _pack_grid(self, data):
        if not data:
            yield tags.GRID_EMPTY
            return
        # encode grid head
        yield tags.GRID
        is_first_row = True
        row_size = 0
        # iterate grid
        for row in data:
            row = self._type_ref.adapt(row)
            if not row_size:
                row_size = len(row)
            if len(row) != row_size:
                raise errors.Error("Inconsistent grid")
            if type(row) not in self._type_ref.list_types:
                msg = "Unknown row type {}".format(type(row))
                raise errors.Error(msg)
            # iterate over the contents of the row
            for item in row:
                item = self._type_ref.adapt(item)
                typename = self._type_ref.check(type(item))
                if typename not in (Datatype.INT, Datatype.FLOAT, Datatype.COMPLEX):
                    msg = "A grid should be built with int, float, or complex numbers"
                    raise errors.Error(msg)
                # process int, float
                if typename == Datatype.INT:
                    yield from self._pack_int(item)
                elif typename == Datatype.FLOAT:
                    yield from self._pack_float(item)
                elif typename == Datatype.COMPLEX:
                    yield from self._pack_complex(item)
            # add grid div if this is the first row
            if is_first_row and len(data) > 1:
                yield tags.GRID_DIV
                is_first_row = False
        # encode grid tail
        yield tags.END

    def _pack_null(self, data):
        yield tags.NULL

    def _pack_bool(self, data):
        yield pack_bool(data)

    def _pack_str(self, data):
        yield pack_str(data)

    def _pack_bin(self, data):
        yield pack_bin(data)

    def _pack_int(self, data):
        if isinstance(data, xtypes.HexInt):
            yield from self._pack_hex_int(data)
            return
        if isinstance(data, xtypes.BinInt):
            yield from self._pack_bin_int(data)
            return
        if isinstance(data, xtypes.OctInt):
            yield from self._pack_oct_int(data)
            return
        yield pack_int(data)

    def _pack_hex_int(self, data):
        yield pack_hex_int(data)

    def _pack_oct_int(self, data):
        yield pack_oct_int(data)

    def _pack_bin_int(self, data):
        yield pack_bin_int(data)

    def _pack_float(self, data):
        yield pack_float(data)

    def _pack_complex(self, data):
        yield pack_complex(data)

    def _pack_datetime(self, data):
        yield pack_datetime(data)

    def _pack_date(self, data):
        yield pack_date(data)

    def _pack_time(self, data):
        yield pack_time(data)


def pack_bool(val):
    if val:
        return tags.BOOL_TRUE
    else:
        return tags.BOOL_FALSE


def pack_str(val):
    if not val:
        return tags.STR_EMPTY
    # const letters
    if len(val) == 1:
        try:
            return LETTER_TO_TAG[val]
        except KeyError as e:
            pass
    data = val.encode("utf-8")
    # 8 to 64 bits
    size = len(data)
    try:
        tag_byte = SIZE_TO_STR[size]
    except KeyError as e:
        pass
    else:
        return misc.forge_bin(tag_byte, data)
    # short
    if size <= 2**8:
        return misc.forge_bin(tags.STR_SHORT, size-1, data)
    # medium
    if size <= 2**(8*2):
        return misc.forge_bin(tags.STR_MEDIUM, size-1, data)
    # long
    if size <= 2**(8*3):
        return misc.forge_bin(tags.STR_LONG, size-1, data)
    # big
    if size <= 2**(8*4):
        return misc.forge_bin(tags.STR_BIG, size-1, data)
    # heavy
    if size <= 2**(8*5):
        return misc.forge_bin(tags.STR_HEAVY, size-1, data)
    # oveeeer heavy
    msg = "The string to pack is over heavy !"
    raise errors.Error(msg)


def pack_bin(val):
    if not val:
        return tags.BIN_EMPTY
    # 8 to 64 bits
    size = len(val)
    # short
    if size <= 2**8:
        return misc.forge_bin(tags.BIN_SHORT, size-1, val)
    # medium
    if size <= 2**(8*2):
        return misc.forge_bin(tags.BIN_MEDIUM, size-1, val)
    # long
    if size <= 2**(8*3):
        return misc.forge_bin(tags.BIN_LONG, size-1, val)
    # big
    if size <= 2**(8*4):
        return misc.forge_bin(tags.BIN_BIG, size-1, val)
    # heavy
    if size <= 2**(8*5):
        return misc.forge_bin(tags.BIN_HEAVY, size-1, val)
    # oveeeer heavy
    msg = "The bin to pack is over heavy !"
    raise errors.Error(msg)


def pack_int(val):
    # yield integer
    if val >= 0:
        return pack_pint(val)
    else:
        return pack_nint(val)


def pack_hex_int(val):
    leading_zeros = misc.count_leading_zeros(val)
    if leading_zeros == 0:
        return misc.forge_bin(tags.RADIX_HEX, pack_int(val))
    return misc.forge_bin(tags.RADIX_HEX_EXT,
                          pack_int(leading_zeros),
                          pack_int(val))


def pack_oct_int(val):
    leading_zeros = misc.count_leading_zeros(val)
    if leading_zeros == 0:
        return misc.forge_bin(tags.RADIX_OCT, pack_int(val))
    return misc.forge_bin(tags.RADIX_OCT_EXT,
                          pack_int(leading_zeros),
                          pack_int(val))


def pack_bin_int(val):
    leading_zeros = misc.count_leading_zeros(val)
    if leading_zeros == 0:
        return misc.forge_bin(tags.RADIX_BIN, pack_int(val))
    return misc.forge_bin(tags.RADIX_BIN_EXT,
                          pack_int(leading_zeros),
                          pack_int(val))


def pack_pint(val):
    size = misc.calc_uint_bytes(val)  # size is the n of bytes
    if val < 100:
        tag = bytes([tags.CONST_0[0] + val])
        return misc.forge_bin(tag)
    if size <= 8:
        tag = SIZE_TO_PINT.get(size)
        return misc.forge_bin(tag, val)
    if size <= 256:
        tag = tags.PINT_BIG
        return misc.forge_bin(tag, size-1, val)
    if size <= 65536:
        tag = tags.PINT_HEAVY
        return misc.forge_bin(tag, size-1, val)
    msg = "Too large positive integer"
    raise errors.Error(msg)


def pack_nint(val):
    val = abs(val)
    size = misc.calc_uint_bytes(val)  # size is the n of bytes
    if size <= 8:
        tag = SIZE_TO_NINT.get(size)
        return misc.forge_bin(tag, val)
    if size <= 256:
        tag = tags.NINT_BIG
        return misc.forge_bin(tag, size-1, val)
    if size <= 65536:
        tag = tags.NINT_HEAVY
        return misc.forge_bin(tag, size-1, val)
    msg = "Too large negative integer"
    raise errors.Error(msg)


def pack_float(val):
    # process special float values
    if val == 0:
        if math.copysign(1, val) == -1:
            return misc.forge_bin(tags.FLOAT_MISC, tags.CHAR_Z)
        else:
            return _pack_regular_float(val)
    elif val == float("+inf"):
        return misc.forge_bin(tags.FLOAT_MISC, tags.CHAR_X)
    elif val == float("-inf"):
        return misc.forge_bin(tags.FLOAT_MISC, tags.CHAR_Y)
    elif val == float("NaN"):
        return misc.forge_bin(tags.FLOAT_MISC, tags.CHAR_N)
    else:
        return _pack_regular_float(val)


def _pack_regular_float(val):
    info = misc.split_float(val)
    exponent = int(info.exponent)
    left_significand = int(info.sign + info.left_significand)
    right_significand = int(info.right_significand)
    leading_zeros = misc.count_leading_zeros(info.right_significand)
    if right_significand == 0:
        r = _pack_float_1(left_significand, exponent)
    elif right_significand != 0 and leading_zeros == 0:
        r = _pack_float_2(left_significand, right_significand, exponent)
    elif right_significand != 0 and leading_zeros != 0:
        r = _pack_float_3(left_significand, leading_zeros,
                          right_significand, exponent)
    else:
        msg = "Inconsistent float value"
        raise errors.Error(msg)
    return r


def _pack_float_1(left_significand, exponent):
    if exponent == 0:
        r = misc.forge_bin(tags.FLOAT_1,
                           pack_int(left_significand))
    else:
        r = misc.forge_bin(tags.FLOAT_1_EXT,
                           pack_int(left_significand),
                           pack_int(exponent))
    return r


def _pack_float_2(left_significand, right_significand, exponent):
    if exponent == 0:
        r = misc.forge_bin(tags.FLOAT_2,
                           pack_int(left_significand),
                           pack_int(right_significand))
    else:
        r = misc.forge_bin(tags.FLOAT_2_EXT,
                           pack_int(left_significand),
                           pack_int(right_significand),
                           pack_int(exponent))
    return r


def _pack_float_3(left_significand, leading_zeros, right_significand, exponent):
    if exponent == 0:
        r = misc.forge_bin(tags.FLOAT_3,
                           pack_int(left_significand),
                           pack_int(leading_zeros),
                           pack_int(right_significand))
    else:
        r = misc.forge_bin(tags.FLOAT_3_EXT,
                           pack_int(left_significand),
                           pack_int(leading_zeros),
                           pack_int(right_significand),
                           pack_int(exponent))
    return r


def pack_complex(val):
    real, imag = val.real, val.imag
    real = int(real) if misc.is_whole_number(real) else real
    imag = int(imag) if misc.is_whole_number(imag) else imag
    packed_real = pack_int(real) if isinstance(real, int) else pack_float(real)
    packed_imag = pack_int(imag) if isinstance(imag, int) else pack_float(imag)
    return misc.forge_bin(tags.COMPLEX,
                          packed_real, packed_imag)


def pack_datetime(val):
    year_delta, ns_delta, trailing_zeros, tz = misc.deconstruct_datetime(val)
    if tz is None:
        r = misc.forge_bin(tags.DATETIME,
                           pack_int(year_delta),
                           pack_int(ns_delta),
                           pack_int(trailing_zeros))
    else:
        r = misc.forge_bin(tags.DATETIME_EXT,
                           pack_int(year_delta),
                           pack_int(ns_delta),
                           pack_int(trailing_zeros),
                           pack_int(tz))
    return r


def pack_date(val):
    year_delta, days_delta = misc.deconstruct_date(val)
    r = misc.forge_bin(tags.DATE,
                       pack_int(year_delta),
                       pack_int(days_delta))
    return r


def pack_time(val):
    ns_delta, trailing_zeros, tz = misc.deconstruct_time(val)
    if tz is None:
        r = misc.forge_bin(tags.TIME,
                           pack_int(ns_delta),
                           pack_int(trailing_zeros))
    else:
        r = misc.forge_bin(tags.TIME_EXT,
                           pack_int(ns_delta),
                           pack_int(trailing_zeros),
                           pack_int(tz))
    return r
