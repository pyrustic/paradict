import re
import datetime
import base64
from paradict import errors, misc, const, kv, box
from paradict.typeref import TypeRef
from paradict.queue.txt_queue import TxtQueue


class Decoder:
    """Class to convert some textual Paradict data into a Python dict"""
    def __init__(self, *, type_ref=None, receiver=None, obj_builder=None,
                 skip_comments=False):
        """
        Init

        [parameters]
        - type_ref: optional TypeRef object
        - receiver: callback function that will be called at the end of conversion.
        This callback function accepts the Decoder instance as argument
        - obj_builder: function that accepts a paradict.box.Obj container and
        returns a fresh new Python object
        - skip_comments: boolean to tell whether comments should be ignored or not
        """
        self._type_ref = type_ref if type_ref else TypeRef()
        self._receiver = receiver
        self._obj_builder = obj_builder
        self._skip_comments = skip_comments
        # data
        self._data = dict()
        # feedable
        self._feedable = True
        # misc
        self._queue = TxtQueue()
        self._stack = list()
        self._lineno = 1
        self._active = False
        self._converters = (self._decode_null, self._decode_bool,
                            self._decode_str, self._decode_complex_number,
                            self._decode_int, self._decode_float,
                            self._decode_date, self._decode_time,
                            self._decode_datetime)

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

    def feed(self, s):
        """
        Feed the decoder engine with some string.
        The string might represent a line in the textual Paradict data,
        or an arbitrary length of characters.

        Note: it is very important to make sure that each line is ended
        by a "\n" newline character

        Check the paradict.decode function to see an example of
        how to use this class
        """
        if not self._feedable:
            return False
        self._queue.put(s)
        for line in self._queue.get():
            line = line.rstrip("\n")
            if line.rstrip() == "===":  # END
                self._cleanup_stack(0)
                self._stack = list()
                self._active = False
                if self._receiver:
                    self._receiver(self)
                return True
            if not self._active:
                self._data = self._type_ref.dict_type()
                #root_context = Context("dict", self._data, 0)
                #self._stack.append(root_context)
                self._update_stack("dict", self._data, 0)
                self._active = True
            self._process(line)
        return True

    def _process(self, line):
        line = self._check_line(line)
        # process line
        try:
            self._interpret(line)
        except Exception as e:
            msg = "Error on line {}: {}{}\n--> {}"
            str_e = str(e)
            str_e = ": " + str_e if str_e else str_e
            msg = msg.format(self._lineno, type(e).__name__, str_e, line)
            raise type(e)(msg)
        self._lineno += 1

    def _interpret(self, line):
        #if not self._stack:
        #    return
        context = self._get_context()
        name = context.name
        container = context.container
        if name in ("dict", "list", "set", "obj"):
            self._update_context(line)
        elif name in ("bin", "raw", "text", "grid"):
            container.append(line)
        else:
            msg = "Unknown tag '{}'. Expected dict, list, set, obj, grid, bin, text, or raw."
            msg = msg.format(name)
            raise errors.Error(msg)

    def _update_context(self, line):
        context = self._get_context()
        name = context.name
        updaters = {"dict": self._update_dict_container,
                    "list": self._update_list_container,
                    "set": self._update_set_container,
                    "obj": self._update_obj_container}
        updater = updaters.get(name)
        if not updater:
            raise errors.Error
        updater(context, line)

    def _update_dict_container(self, context, line):
        container = context.container
        indents = context.indents
        # process whitespaces
        if not line or line.isspace():
            pass
        # process comments
        elif line.startswith("#"):
            if self._skip_comments:
                return
            comment_id = box.CommentID()
            container[comment_id] = box.Comment(line.strip("# "))
        # process key value
        else:
            info = kv.split(line)
            key, val, mode = info.key, info.val, info.mode
            key = self._check_key(key, mode)
            value = self._decode_value(val)
            tag = self._check_multiline_tag(val)
            if tag in ("dict", "list", "set"):
                container[key] = value
                context.cached_dict_key = None
                self._update_stack(tag, value, indents + 1)
            elif tag in ("grid", "obj", "bin", "raw", "text"):
                context.cached_dict_key = key
                self._update_stack(tag, value, indents + 1)
            else:
                container[key] = value

    def _update_obj_container(self, context, line):
        return self._update_dict_container(context, line)

    def _update_list_container(self, context, line):
        container = context.container
        indents = context.indents
        # process whitespaces
        if not line or line.isspace():
            pass
        # process comments
        elif line.startswith("#"):
            if self._skip_comments:
                return
            comment = box.Comment(line.strip("# "))
            container.append(comment)

        # process key value
        else:
            value = self._decode_value(line)
            tag = self._check_multiline_tag(line)
            if tag in ("dict", "list", "set"):
                container.append(value)
                self._update_stack(tag, value, indents + 1)
            elif tag in ("grid", "obj", "bin", "raw", "text"):
                self._update_stack(tag, value, indents + 1)
            else:
                container.append(value)

    def _update_set_container(self, context, line):
        container = context.container
        indents = context.indents
        # process whitespaces
        if not line or line.isspace():
            pass
        # process comments
        elif line.startswith("#"):
            if self._skip_comments:
                return
            comment = box.Comment(line.strip("# "))
            container.add(comment)
        # process key value
        else:
            value = self._decode_value(line)
            tag = self._check_multiline_tag(line)
            if tag in ("bin", "raw", "text"):
                self._update_stack(tag, value, indents + 1)
            elif tag in ("dict", "list", "set", "grid", "obj"):
                msg = "Set can't contain any of: dict, list, set, grid, obj"
                raise errors.Error(msg)
            else:
                container.add(value)

    def _check_line(self, line):
        """Check the validity of the indent in the line
        Returns the indent-less version of line"""
        if not line:
            return line
        context = self._get_context()
        strict = False if context.name in ("bin", "raw", "text") else True
        indents = misc.count_indents(line, strict)
        # same indent
        if indents == context.indents:
            pass
        # lower indent
        elif indents < context.indents:
            self._cleanup_stack(indents)
        # exaggerated forward indent
        elif indents > context.indents and strict:
            if context.indents == 0:
                msg = "Expected {} indent at line {}:{}"
            else:
                msg = "Expected {} or less indents at line {}:{}"
            msg = msg.format(context.indents, self._lineno, line)
            raise errors.IndentError(msg)
        return misc.dedent(line, context.indents)

    def _check_key(self, key, mode):
        if mode == const.CONFIG_MODE:
            pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
            if not re.match(pattern, key):
                msg = ("Keys in CONFIG_MODE must contain "
                       "only strict alphanumeric characters"
                       " (a-z, A-Z, 0-9) and underscore characters."
                       " Also, they cannot start with a number.")
                raise errors.Error(msg)
            key = "'{}'".format(key)
        key = self._decode_value(key)
        if self._type_ref.check(type(key)) in ("str", "raw",
                                               "int", "hex_int",
                                               "oct_int", "bin_int",
                                               "float", "complex"):
            return key
        # exception
        if mode == const.DATA_MODE:
            msg = ("In DATA_MODE, a key should be one of: str, raw, "
                   "int, hex_int, oct_int, bin_int, float, complex.")
        else:
            msg = ("In CONFIG_MODE, a key should be either str or raw"
                   " without whitespace. ")
        raise errors.Error(msg)

    def _check_multiline_tag(self, value):
        if not value.startswith("(") or not value.endswith(")"):
            return None
        value = value.strip("()")
        if value not in ("bin", "dict", "list", "set",
                         "raw", "text", "obj", "grid"):
            return None
        return value

    def _update_stack(self, container_name,
                      container, indents):
        new_context = Context(container_name, container, indents)
        self._stack.append(new_context)

    def _cleanup_stack(self, indents):
        if not self._stack:
            return
        while True:
            if len(self._stack) == 1:
                break
            context = self._get_context()
            parent_context = self._get_parent_context()
            if indents >= context.indents:
                break
            # bin
            if context.name == "bin":
                self._consume_bin_block(parent_context, context)
            # raw
            elif context.name == "raw":
                self._consume_raw_block(parent_context, context)
            # text
            elif context.name == "text":
                self._consume_text_block(parent_context, context)
            # obj
            elif context.name == "obj":
                self._consume_obj_block(parent_context, context)
            # obj
            elif context.name == "grid":
                self._consume_grid_block(parent_context, context)
            # delete the latest context
            del self._stack[-1]

    def _consume_bin_block(self, parent_context, context):
        bin_block = context.container
        val = list()
        for line in bin_block:
            if not line or line.isspace():
                continue
            for char in line:
                if not char.isspace():
                    val.append(char)
        #value = [item.strip() for item in bin_block if item]
        value = "".join(val)
        bin_data = self._decode_bin(value)
        #default_bin_type = self._bin_type
        #if type(bin_data) is not default_bin_type:
        #    bin_data = default_bin_type(bin_data)
        self._update_parent_context(parent_context, bin_data)

    def _consume_raw_block(self, parent_context, context):
        # concatenate text lines
        block = misc.strip_block_extra_space(context.container)
        #text = self._decode_raw(raw_block)
        text = "'{}'".format(block)
        text = self._decode_str(text)
        self._update_parent_context(parent_context, text)

    def _consume_text_block(self, parent_context, context):
        # concatenate text lines
        block = misc.strip_block_extra_space(context.container)
        #text = self._decode_text(text_block)
        text = '"{}"'.format(block)
        text = self._decode_str(text)
        self._update_parent_context(parent_context, text)

    def _consume_obj_block(self, parent_context, context):
        container = context.container
        if self._obj_builder:
            container = self._obj_builder(container)
        self._update_parent_context(parent_context, container)

    def _consume_grid_block(self, parent_context, context):
        container = context.container
        row_size = 0
        grid = list()
        # turn lines into rows
        for line in container:
            temp_row = line.split()
            if row_size == 0:
                row_size = len(temp_row)
            elif len(temp_row) != row_size:
                msg = "Inconsistent grid"
                raise errors.Error(msg)
            row = list()
            for item in temp_row:
                val = self._decode_value(item)
                dtype = self._type_ref.check(type(val))
                if dtype not in ("int", "float", "complex"):
                    msg = "A grid should be built with int, float, or complex numbers"
                    raise errors.Error(msg)
                row.append(val)
            grid.append(tuple(row))
        # update parent context
        grid = self._type_ref.grid_type(grid)
        self._update_parent_context(parent_context, grid)

    def _update_parent_context(self, parent_context, data):
        if parent_context.name in ("dict", "obj"):
            key = parent_context.cached_dict_key
            parent_context.container[key] = data
        elif parent_context.name == "list":
            parent_context.container.append(data)
        elif parent_context.name == "set":
            parent_context.container.add(data)
        else:
            msg = "Invalid parent name '{}'"
            msg = msg.format(parent_context.name)
            raise errors.Error(msg)

    def _add_whitespace_to_parent_context(self, parent_context):
        if self._skip_comments:
            return
        whitespace = box.Comment()
        if parent_context.name == "dict":
            whitespace_id = box.CommentID()
            parent_context.container[whitespace_id] = whitespace
        elif parent_context.name == "list":
            parent_context.container[-1] = whitespace
        else:
            msg = "Invalid parent name '{}'"
            msg = msg.format(parent_context.name)
            raise errors.Error(msg)

    def _get_context(self):
        try:
            return self._stack[-1]
        except IndexError as e:
            msg = "Inconsistent stack state"
            raise errors.Error(msg)

    def _get_parent_context(self):
        try:
            return self._stack[-2]
        except IndexError as e:
            msg = "Inconsistent stack state"
            raise errors.Error(msg)

    def _decode_value(self, value):
        value = value.strip()
        container = self._decode_container(value)
        if container is not None:
            return container
        # scalars and co.  (note that the order of items matters here)
        for p in self._converters:
            try:
                result = p(value)
            except Exception as e:
                continue
            else:
                return result
        raise errors.Error("Conversion error")

    def _decode_container(self, val):
        if not val.startswith("(") or not val.endswith(")"):
            return None
        # bin
        if val == "(bin)":
            return list()
        # dict
        if val == "(dict)":
            return self._type_ref.dict_type()
        # list
        if val == "(list)":
            return self._type_ref.list_type()
        # set
        if val == "(set)":
            return self._type_ref.set_type()
        # obj
        if val == "(obj)":
            return self._type_ref.obj_type()
        # raw
        if val == "(raw)":
            return list()
        # text
        if val == "(text)":
            return list()
        # grid
        if val == "(grid)":
            return list()
        msg = ("Expected one of these containers: (bin), "
               "(dict), (list), (set), (raw), (text), (obj), (grid)")
        raise errors.Error(msg)

    def _decode_null(self, val):
        return decode_null(val)

    def _decode_bool(self, val):
        r = decode_bool(val)
        return self._type_ref.bool_type(r)

    def _decode_bin(self, val):
        r = base64.b16decode(val, casefold=True)
        r = r if self._type_ref.bin_type is bytes else self._type_ref.bin_type(r)
        return r

    def _decode_str(self, val):
        r = decode_str(val)
        r = r if self._type_ref.str_type is str else self._type_ref.str_type(r)
        return r

    def _decode_complex_number(self, val):
        r = decode_complex(val)
        r = r if self._type_ref.complex_type is complex else self._type_ref.complex_type(r)
        return r

    def _decode_int(self, val):
        r = decode_int(val)
        r = r if self._type_ref.int_type is int else self._type_ref.int_type(r)
        return r

    def _decode_float(self, val):
        r = decode_float(val)
        r = r if self._type_ref.float_type is float else self._type_ref.float_type(r)
        return r

    def _decode_date(self, val):
        r = decode_date(val)
        r = r if self._type_ref.date_type is datetime.date else self._type_ref.date_type(r)
        return r

    def _decode_time(self, val):
        r = decode_time(val)
        r = r if self._type_ref.time_type is datetime.time else self._type_ref.time_type(r)
        return r

    def _decode_datetime(self, val):
        r = decode_datetime(val)
        r = r if self._type_ref.datetime_type is datetime.datetime else self._type_ref.datetime_type(r)
        return r


class Context:
    def __init__(self, name, container, indents):
        self._name = name
        self._container = container
        self._indents = indents
        self._cached_dict_key = None
        self._is_dict_key_cached = False

    @property
    def name(self):
        return self._name

    @property
    def container(self):
        return self._container

    @property
    def indents(self):
        return self._indents

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


# === Decoders ===


def decode_bin(val):
    # list of strings
    val = "".join(val)
    return base64.standard_b64decode(val)


def decode_bool(val):
    val = val.lower()
    if val == "true":
        return bool(1)
    elif val == "false":
        return bool(0)
    raise errors.Error


def decode_complex(val):
    if val.endswith("i"):
        val = val.replace(" ", "")
        val = val.rstrip("i") + "j"
        return complex(val)
    raise errors.Error


def decode_date(val):
    """Parse date and time with the ISO 8601 format"""
    # date ISO format
    return datetime.date.fromisoformat(val)


def decode_datetime(val):
    # datetime (2023-03-13T09:10:42Z)
    if val.endswith("Z"):
        val += "+00:00"
    return datetime.datetime.fromisoformat(val)


def decode_float(val):
    val = val.lower()
    if "e" in val or "." in val:
        return float(val)
    raise errors.Error


def decode_int(val):
    v = val.lstrip("+-")
    # hexadecimal
    if v.startswith("0x"):
        val = int(val, 16)
        return box.HexInt(val)
    # octal
    if v.startswith("0o"):
        val = int(val, 8)
        return box.OctInt(val)
    # binary
    if v.startswith("0b"):
        val = int(val, 2)
        return box.BinInt(val)
    # default base 10
    return int(val)


def decode_null(val):
    val = val.lower()
    if val == "null":
        return None
    raise errors.Error


def decode_str(val):
    if val.startswith('"') and val.endswith('"'):
        return misc.decode_unicode(val[1:-1])
    if val.startswith("'") and val.endswith("'"):
        return box.Raw(val[1:-1])
    raise errors.Error("Conversion error")
    #val = misc.replace_newlines(val)
    #val = misc.replace_tabs(val)


def decode_time(val):
    if val.endswith("Z"):
        val += "+00:00"
    # time ISO format
    return datetime.time.fromisoformat(val)
