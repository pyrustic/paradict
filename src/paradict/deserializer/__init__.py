"""High-level functions to deserialize Paradict binary/text data into a Python dict"""
import os
import os.path
import pathlib
from paradict.deserializer.decoder import Decoder
from paradict.deserializer.unpacker import Unpacker


__all__ = ["decode", "read", "unpack", "load"]


def decode(text, type_ref=None, receiver=None, obj_builder=None,
           root_dir=None):
    """
    Convert some textual Paradict data into a Python dictionary

    [param]
    - text: string to convert into a Python dict
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.box.Obj container and
    returns a fresh new Python object
    - root_dir: root directory in which the attachments dir is supposed to be

    [return]
    Return the newly built Python object
    """
    decoder = Decoder(type_ref=type_ref, receiver=receiver,
                      obj_builder=obj_builder,
                      root_dir=root_dir)
    decoder.feed(text)
    if decoder.queue.buffer:
        decoder.feed("\n")
    decoder.feed("===\n")
    return decoder.data


def read(file, type_ref=None, receiver=None, obj_builder=None,
         root_dir=None):
    """
    Open a textual Paradict file then read its contents into Python dict

    [param]
    - file: text file object
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.box.Obj container and
    returns a fresh new Python object

    [return]
    Return the newly built Python object
    """
    decoder = Decoder(type_ref=type_ref, receiver=receiver,
                      obj_builder=obj_builder,
                      root_dir=root_dir)
    while True:
        line = file.readline()
        if not line:
            break
        decoder.feed(line)
    if decoder.queue.buffer:
        decoder.feed("\n")
    decoder.feed("===\n")
    return decoder.data


def unpack(raw, type_ref=None, receiver=None, obj_builder=None,
           dict_only=False):
    """
    Convert some binary Paradict data into a Python dictionary

    [param]
    - raw: raw data previously packed with Paradict
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.box.Obj container and
    returns a fresh new Python object
    - dict_only: boolean to enforce dict as root

    [return]
    Return the newly built Python object
    """
    unpacker = Unpacker(type_ref=type_ref,
                        receiver=receiver,
                        obj_builder=obj_builder,
                        dict_only=dict_only)
    unpacker.feed(raw)
    return unpacker.data


def load(file, type_ref=None, receiver=None,
         obj_builder=None, dict_only=False):
    """
    Open a binary Paradict file then unpack its contents into Python dict

    [param]
    - file: bin file object
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.box.Obj container and
    returns a fresh new Python object
    - dict_only: boolean to enforce dict as root

    [return]
    Return the newly built Python object
    """
    unpacker = Unpacker(type_ref=type_ref,
                        receiver=receiver,
                        obj_builder=obj_builder,
                        dict_only=dict_only)
    chunk_size = 1024
    while True:
        r = file.read(chunk_size)
        if not r:
            break
        unpacker.feed(r)
    return unpacker.data
