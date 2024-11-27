"""High-level functions to serialize Python dict in Paradict binary/text format"""
import os
import os.path
import pathlib
from paradict.serializer.encoder import Encoder
from paradict.serializer.packer import Packer
from paradict import const


__all__ = ["encode", "write", "pack", "dump"]


def encode(data, *, mode=const.DATA_MODE, type_ref=None,
           bin_to_text=True, root_dir=None, attachments_dir="attachments"):
    """
    Serialize a Python dict object with the Paradict binary format

    [param]
    - data: Python dict
    - mode: either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.
    - type_ref: optional TypeRef object
    - bin_to_text: boolean to tell whether bin data should be converted into text or not
    - root_dir: root directory in which the attachments dir is supposed to be
    - attachments_dir: attachments directory. This is a path that is relative to the root dir.
     Note that relative paths should use a slash as separator.

    [return]
    Return a string in the Paradict text format
    """
    encoder = Encoder(mode=mode, type_ref=type_ref,
                      bin_to_text=bin_to_text, root_dir=root_dir,
                      attachments_dir=attachments_dir)
    lines = list()
    for r in encoder.encode(data):
        lines.append(r)
    return "\n".join(lines)


def write(data, file, *, mode=const.DATA_MODE, type_ref=None,
          bin_to_text=False, attachments_dir="attachments"):
    """
    Serialize a Python dict object with the Paradict text format then write it to a file

    [param]
    - data: Python dict object
    - file: text file object
    - mode: either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.
    - type_ref: optional TypeRef object
    - bin_to_text: boolean to tell whether bin data should be converted into text or not
    - attachments_dir: path to attachments directory. Relative paths should use
        a slash as separator
    """
    root_dir = None
    if not bin_to_text:
        try:
            root_dir = os.path.dirname(os.path.abspath(file.name))
        except AttributeError as e:
            pass
    root_dir = None if bin_to_text else os.path.dirname(os.path.abspath(file.name))
    encoder = Encoder(mode=mode, type_ref=type_ref,
                      bin_to_text=bin_to_text, root_dir=root_dir,
                      attachments_dir=attachments_dir)
    for r in encoder.encode(data):
        file.write(r+"\n")


def pack(data, *, type_ref=None, dict_only=False):
    """
    Serialize a Python dict object with the Paradict binary format

    [param]
    - data: Python data object
    - type_ref: optional TypeRef object
    - dict_only: boolean to enforce dict as root

    [return]
    Return a Python bytes object packed in the Paradict binary format
    """
    packer = Packer(type_ref=type_ref, dict_only=dict_only)
    buffer = bytearray()
    for r in packer.pack(data):
        buffer.extend(r)
    return bytes(buffer)


def dump(data, file, *, type_ref=None, dict_only=False):
    """
    Serialize a Python data object with the Paradict binary format
    then dump it in a file

    [param]
    - data: Python data object
    - file: binary file object
    - type_ref: optional TypeRef object
    - dict_only: boolean to enforce dict as root
    """
    packer = Packer(type_ref=type_ref, dict_only=dict_only)
    for r in packer.pack(data):
        file.write(r)
