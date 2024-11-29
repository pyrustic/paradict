import os

import paradict.io_text
from paradict import tags
from paradict.tags.mappings import (PINT_TO_SIZE,
                                    NINT_TO_SIZE, BIN_TO_SIZE,
                                    VARSTR_TO_SIZE, STR_TO_SIZE)


def scan(file):
    """Scan a binary Paradict file object, yielding a tag with
    the slice object of its associated payload"""
    file.seek(0)
    while 1:
        tag = file.read(1)
        if not tag:
            return
        file.seek(-1, os.SEEK_CUR)  # put cursor back to original position
        # STRx
        if tags.STR_8 <= tag <= tags.STR_256:
            slice_object = process_strx(file, tag)
        # STR
        elif tag in (tags.STR_SHORT,
                           tags.STR_MEDIUM,
                           tags.STR_LONG,
                           tags.STR_BIG,
                           tags.STR_HEAVY):
            slice_object = process_str(file, tag)
        # BIN
        elif tag in (tags.BIN_SHORT,
                           tags.BIN_MEDIUM,
                           tags.BIN_LONG,
                           tags.BIN_BIG,
                           tags.BIN_HEAVY):
            slice_object = process_bin(file, tag)
        # PINTx
        elif tags.PINT_8 <= tag <= tags.PINT_64:
            slice_object = process_pintx(file, tag)
        # PINT_BIG
        elif tag == tags.PINT_BIG:
            slice_object = process_pint_big(file, tag)
        # PINT_HEAVY
        elif tag == tags.PINT_HEAVY:
            slice_object = process_pint_heavy(file, tag)
        # NINTx
        elif tags.NINT_8 <= tag <= tags.NINT_64:
            slice_object = process_nintx(file, tag)
        # NINT_BIG
        elif tag == tags.NINT_BIG:
            slice_object = process_nint_big(file, tag)
        # NINT_HEAVY
        elif tag == tags.NINT_HEAVY:
            slice_object = process_nint_heavy(file, tag)
        # else...
        else:
            slice_object = process_tag(file, tag)
        yield tag, slice_object


def read_payload_size(file, nb):
    """
    Read the expected size of payload
    Note that nb is the number of bytes encoding the size of payload
    """
    position = file.tell()
    r = file.read(nb)
    file.seek(position)
    return int.from_bytes(r, "little", signed=False)


def get_slice_for_fixed_length_datum(file, payload_size):
    """
    This function returns the slice object for
    datums with fixed-length payload
    """
    position = file.tell()
    width = 1 + payload_size  # 1 tag + size
    start, stop = position, position + width
    file.seek(stop)
    return slice(start, stop)


def get_slice_for_variable_length_datum(file, nb):
    """
    This function is used to generate a slice object for
    tags with variable-length payload such as:
    STR_SHORT, STR_MEDIUM, STR_LONG, STR_BIG, STR_HEAVY,
    BIN_SHORT, BIN_MEDIUM, BIN_LONG, BIN_BIG, and BIN_HEAVY.

    nb is the number of bytes encoding the size of payload

    This function returns a slice object
    """
    # put the file cursor right after the tag
    position = file.tell()
    file.seek(position+1)
    # header_size
    header_size = 1 + nb  # 1 tag + nb
    payload_size = read_payload_size(file, nb) + 1  # \x00 as payload size means 1
    # Width is the size (bytes) of the datum (header + payload)
    # note that the header is made of tag + byte(s) to store payload size
    width = header_size + payload_size
    start, stop = position, position + width
    file.seek(stop)  # move the file cursor to the stop
    return slice(start, stop)


def process_tag(file, tag):
    position, width = file.tell(), 1
    start, stop = position, position + width
    file.seek(stop)  # move the file cursor to the stop
    return slice(start, stop)


def process_str(file, tag):
    # nb is the number of bytes to encode the size of payload
    nb = VARSTR_TO_SIZE[tag]
    return get_slice_for_variable_length_datum(file, nb)


def process_strx(file, tag):
    payload_size = STR_TO_SIZE[tag]
    return get_slice_for_fixed_length_datum(file, payload_size)


def process_bin(file, tag):
    # nb is the number of bytes to encode the size of payload
    nb = BIN_TO_SIZE[tag]
    return get_slice_for_variable_length_datum(file, nb)


def process_pint_big(file, tag):
    nb = 1
    return get_slice_for_variable_length_datum(file, nb)


def process_pint_heavy(file, tag):
    nb = 2
    return get_slice_for_variable_length_datum(file, nb)


def process_pintx(file, tag):
    payload_size = PINT_TO_SIZE[tag]
    return get_slice_for_fixed_length_datum(file, payload_size)


def process_nint_big(file, tag):
    return process_pint_big(file, tag)


def process_nint_heavy(file, tag):
    return process_pint_heavy(file, tag)


def process_nintx(file, tag):
    payload_size = NINT_TO_SIZE[tag]
    return get_slice_for_fixed_length_datum(file, payload_size)
