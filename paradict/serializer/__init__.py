"""High-level functions to serialize Python dict in Paradict binary/text format"""
import os
import os.path
import written
import pathlib
from paradict.serializer.encoder import Encoder
from paradict.serializer.packer import Packer
from paradict import const


__all__ = ["encode", "write", "pack", "dump"]


def encode(data, *, mode=const.DATA_MODE, type_ref=None,
           skip_comments=False, bin_to_text=True,
           root_dir=None, attachments_dir="attachments"):
    """
    Convert a Python dictionary object to Paradict binary format

    [param]
    - data: Python dict
    - mode: either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.
    - type_ref: optional TypeRef object
    - skip_comments: boolean to tell whether comments should be ignored or not
    - bin_to_text: boolean to tell whether bin data should be converted into text or not
    - root_dir: root directory in which the attachments dir is supposed to be
    - attachments_dir: attachments directory. This is a path that is relative to the root dir.
     Note that relative paths should use a slash as separator.

    [return]
    Return a string in the Paradict text format
    """
    encoder = Encoder(mode=mode, type_ref=type_ref,
                      skip_comments=skip_comments,
                      bin_to_text=bin_to_text, root_dir=root_dir,
                      attachments_dir=attachments_dir)
    lines = list()
    for r in encoder.encode(data):
        lines.append(r)
    return "\n".join(lines)


def write(data, path, *, mode=const.DATA_MODE, type_ref=None,
          skip_comments=False, bin_to_text=False,
          attachments_dir="attachments"):
    """
    Convert some Python dict in the Paradict textual format
    then write it to a file

    [param]
    - path: path string or pathlib.Path instance
    - mode: either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.
    - type_ref: optional TypeRef object
    - skip_comments: boolean to tell whether comments should be ignored or not
    - bin_to_text: boolean to tell whether bin data should be converted into text or not
    - attachments_dir: path to attachments directory. Relative paths should use
        a slash as separator
    """
    path = str(pathlib.Path(path).resolve())
    r = encode(data, mode=mode, skip_comments=skip_comments,
               type_ref=type_ref, bin_to_text=bin_to_text,
               root_dir=os.path.dirname(path),
               attachments_dir=attachments_dir)
    return written.write(r, path)


def pack(data, *, type_ref=None, skip_comments=False):
    """
    Convert a Python dictionary object to Paradict binary format

    [param]
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

    [param]
    - path: path string or pathlib.Path instance
    - type_ref: optional TypeRef object
    - skip_comments: boolean to tell whether comments should be ignored or not
    """
    path = str(pathlib.Path(path).resolve())
    r = pack(data, skip_comments=skip_comments, type_ref=type_ref)
    return written.write(r, path)
