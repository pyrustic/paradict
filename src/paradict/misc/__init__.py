"""Private miscellaneous functions and classes."""
import os
import os.path
import math
import datetime
from collections import namedtuple
from paradict import errors, const


__all__ = ["forge_bin", "stringify_bin"]


# TODO: update this module (write/correct docstrings, etc), and write tests

IntParts = namedtuple("IntParts", ["sign", "prefix", "leading_zeros", "val"])
FloatParts = namedtuple("FloatParts", ["sign", "left_significand",
                                       "right_significand", "exponent"])


def make_indent_str(indents):
    """The type of 'indents' is int !"""
    return const.INDENT_STR * indents


def forge_bin(*items):
    """items are int, bytes, bytearrays, or Nones, returns a bytearray"""
    # items are integers
    cache = bytearray()
    for item in items:
        # Skip null value
        if item is None:
            continue
        # process item
        if isinstance(item, int):
            if item < 0:
                raise errors.Error("Negative integer isn't allowed")
            n = calc_uint_bytes(item)
            item = item.to_bytes(n, "little", signed=False)
        elif isinstance(item, (bytes, bytearray)):
            if not item:
                continue
        else:
            msg = "The forge_bin func only accepts ints, bytes and bytearrays as items"
            raise errors.Error(msg)
        cache.extend(item)
    return cache


def stringify_bin(b, offset=0, width=None, spaced=False):
    """Good for debug. Stringify some binary data"""
    cache = list()
    for x in b:
        h = hex(x)[2:]
        if len(h) != 2:
            h = "0" + h
        h = r"\x" + h
        cache.append(h)
    space = " " if spaced else ""
    width = width + offset if width else len(b)
    return space.join(cache[offset:width])


def prettify_grid(grid):
    """prettify grids, returns a list that can be iterated like this:
    for row in result:
        print("  ".join(row))"""
    r = list()
    for col in zip(*grid):
        cache = list()
        n = 0
        # stringifying
        for row in col:
            row = str(row)
            if len(row) > n:
                n = len(row)
            cache.append(row)
        # padding
        for i, row in enumerate(cache):
            if len(row) < n:
                row += (" "*(n-len(row)))
                cache[i] = row
        r.append(cache)
    return list(zip(*r))


def prettify_base16(s):
    """Prettify base16 string. Returns a list of strings, each string representing
        a line of 16 bytes"""
    return make_multiline(s, group_size=2, row_size=16)


def split_relative_path(path):
    path = path.strip("/")
    if path.startswith("./"):
        path = path[2:]
    return path.split("/")


def store_attachment(attachment, directory):
    basename = gen_attachment_name(directory)
    filename = os.path.join(directory, basename)
    ensure_parent_dir(filename)
    with open(filename, "wb") as file:
        file.write(attachment)
    return basename


def gen_attachment_name(directory):
    i = 1
    while True:
        basename = str(i)
        filename = os.path.join(directory, basename)
        if not os.path.exists(filename):
            break
        i += 1
    return basename


def ensure_parent_dir(path):
    """Make sure that parent dir exists (create it if isn't yet created)"""
    parent = os.path.dirname(path)
    try:
        os.makedirs(parent)
    except FileExistsError as e:
        pass


def make_multiline(s, group_size=0, row_size=42):
    group_size = 0 if group_size <= 0 else group_size
    row_size = 42 if row_size <= 0 else row_size
    result = list()
    row = list()
    group = list()
    spacing = " " if group_size else ""
    for char in s:
        if group_size:
            group.append(char)
            if len(group) == group_size:
                row.append("".join(group))
                group = list()
        else:
            row.append(char)
        if len(row) == row_size:
            result.append(spacing.join(row))
            row = list()
    if row:
        result.append(spacing.join(row))
    return result


def strip_block_extra_space(block):
    """
    This function is useful for textual Paradict's text and raw.
    It strips extra space out from text/raw block
    which is either a list of strings or a string.
    Return a string.
    """
    three_dashes = "---"
    end_of_block = "\n" + three_dashes
    if not isinstance(block, str):
        block = "\n".join(block)
    if block == three_dashes:
        return ""
    block = block.rstrip()
    x = len(end_of_block)
    if block.endswith(end_of_block):
        return block[0:-x]
    return block


def calc_uint_bytes(x):
    """Return the number of bytes needed for a given integer"""
    if x == 0:
        return 1
    return math.ceil(x.bit_length() / 8)


def deconstruct_datetime(dt):
    years = dt.year - const.COVID_YEAR
    tz = None
    if dt.tzinfo is not None:
        tz = dt.tzinfo
    if years >= 0:
        xdt = datetime.datetime(year=dt.year, month=1, day=1,
                                hour=0, minute=0, second=0,
                                microsecond=0, tzinfo=tz)
    else:
        xdt = datetime.datetime(year=dt.year, month=12, day=31,
                                hour=23, minute=59, second=59,
                                microsecond=999999, tzinfo=tz)
    ns = (abs(dt - xdt) // datetime.timedelta(microseconds=1)) * 1000
    str_ns = str(ns)
    str_ns_stripped = str_ns if str_ns == "0" else str_ns.rstrip("0")
    lite_ns = int(str_ns_stripped)
    trailing_zeros = len(str_ns) - len(str_ns_stripped)
    tz_minutes = None
    if dt.tzinfo:
        tz_minutes = dt.utcoffset() // datetime.timedelta(minutes=1)
    return years, lite_ns, trailing_zeros, tz_minutes


def construct_datetime(year_delta, ns_delta, trailing_zeros, tz_minutes=None):
    if tz_minutes is None:
        tz = None
    else:
        tz = datetime.timezone(datetime.timedelta(minutes=tz_minutes))
    year = const.COVID_YEAR + year_delta
    ns_str = str(ns_delta) + ("0" * trailing_zeros)
    if len(ns_str) <= 3:
        ms = 0
    else:
        ms = int(ns_str[:-3])
    if year_delta >= 0:
        dt = datetime.datetime(year=year, month=1, day=1, tzinfo=tz)
    else:
        dt = datetime.datetime(year=year, month=12, day=31, hour=23,
                               minute=59, second=59, microsecond=999999,
                               tzinfo=tz)
        ms = -ms
    return dt + datetime.timedelta(microseconds=ms)


def deconstruct_date(d):
    years = d.year - const.COVID_YEAR
    if years >= 0:
        xd = datetime.date(year=d.year, month=1, day=1)
    else:
        xd = datetime.date(year=d.year, month=12, day=31)
    days = (abs(d - xd) // datetime.timedelta(days=1))
    return years, days


def construct_date(year_delta, days_delta):
    year = const.COVID_YEAR + year_delta
    if year_delta >= 0:
        dt = datetime.date(year=year, month=1, day=1)
    else:
        dt = datetime.date(year=year, month=12, day=31)
        days_delta = -days_delta
    return dt + datetime.timedelta(days=days_delta)


def deconstruct_time(t):
    val = datetime.datetime(year=const.COVID_YEAR, month=1, day=1,
                            hour=t.hour, minute=t.minute,
                            second=t.second, microsecond=t.microsecond,
                            tzinfo=t.tzinfo)
    _, ns_delta, trailing_zeros, tz = deconstruct_datetime(val)
    return ns_delta, trailing_zeros, tz


def construct_time(ns_delta, trailing_zeros, tz_minutes=None):
    dt = construct_datetime(0, ns_delta, trailing_zeros, tz_minutes=tz_minutes)
    return datetime.time(hour=dt.hour, minute=dt.minute, second=dt.second,
                         microsecond=dt.microsecond, tzinfo=dt.tzinfo)


def count_indents(line, strict=True):
    i = 0
    for char in line:
        if char == " ":
            i += 1
            continue
        break
    x = i / const.INDENT_WIDTH
    y = int(x)
    if strict and x > y:
        raise errors.IndentError
    return y


def dedent(line, indents=1):
    x = indents * const.INDENT_WIDTH
    y = 0
    for i, char in enumerate(line):
        if char == " ":
            y += 1
        else:
            break
    if y == 0:
        return line
    return line[x:] if x<= y else line[y:]


def decode_unicode(text):
    """Take in input some string that might have Unicode escape sequences.
    Output the same string with Unicode escape sequences converted into
    the actual characters that they represent"""
    return text.encode("latin-1", "backslashreplace").decode("unicode-escape")


def encode_unicode(text, codec="latin-1"):  # TODO: why it isn't used ?
    """Convert a string into another where non-latin characters are
    replaced with Unicode escape sequences"""
    return text.encode(codec, "backslashreplace").decode(codec)


def get_int_base(val):
    if not isinstance(val, str):
        return 10
    parts = split_int(val)
    if parts.prefix == "0x":
        return 16
    elif parts.prefix == "0o":
        return 8
    elif parts.prefix == "0b":
        return 2
    return 10


def count_leading_zeros(val):
    parts = split_int(val)
    return len(parts.leading_zeros)


def left_pad_int(val, width):
    parts = split_int(val)
    width = 0 if width < len(parts.val) else width
    nz = width - len(parts.val) if width else 0
    leading_zeros = nz*"0"
    return parts.sign + parts.prefix + leading_zeros + parts.val


def add_leading_zeros(val, n):
    parts = split_int(val)
    leading_zeros = n * "0" if n else ""
    return parts.sign + parts.prefix + leading_zeros + parts.val


def split_int(val):
    val = val if isinstance(val, str) else str(val)
    val = val.replace("_", "")
    if val == "":
        raise errors.Error("Missing value")
    # process sign
    sign = ""
    if val.startswith("-") or val.startswith("+"):
        sign, val = val[0], val[1:]
    # process prefix
    prefix = val[0:2]
    if prefix in ("0x", "0o", "0b"):
        val = val[2:]
    else:
        prefix = ""
    # count leading zeros
    n = _count_leading_zeros(val)
    val = val.lstrip("0")
    val = "0" if not val else val
    leading_zeros = "0"*n
    return IntParts(sign, prefix, leading_zeros, val)


def split_float(s):
    """Parse a float number (string or decimal.Decimal or float), returns
    an instance of this namedtuple:
    FloatParts = namedtuple("FloatParts", ["sign", "left_significand", "right_significand", "exponent"])"""
    s = _prepare_float(s)
    # Split s at the exponent separator
    parts = s.split("E", 1)
    significand = parts[0]
    exponent = parts[1] if len(parts) == 2 else "0"
    exponent = exponent.lstrip("+")
    #exponent = (exponent[1:] if exponent and exponent[0] == "+"
    #            else exponent)
    # Split significand at the dot separator
    sign, left_significand, right_significand = _parse_significand(significand)
    # Return the named tuple
    return FloatParts(sign=sign, left_significand=left_significand,
                      right_significand=right_significand,
                      exponent=exponent)


def _count_leading_zeros(val):
    """
    This function accepts a string representing an integer.
    This string shouldn't contain a sign symbol,
    or any prefix such 0x, 0b, or 0o.
    If you want to count leading zeros for an integer representation
    that might contain a sign symbol, use the 'count_leading_zeros' function
    """
    if not val:
        return 0
    z = list()
    for x in val:
        if x == "0":
            z.append(x)
        elif x == "_":
            continue
        else:
            break
    n = len(z)
    if n == len(val):
        return n-1
    return n


def tidy_up_float(s, width=3):
    """Tidy up a float number (str or float or decimal.Decimal)
    Example: 3.141234 -> 3.141_234
    """
    s = s if isinstance(s, str) else str(s)
    # make sure that s isn't "nan", "inf", "-inf", "infinity", ...
    for char in s:
        if char not in "-01234.56789+eE":
            return s
    info = split_float(s)
    tidy_left_significand = tidy_up_int(info.left_significand)
    tidy_right_significand = ""
    if info.right_significand:
        cache = _tidy_up_right_significand(info.right_significand, width)
        tidy_right_significand = "." + cache
    tidy_exponent = "E" + info.exponent if int(info.exponent) != 0 else ""
    result = info.sign + tidy_left_significand + tidy_right_significand + tidy_exponent
    return result


def _tidy_up_right_significand(s, width):
    if not s:
        return ""
    cache = list()
    group = list()
    i = 0
    for char in s:
        if i == width:
            cache.append("".join(group))
            group = list()
            i = 0
        group.append(char)
        i += 1
    if group:
        cache.append("".join(group))
    return "_".join(cache)


def tidy_up_int(val, width=3):
    """Tidy up some int number (str or int)
    Example: 300141234 -> 300_141_234
    0xFFFFFFFF -> 0xFFFF_FFFF
    Returns a string
    """
    parts = split_int(val)
    val = parts.leading_zeros + parts.val.upper()
    tidy = list()
    group = list()
    i = 0
    for char in reversed(val):
        if i == width:
            tidy.insert(0, "".join(group))
            group = list()
            i = 0
        group.insert(0, char)
        i += 1
    if group:
        tidy.insert(0, "".join(group))
    return parts.sign + parts.prefix + "_".join(tidy)


def is_whole_number(number):
    return number % 1 == 0


def _prepare_float(s):
    if not isinstance(s, str):
        s = str(s)
    # Remove underscores, whitespaces, upper e
    cache = list()
    for c in s:
        if c in ("_", " "):
            continue
        elif c == "e":
            c = "E"
        cache.append(c)
    return "".join(cache)


def _parse_significand(s):
    if not s:
        raise errors.Error("Can't parse an empty significand")
    parts = s.split(".", 1)
    left_significand = parts[0]
    sign = left_significand[0]
    if sign in ("+", "-"):
        left_significand = left_significand[1:]
    else:
        sign = ""
    right_significand = parts[1] if len(parts) == 2 else "0"
    return sign, left_significand, right_significand
