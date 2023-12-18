"""High-level functions to deserialize Paradict binary/text data into a Python dict"""
import pathlib
from paradict.deserializer.decoder import Decoder
from paradict.deserializer.unpacker import Unpacker


def decode(text, type_ref=None, receiver=None, obj_builder=None,
           skip_comments=False):
    """
    Convert some textual Paradict data into a Python dictionary

    [parameters]
    - text: string to convert into a Python dict
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.box.Obj container and
    returns a fresh new Python object
    - skip_comments: boolean to tell whether comments should be ignored or not

    [return]
    Return the newly built Python object
    """
    decoder = Decoder(type_ref=type_ref, receiver=receiver,
                      obj_builder=obj_builder,
                      skip_comments=skip_comments)
    decoder.feed(text)
    if decoder.queue.buffer:
        decoder.feed("\n")
    decoder.feed("===\n")
    return decoder.data


def unpack(raw, type_ref=None, receiver=None, obj_builder=None,
           skip_comments=False):
    """
    Convert some binary Paradict data into a Python dictionary

    [parameters]
    - raw: raw data previously packed with Paradict
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.box.Obj container and
    returns a fresh new Python object
    - skip_comments: boolean to tell whether comments should be ignored or not

    [return]
    Return the newly built Python object
    """
    unpacker = Unpacker(type_ref=type_ref,
                        receiver=receiver,
                        obj_builder=obj_builder,
                        skip_comments=skip_comments)
    unpacker.feed(raw)
    return unpacker.data


def load(path, type_ref=None, obj_builder=None, skip_comments=False):
    """
    Open a binary Paradict file then unpack its contents into Python dict

    [parameters]
    - path: a path string, or a pathlib.Path instance
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.box.Obj container and
    returns a fresh new Python object
    - skip_comments: boolean to tell whether comments should be ignored or not

    [return]
    Return the newly built Python object
    """
    path = str(pathlib.Path(path).resolve())
    with open(path, "rb") as file:
        r = file.read()
    return unpack(r, obj_builder=obj_builder, type_ref=type_ref,
                  skip_comments=skip_comments)
