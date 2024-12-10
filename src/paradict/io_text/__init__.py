"""Load and dump text Paradict from/to file"""
import os
from paradict import const
from paradict.serializer.encoder import Encoder
from paradict.deserializer.decoder import Decoder


__all__ = ["decode_from", "encode_into"]


def decode_from(file, type_ref=None, receiver=None, obj_builder=None,
                root_dir=None):
    """
    Open a textual Paradict file then read its contents into Python dict

    [param]
    - file: text file object
    - type_ref: optional TypeRef object
    - receiver: callback function that will be called at the end of conversion.
    This callback function accepts the Decoder instance as argument
    - obj_builder: function that accepts a paradict.xtypes.Obj container and
    returns a fresh new Python object
    - root_dir: The root_dir should be set only when the file object doesn't have
        a '.name' property. The root_dir will help to load attachments.
    [return]
    Return the newly built Python object
    """
    if root_dir is None:
        try:
            root_dir = os.path.dirname(os.path.abspath(file.name))
        except AttributeError as e:
            root_dir = None
    decoder = Decoder(type_ref=type_ref, receiver=receiver,
                      obj_builder=obj_builder,
                      root_dir=root_dir)
    while True:
        line = file.readline()
        if not line:
            break
        decoder.feed(line)
    if not decoder.queue.is_empty():
        decoder.feed("\n")
    decoder.feed("===\n")
    return decoder.data


def encode_into(data, file, *, mode=const.DATA_MODE, type_ref=None,
                bin_to_text=False, root_dir=None, attachments_dir="attachments"):
    """
    Serialize a Python dict object with the Paradict text format then write it to a file

    [param]
    - data: Python dict object
    - file: text file object
    - mode: either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.
    - type_ref: optional TypeRef object
    - bin_to_text: boolean to tell whether bin data should be converted into text or not
    - root_dir: the root_dir inside which attachments_dir is supposed to be.
        Set this only when bin_to_text is False and when the file object doesn't have a '.name'
        property that is basically the filename.
    - attachments_dir: path to attachments directory. Relative paths should use
        a slash as separator
    """
    if bin_to_text:
        root_dir = None
    else:
        if root_dir is None:
            try:
                root_dir = os.path.dirname(os.path.abspath(file.name))
            except AttributeError as e:
                root_dir = None
    encoder = Encoder(mode=mode, type_ref=type_ref,
                      bin_to_text=bin_to_text, root_dir=root_dir,
                      attachments_dir=attachments_dir)
    for r in encoder.encode(data):
        file.write(r+"\n")
