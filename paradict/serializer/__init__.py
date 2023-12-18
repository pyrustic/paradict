"""High-level functions to serialize Python dict in Paradict binary/text format"""
import written
from paradict.serializer.encoder import Encoder
from paradict.serializer.packer import Packer
from paradict import const


def encode(data, *, mode=const.DATA_MODE, type_ref=None,
           skip_comments=False, skip_bin_data=False):
    """
    Convert a Python dictionary object to Paradict binary format

    [parameters]
    - data: Python dict
    - mode: either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.
    - type_ref: optional TypeRef object
    - skip_comments: boolean to tell whether comments should be ignored or not
    - skip_bin_data: boolean to tell whether bin data should be ignored or not

    [return]
    Return a string in the Paradict text format
    """
    encoder = Encoder(mode=mode, type_ref=type_ref,
                      skip_comments=skip_comments,
                      skip_bin_data=skip_bin_data)
    lines = list()
    for r in encoder.encode(data):
        lines.append(r)
    return "\n".join(lines)


def pack(data, *, type_ref=None, skip_comments=False):
    """
    Convert a Python dictionary object to Paradict binary format

    [parameters]
    - data: Python dict
    - type_ref: optional TypeRef object
    - skip_comments: boolean to tell whether comments should be ignored or not

    [return]
    Return a Python bytes object packed in the Paradict binary format
    """
    packer = Packer(type_ref=type_ref, skip_comments=skip_comments)
    buffer = bytearray()
    for r in packer.pack(data):
        buffer.extend(r)
    return bytes(buffer)


def dump(data, path, *, type_ref=None, skip_comments=False):
    """
    Convert some Python dict in the Paradict binary format
    then dump it in a file
    [parameters]
    - path: path string or pathlib.Path instance
    - type_ref: optional TypeRef object
    - skip_comments: boolean to tell whether comments should be ignored or not
    """
    r = pack(data, skip_comments=skip_comments, type_ref=type_ref)
    written.write(r, path)
