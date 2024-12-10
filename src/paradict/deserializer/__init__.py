"""High-level functions to deserialize Paradict binary/text data into a Python dict"""
from paradict.deserializer.decoder import Decoder
from paradict.deserializer.unpacker import Unpacker


__all__ = ["decode", "unpack"]


def decode(text, type_ref=None, receiver=None, obj_builder=None,
           root_dir=None):
    """
    Convert some textual Paradict data into a Python dictionary

    [param]
    - text: string to convert into a Python dict
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.xtypes.Obj container and
    returns a fresh new Python object
    - root_dir: root directory in which the attachments dir is supposed to be

    [return]
    Return the newly built Python object
    """
    decoder = Decoder(type_ref=type_ref, receiver=receiver,
                      obj_builder=obj_builder,
                      root_dir=root_dir)
    decoder.feed(text)
    if not decoder.queue.is_empty():
        decoder.feed("\n")
    decoder.feed("===\n")  # it's important to send an explicit end of stream
    return decoder.data


def unpack(raw, type_ref=None, receiver=None, obj_builder=None):
    """
    Convert some binary Paradict data into a Python dictionary

    [param]
    - raw: raw data previously packed with Paradict
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.xtypes.Obj container and
    returns a fresh new Python object
    - dict_only: boolean to enforce dict as root

    [return]
    Return the newly built Python object
    """
    unpacker = Unpacker(type_ref=type_ref,
                        receiver=receiver,
                        obj_builder=obj_builder)
    unpacker.feed(raw)
    return unpacker.data
