"""ConfigFile class for creating model for Paradict configuration file"""
from paradict import const
from paradict.filedoc import FileDoc


class ConfigFile(FileDoc):
    """A configfile is based on FileDoc, itself based on Document.
    The difference between FileDoc and Document is that
    FileDoc implies a physical file.
    ConfigFile is a FileDoc but only for configuration file.
    Its encoding_mode is const.CONFIG_MODE"""
    def __init__(self, path, *, schema=None,
                 type_ref=None, obj_builder=None,
                 spacing=1):
        """
        Init

        [parameters]
        - path: path string or a pathlib.Path instance
        - schema: a Python dict that serves as schema to validate the sections
        of the document. It is a dictionary of dictionaries, with root keys
        representing a section header.
        - type_ref: optional TypeRef object
        - obj_builder: function that accepts a paradict.box.Obj container and
        returns a fresh new Python object
        - spacing: number of blank lines to place between two adjacent sections
        """
        super().__init__(path, schema=schema, type_ref=type_ref,
                         obj_builder=obj_builder, spacing=spacing,
                         encoding_mode=const.CONFIG_MODE)
