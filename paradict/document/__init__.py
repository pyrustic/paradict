"""Modeling a textual Paradict Document made of sections"""
import braq
from paradict.typeref import TypeRef
from paradict import validator, encode, decode
from paradict import errors, const


class Document:
    """Create a model for a textual Paradict Document made of sections."""
    def __init__(self, init_text="", *, schema=None,
                 type_ref=None, obj_builder=None,
                 spacing=1, encoding_mode=const.DATA_MODE):
        """
        Init

        [parameters]
        - init_text: optional TypeRef object
        - schema: a Python dict that serves as schema to validate the sections
        of the document. It is a dictionary of dictionaries, with root keys
        representing a section header.
        - type_ref: optional TypeRef object
        - obj_builder: function that accepts a paradict.box.Obj container and
        returns a fresh new Python object
        - spacing: number of blank lines to place between two adjacent sections
        - encoding_mode: either 1 or 2, to indicate if Python dicts should be
        encoded with the const.DATA_MODE or const.CONFIG_MODE. By default,
        a document's encoding mode is set to const.DATA_MODE
        """
        self._sections = braq.parse(init_text, end_of_stream="===")
        self._schema = schema
        self._type_ref = type_ref if type_ref else TypeRef()
        self._obj_builder = obj_builder
        self._spacing = spacing
        self._encoding_mode = encoding_mode

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, val):
        self._schema = val

    @property
    def spacing(self):
        return self._spacing

    @spacing.setter
    def spacing(self, val):
        self._spacing = val

    @property
    def obj_builder(self):
        return self._obj_builder

    @obj_builder.setter
    def obj_builder(self, val):
        self._obj_builder = val

    @property
    def encoding_mode(self):
        return self._encoding_mode

    @property
    def type_ref(self):
        return self._type_ref

    @type_ref.setter
    def type_ref(self, val):
        self._type_ref = val if val else TypeRef()

    def get(self, header, skip_comments=True):
        """
        Decode and return the section whose header is provided

        [parameters]
        - header: the string header of the section
        - skip_comments: boolean to tell whether comments should be ignored or not
        """
        body = self._sections.get(header)
        if not body:
            return None
        body = decode(body, obj_builder=self._obj_builder,
                      skip_comments=skip_comments,
                      type_ref=self._type_ref)
        return body

    def set(self, header, body=None):
        """
        Encode and set a new section

        [parameters]
        - body: Python dictionary representing the data to encode
        - header: the string header of the section
        """
        body = self._type_ref.dict_type if body is None else body
        if type(body) not in self._type_ref.dict_types:
            msg = "The body must be a dictionary"
            raise errors.Error(msg)
        body = encode(body, mode=self._encoding_mode,
                      type_ref=self._type_ref,
                      skip_comments=False,
                      skip_bin_data=False)
        self._sections[header] = body

    def check(self):
        """
        Return the ordered list (a 'tuple' to be precise)
        of section's headers (strings)
        """
        return tuple(self._sections.keys())

    def render(self, *headers):
        """
        Render the entire document or a specific set of sections, i.e.,
        return a textual Paradict string that may be stored in a file.

        [parameters]
        - *headers: Headers of sections to render.
        Omitting this will render the entire document

        [return]
        Returns a string that contains sections (each made of square-brackets delimited header
        and the associated body)
        """
        sections = list()
        cache = set()
        headers = headers if headers else self.check()
        for header in headers:
            if header in cache:
                continue
            else:
                cache.add(header)
            if header not in self._sections:
                continue
            sections.append((header, self._sections.get(header)))
        return braq.render(*sections, spacing=self._spacing)

    def load_schema(self, src):
        """
        Load a schema file

        [parameters]
        - src: either a path, a pathlib.Path object, or a file like object
        """
        r = braq.read(src, end_of_stream="===")
        self._schema = dict()
        for header, body in r.items():
            body = decode(body, type_ref=self._type_ref, obj_builder=self._obj_builder,
                          skip_comments=True)
            self._schema[header] = body

    def validate(self, *headers):
        """
        Validate this entire document or only specific section(s)

        [parameters]
        - *headers: headers to validate. If you ignore this parameter, the document will
        be checked against the schema.

        [return]
        Return true if the document is valid. Raise an exception if the schema is missing
        """
        if self._schema is None:
            msg = "Missing schema"
            raise errors.Error(msg)
        if type(self._schema) not in self._type_ref.dict_types:
            msg = "The schema must be a dictionary whose keys represent the section headers"
            raise errors.Error(msg)
        headers = headers if headers else self.check()
        for header in headers:
            if header not in self._schema:
                continue
            if not validator.validate(self.get(header, skip_comments=True),
                                      self._schema.get(header)):
                return False
        return True

    def load_from(self, path):
        """Load the document from a file by providing
        a path string or pathlib.Path object"""
        self._sections = braq.read(path, end_of_stream="===")

    def save_to(self, path):
        """
        Save the contents of this document to a specific file

        [parameters]
        - path: path to filename. Path may be a pathlib.Path instance
        """
        if not path:
            return False
        sections = list()
        for header, body in self._sections.items():
            sections.append((header, body))
        braq.write(*sections, dest=path, spacing=self._spacing)
        return True

    def remove(self, *headers):
        """
        Remove specific section(s) from this document

        [parameters]
        - *headers: the headers of the sections to remove
        """
        for header in headers:
            try:
                del self._sections[header]
            except KeyError as e:
                pass

    def clear(self):
        """Clear the entire document"""
        self._sections = dict()
