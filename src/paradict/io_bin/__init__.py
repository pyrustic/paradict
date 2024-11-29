"""Load and dump binary Paradict from/to file"""
from paradict.serializer.packer import Packer
from paradict.deserializer.unpacker import Unpacker


__all__ = ["load", "dump"]


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
