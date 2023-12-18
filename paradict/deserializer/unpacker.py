import datetime
from paradict import tags
from paradict.tags.misc import ALPHABET
from paradict.typeref import TypeRef
from paradict import errors
from paradict.queue.bin_queue import BinQueue
from paradict import misc, box


class Unpacker:
    """Class to convert some binary Paradict data into a Python dict"""

    def __init__(self, type_ref=None, receiver=None, obj_builder=None,
                 skip_comments=False):
        """
        Init

        [parameters]
        - type_ref: optional TypeRef object
        - receiver: callback function that will be called at the end of conversion.
        This callback function accepts the Unpacker instance as argument
        - obj_builder: function that accepts a paradict.box.Obj container and
        returns a fresh new Python object
        - skip_comments: boolean to tell whether comments should be ignored or not
        """
        self._type_ref = type_ref if type_ref else TypeRef()
        self._receiver = receiver
        self._obj_builder = obj_builder
        self._skip_comments = skip_comments
        self._buffer = bytearray()
        self._index = 0
        self._queue = BinQueue()
        self._feedable = True
        self._stack = list()
        self._data = None
        self._block_on = False
        self._block_count = 0
        # flags
        self._as_raw_str = False
        self._as_comment_str = False
        # byte count for exception message
        self._byte_count = 0

    @property
    def data(self):
        if self._stack:
            context = self._stack[0]
            return context.container
        return self._data

    @property
    def feedable(self):
        return self._feedable

    @feedable.setter
    def feedable(self, val):
        self._feedable = val

    @property
    def type_ref(self):
        return self._type_ref

    @type_ref.setter
    def type_ref(self, val):
        self._type_ref = val

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, val):
        self._receiver = val

    @property
    def obj_builder(self):
        return self._obj_builder

    @obj_builder.setter
    def obj_builder(self, val):
        self._obj_builder = val

    @property
    def skip_comments(self):
        return self._skip_comments

    @skip_comments.setter
    def skip_comments(self, val):
        self._skip_comments = val

    @property
    def queue(self):
        return self._queue

    @queue.setter
    def queue(self, val):
        self._queue = val

    def feed(self, raw):
        """Feed in arbitrary chunks of data"""
        if not self._feedable:
            return False
        self._queue.put(raw)
        for tag, payload in self._queue.get():
            if tag == tags.NOP:
                continue
            self._process(tag, payload)
        return True

    def _process(self, tag, payload):
        # ensure that root data structure is a dict
        if not self._stack and tag not in (tags.DICT,
                                           tags.DICT_EMPTY):
            msg = "The root data structure should be a dict"
            raise errors.Error(msg)
        # interpret tag
        try:
            self._interpret(tag, payload)
        except Exception as e:
            msg = "Error at byte index {}: {}{}"
            str_e = str(e)
            str_e = ": " + str_e if str_e else str_e
            msg = msg.format(self._byte_count, type(e).__name__, str_e)
            raise type(e)(msg)
        self._byte_count += 1 + len(payload)
        # consume block
        while self._consume_block():
            pass

    def _interpret(self, tag, payload):
        if tag in (tags.DICT_EMPTY, tags.LIST_EMPTY,
                   tags.SET_EMPTY):
            self._create_context(tag)
            self._remove_context()
        elif tag in (tags.DICT,
                     tags.LIST,
                     tags.SET,
                     tags.GRID,
                     tags.OBJ,
                     tags.COMPLEX,
                     tags.FLOAT_1, tags.FLOAT_2, tags.FLOAT_3,
                     tags.FLOAT_1_EXT, tags.FLOAT_2_EXT, tags.FLOAT_3_EXT,
                     tags.DATETIME, tags.DATETIME_EXT,
                     tags.DATE,
                     tags.TIME, tags.TIME_EXT,
                     tags.RADIX_HEX, tags.RADIX_HEX_EXT,
                     tags.RADIX_OCT, tags.RADIX_OCT_EXT,
                     tags.RADIX_BIN, tags.RADIX_BIN_EXT):
            self._create_context(tag)
        # closing container
        elif tag == tags.END:
            self._cleanup_stack()
        # process empty grid
        elif tag == tags.GRID_EMPTY:
            self._update_context(self._unpack_grid(tag))
        # process empty obj
        elif tag == tags.OBJ_EMPTY:
            self._update_context(self._unpack_obj(tag))
        # flags
        elif tag in (tags.RAW_STR, tags.COMMENT_STR):
            self._update_flags(tag)
        # process payload
        else:
            try:
                data = self._unpack_payload(tag, payload)
            except errors.CommentSkip as e:
                pass
            else:
                self._update_context(data)

    def _create_context(self, tag):
        if tag in (tags.DICT, tags.DICT_EMPTY,
                   tags.LIST, tags.LIST_EMPTY,
                   tags.SET, tags.SET_EMPTY):
            self._create_alpha_context(tag)
        else:
            self._create_beta_context(tag)

    def _create_alpha_context(self, tag):
        if tag in (tags.DICT, tags.DICT_EMPTY):
            datatype = "dict"
            new_container = self._type_ref.dict_type()
        elif tag in (tags.LIST, tags.LIST_EMPTY):
            datatype = "list"
            new_container = self._type_ref.list_type()
        elif tag in (tags.SET, tags.SET_EMPTY):
            datatype = "set"
            new_container = self._type_ref.set_type()
        else:
            msg = "Unknown container tag '{}'".format(tag)
            raise errors.Error(msg)
        if len(self._stack) != 0:
            self._update_context(new_container)
        context = Context(tag, datatype, new_container)
        self._stack.append(context)
        self._data = None

    def _create_beta_context(self, tag):
        if tag == tags.OBJ:
            context = Context(tag, "obj", box.Obj())
        else:
            context = Context(tag, "list", list())
        self._stack.append(context)
        self._block_on = True
        self._block_count += 1

    def _get_context(self):
        try:
            return self._stack[-1]
        except IndexError as e:
            msg = "Inconsistent stack state"
            raise errors.Error(msg)

    def _update_context(self, data):
        context = self._stack[-1]
        is_dict_key_cached = context.is_dict_key_cached
        cached_dict_key = context.cached_dict_key
        # Dict and obj
        if context.datatype == "dict":
            if is_dict_key_cached:
                context.container[cached_dict_key] = data
                context.is_dict_key_cached, context.cached_dict_key = False, None
            else:
                context.is_dict_key_cached, context.cached_dict_key = True, data
        # List
        elif context.datatype == "list":
            context.container.append(data)
        # Set
        elif context.datatype == "set":
            context.container.add(data)
        # Obj
        elif context.datatype == "obj":
            if is_dict_key_cached:
                context.container[cached_dict_key] = data
                context.is_dict_key_cached, context.cached_dict_key = False, None
            else:
                context.is_dict_key_cached, context.cached_dict_key = True, data

    def _remove_context(self):
        if not self._stack:
            return
        context = self._stack[-1]
        data = context.container
        if len(self._stack) == 1:
            self._data = data
            self._stack = list()
            if self._receiver:
                self._receiver(self)
        else:
            del self._stack[-1]

    def _consume_block(self):
        if not self._block_on:
            return False
        context = self._get_context()
        tag, container = context.tag, context.container
        n = len(container)
        if tag == tags.COMPLEX and n == 2:
            data = self._unpack_complex(tag, container)
        elif tag == tags.RADIX_HEX and n == 1:
            data = self._unpack_hex_int(tag, container)
        elif tag == tags.RADIX_HEX_EXT and n == 2:
            data = self._unpack_hex_int(tag, container)
        elif tag == tags.RADIX_OCT and n == 1:
            data = self._unpack_oct_int(tag, container)
        elif tag == tags.RADIX_OCT_EXT and n == 2:
            data = self._unpack_oct_int(tag, container)
        elif tag == tags.RADIX_BIN and n == 1:
            data = self._unpack_bin_int(tag, container)
        elif tag == tags.RADIX_BIN_EXT and n == 2:
            data = self._unpack_bin_int(tag, container)
        elif tag == tags.FLOAT_1 and n == 1:
            data = self._unpack_float(tag, container)
        elif tag == tags.FLOAT_1_EXT and n == 2:
            data = self._unpack_float(tag, container)
        elif tag == tags.FLOAT_2 and n == 2:
            data = self._unpack_float(tag, container)
        elif tag == tags.FLOAT_2_EXT and n == 3:
            data = self._unpack_float(tag, container)
        elif tag == tags.FLOAT_3 and n == 3:
            data = self._unpack_float(tag, container)
        elif tag == tags.FLOAT_3_EXT and n == 4:
            data = self._unpack_float(tag, container)
        elif tag == tags.DATETIME and n == 3:
            data = self._unpack_datetime(tag, container)
        elif tag == tags.DATETIME_EXT and n == 4:
            data = self._unpack_datetime(tag, container)
        elif tag == tags.DATE and n == 2:
            data = self._unpack_date(tag, container)
        elif tag == tags.TIME and n == 2:
            data = self._unpack_time(tag, container)
        elif tag == tags.TIME_EXT and n == 3:
            data = self._unpack_time(tag, container)
        else:
            return False
        # the next line is safe, i.e., if stack were empty,
        # self._get_context() would've raised an exception
        self._remove_block()
        self._update_context(data)
        return True

    def _remove_block(self):
        del self._stack[-1]
        self._block_count -= 1
        if self._block_count == 0:
            self._block_on = False

    def _update_flags(self, tag):
        if tag == tags.RAW_STR:
            self._as_raw_str = True
        elif tag == tags.COMMENT_STR:
            self._as_comment_str = True

    def _cleanup_stack(self):
        context = self._get_context()
        if context.tag not in (tags.GRID, tags.OBJ):
            self._remove_context()
            return
        if context.tag == tags.GRID:
            data = self._unpack_grid(context.tag, context.container)
        elif context.tag == tags.OBJ:
            data = self._unpack_obj(context.tag, context.container)
        else:
            msg = "END tag is only allowed to end containers, grids, and objs"
            raise errors.Error(msg)
        self._remove_block()
        self._update_context(data)

    def _unpack_payload(self, tag, payload=None):
        # unpack null
        if tag == tags.NULL:
            if self._as_comment_str:
                self._as_comment_str = False
                return self._unpack_comment_id(tags.COMMENT_STR, None)
            return self._unpack_null(tag, payload)
        # boolean
        elif tag in (tags.BOOL_TRUE, tags.BOOL_FALSE):
            return self._unpack_bool(tag, payload)
        # unpack integer
        elif (tags.PINT_8 <= tag <= tags.NINT_HEAVY
              or tags.CONST_0 <= tag <= tags.CONST_99):
            return self._unpack_int(tag, payload)
        # float misc
        elif tags.FLOAT_NAN <= tag <= tags.FLOAT_INF_2:
            return self._unpack_float_misc(tag, payload)
        # unpack string
        elif (tags.STR_8 <= tag <= tags.STR_HEAVY
              or tags.CHAR_A <= tag <= tags.CHAR_UP_Z):
            if self._as_raw_str:
                return self._unpack_raw(tag, payload)
            elif self._as_comment_str:
                if self._skip_comments:
                    raise errors.CommentSkip
                return self._unpack_comment(tag, payload)
            else:
                return self._unpack_str(tag, payload)
        # unpack bin
        elif tags.BIN_EMPTY <= tag <= tags.BIN_HEAVY:
            return self._unpack_bin(tag, payload)
        # grid's DIV flag
        elif tag == tags.GRID_DIV:
            return GridDiv

    def _unpack_null(self, tag, payload=None):
        return None

    def _unpack_bool(self, tag, payload=None):
        if tag == tags.BOOL_TRUE:
            return self._type_ref.bool_type(True)
        elif tag == tags.BOOL_FALSE:
            return self._type_ref.bool_type(False)

    def _unpack_int(self, tag, payload=None):
        if payload is None:
            msg = "Payload missing"
            raise errors.Error(msg)
        r = unpack_int(tag, payload)
        r = r if self._type_ref.int_type is int else self._type_ref.int_type(r)
        return r

    def _unpack_hex_int(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if tag == tags.RADIX_HEX:
            r = payload_list[0]
        elif tag == tags.RADIX_HEX_EXT:
            leading_zeros, x = payload_list
            r = misc.add_leading_zeros(x, leading_zeros)
        else:
            msg = "Malformed hex_int block"
            raise errors.Error(msg)
        return self._type_ref.hex_int_type(r)

    def _unpack_oct_int(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if tag == tags.RADIX_OCT:
            r = payload_list[0]
        elif tag == tags.RADIX_OCT_EXT:
            leading_zeros, x = payload_list
            r = misc.add_leading_zeros(x, leading_zeros)
        else:
            msg = "Malformed oct_int block"
            raise errors.Error(msg)
        return self._type_ref.oct_int_type(r)

    def _unpack_bin_int(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if tag == tags.RADIX_BIN:
            r = payload_list[0]
        elif tag == tags.RADIX_BIN_EXT:
            leading_zeros, x = payload_list
            r = misc.add_leading_zeros(x, leading_zeros)
        else:
            msg = "Malformed bin_int block"
            raise errors.Error(msg)
        return self._type_ref.bin_int_type(r)

    def _unpack_float(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if tag == tags.FLOAT_1:
            significand = payload_list[0]
            return self._type_ref.float_type(significand)
        elif tag == tags.FLOAT_1_EXT:
            significand, exponent = payload_list
            x = "{}E{}".format(significand, exponent)
            return self._type_ref.float_type(x)
        elif tag == tags.FLOAT_2:
            left_significand, right_significand = payload_list
            x = "{}.{}".format(left_significand, right_significand)
            return self._type_ref.float_type(x)
        elif tag == tags.FLOAT_2_EXT:
            left_significand, right_significand, exponent = payload_list
            x = "{}.{}E{}".format(left_significand, right_significand,
                                  exponent)
            return self._type_ref.float_type(x)
        elif tag == tags.FLOAT_3:
            left_significand, leading_zeros, right_significand = payload_list
            leading_zeros = "0" * leading_zeros
            x = "{}.{}{}".format(left_significand, leading_zeros,
                                 right_significand)
            return self._type_ref.float_type(x)
        elif tag == tags.FLOAT_3_EXT:
            left_significand, leading_zeros, right_significand, exponent = payload_list
            leading_zeros = "0" * leading_zeros
            x = "{}.{}{}E{}".format(left_significand, leading_zeros,
                                    right_significand, exponent)
            return self._type_ref.float_type(x)
        else:
            msg = "Malformed float block"
            raise errors.Error(msg)

    def _unpack_float_misc(self, tag, payload=None):
        if tag == tags.FLOAT_NAN:
            return self._type_ref.float_type("NaN")
        elif tag == tags.FLOAT_INF_1:
            return self._type_ref.float_type("+inf")
        elif tag == tags.FLOAT_INF_2:
            return self._type_ref.float_type("-inf")
        elif tag == tags.FLOAT_ZERO_1:
            return self._type_ref.float_type("0.0")
        elif tag == tags.FLOAT_ZERO_2:
            return self._type_ref.float_type("-0.0")

    def _unpack_complex(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if len(payload_list) == 2:
            real, imag = payload_list
            return self._type_ref.complex_type(real, imag)
        else:
            msg = "Malformed complex number"
            raise errors.Error(msg)

    def _unpack_bin(self, tag, payload=None):
        if payload is None:
            msg = "Payload missing"
            raise errors.Error(msg)
        r = unpack_bin(tag, payload)
        r = r if self._type_ref.bin_type is bytes else self._type_ref.bin_type(r)
        return r

    def _unpack_str(self, tag, payload=None):
        if payload is None:
            msg = "Payload missing"
            raise errors.Error(msg)
        r = unpack_str(tag, payload)
        r = r if self._type_ref.str_type is str else self._type_ref.str_type(r)
        return r

    def _unpack_raw(self, tag, payload=None):
        if payload is None:
            msg = "Payload missing"
            raise errors.Error(msg)
        self._as_raw_str = False
        r = self._unpack_str(tag, payload)
        return self._type_ref.raw_type(r)

    def _unpack_comment_id(self, tag, payload=None):
        return self._type_ref.comment_id_type()

    def _unpack_comment(self, tag, payload=None):
        if payload is None:
            msg = "Payload missing"
            raise errors.Error(msg)
        self._as_comment_str = False
        r = self._unpack_str(tag, payload)
        return self._type_ref.comment_type(r)

    def _unpack_obj(self, tag, payload_obj=None):
        if tag == tags.OBJ_EMPTY:
            return self._type_ref.obj_type()
        if payload_obj is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if self._obj_builder:
            return self._obj_builder(payload_obj)
        if type(payload_obj) == self._type_ref.obj_type:
            return payload_obj
        return self._type_ref.obj_type(payload_obj)

    def _unpack_grid(self, tag, payload_list=None):
        if tag == tags.GRID_EMPTY:
            return self._type_ref.grid_type()
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        row = list()
        row_size = 0
        grid = list()
        for item in payload_list:
            if item is GridDiv:
                row_size = len(row)
            else:
                if row_size and len(row) == row_size:
                    grid.append(tuple(row))
                    row = list()
                row.append(item)
        if row:
            if row_size and len(row) != row_size:
                msg = "Inconsistent grid"
                raise errors.Error(msg)
            grid.append(tuple(row))
        # check type validity
        for row in grid:
            for item in row:
                dtype = self._type_ref.check(type(item))
                if dtype not in ("int", "float", "complex"):
                    msg = "A grid should be built with int, float, or complex numbers"
                    raise errors.Error(msg)
        return self._type_ref.grid_type(grid)

    def _unpack_datetime(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if len(payload_list) == 3:  # year, nanoseconds, trailing zeros
            year_delta, ns_delta, trailing_zeros = payload_list
            tz_minutes = None
        elif len(payload_list) == 4:  # year, nanoseconds, trailing zeros, timezone
            year_delta, ns_delta, trailing_zeros, tz_minutes = payload_list
        else:
            msg = "Inconsistent datetime"
            raise errors.Error(msg)
        r = misc.construct_datetime(year_delta, ns_delta, trailing_zeros, tz_minutes)
        r = r if self._type_ref.datetime_type is datetime.datetime\
            else self._type_ref.datetime_type(r)
        return r

    def _unpack_date(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if len(payload_list) == 2:  # year_delta, day_delta
            year_delta, day_delta = payload_list
        else:
            msg = "Inconsistent date"
            raise errors.Error(msg)
        r = misc.construct_date(year_delta, day_delta)
        r = r if self._type_ref.date_type is datetime.date \
            else self._type_ref.date_type(r)
        return r

    def _unpack_time(self, tag, payload_list=None):
        if payload_list is None:
            msg = "Payloads missing"
            raise errors.Error(msg)
        if len(payload_list) == 2:  # nanoseconds, trailing zeros
            ns_delta, trailing_zeros = payload_list
            tz_minutes = None
        elif len(payload_list) == 3:  # nanoseconds, trailing zeros, timezone
            ns_delta, trailing_zeros, tz_minutes = payload_list
        else:
            msg = "Inconsistent datetime"
            raise errors.Error(msg)
        r = misc.construct_time(ns_delta, trailing_zeros, tz_minutes)
        r = r if self._type_ref.time_type is datetime.time \
            else self._type_ref.time_type(r)
        return r


class Context:
    def __init__(self, tag, datatype, container):
        self._tag = tag
        self._datatype = datatype
        self._container = container
        self._cached_dict_key = None
        self._is_dict_key_cached = False

    @property
    def tag(self):
        return self._tag

    @property
    def datatype(self):
        return self._datatype

    @property
    def container(self):
        return self._container

    @property
    def cached_dict_key(self):
        return self._cached_dict_key

    @cached_dict_key.setter
    def cached_dict_key(self, val):
        self._cached_dict_key = val

    @property
    def is_dict_key_cached(self):
        return self._is_dict_key_cached

    @is_dict_key_cached.setter
    def is_dict_key_cached(self, val):
        self._is_dict_key_cached = val


class GridDiv:
    pass


def unpack_int(tag, payload):
    if (tags.PINT_8 <= tag <= tags.PINT_HEAVY
            or tags.CONST_0 <= tag <= tags.CONST_99):
        r = unpack_pint(tag, payload)
    # unpack negative integer
    elif tags.NINT_8 <= tag <= tags.NINT_HEAVY:
        r = unpack_nint(tag, payload)
    else:
        msg = "Unknown integer tag byte {}".format(tag)
        raise errors.Error(msg)
    return r


def unpack_str(tag, payload):
    if tag == tags.STR_EMPTY:
        return str()
    elif tags.CHAR_A <= tag <= tags.CHAR_UP_Z:
        for k, v in ALPHABET.items():
            if v == tag:
                return k
    else:
        return payload.decode("utf-8")


def unpack_bin(tag, payload):
    if tag == tags.BIN_EMPTY:
        return b''
    else:
        return bytes(payload)


def unpack_pint(tag, payload):
    if tags.CONST_0 <= tag <= tags.CONST_99:
        return 99 - (tags.CONST_99[0] - tag[0])
    return int.from_bytes(payload, "little", signed=False)


def unpack_nint(tag, payload):
    return -int.from_bytes(payload, "little", signed=False)
