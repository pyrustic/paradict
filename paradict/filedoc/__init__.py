"""FileDoc class for creating model for textual Paradict data file"""
import os.path
import braq
from paradict.document import Document
from paradict import const


class FileDoc(Document):
    """Create a model for a textual Paradict data file"""
    def __init__(self, path, *, schema=None,
                 type_ref=None, obj_builder=None,
                 spacing=1, encoding_mode=const.DATA_MODE):
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
        - encoding_mode: either 1 or 2, to indicate if Python dicts should be
        encoded with the const.DATA_MODE or const.CONFIG_MODE. By default,
        a document's encoding mode is set to const.DATA_MODE
        """
        super().__init__(schema=schema, type_ref=type_ref,
                         obj_builder=obj_builder, spacing=spacing,
                         encoding_mode=encoding_mode)
        self._sections = None
        self._path = path

    @property
    def path(self):
        return self._path

    def get(self, header, skip_comments=True):
        """
        Decode and return the section whose header is provided

        [parameters]
        - header: the string header of the section
        - skip_comments: boolean to tell whether comments should be ignored or not
        """
        self._ensure_sections()
        return super().get(header, skip_comments=skip_comments)

    def set(self, header, body=None):
        """
        Encode and set a new section.
        Note that this operation will edit the linked file.
        Also note that the update method is suited for
        multiple 'set' operations

        [parameters]
        - body: Python dictionary representing the data to encode
        - header: the string header of the section
        """
        self._ensure_sections()
        super().set(header, body)
        self.save()

    def update(self, *sections):
        """
        Encode and set new sections.
        Note that this operation will edit the linked file.

        [parameters]
        - *sections: A section is a 2-tuple: (header, body)
        """
        self._ensure_sections()
        for header, body in sections:
            super().set(header, body)
        self.save()

    def check(self):
        """
        Return the ordered list (a 'tuple' to be precise)
        of section's headers (strings)
        """
        self._ensure_sections()
        return super().check()

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
        self._ensure_sections()
        return super().render(*headers)

    def save_to(self, path):
        """Save the document to a new file.
        Here, path is either a path string
        or a pathlib.Path object"""
        self._ensure_sections()
        return super().save_to(path)

    def remove(self, *headers):
        """remove specific sections from both the document model and the linked file"""
        self._ensure_sections()
        super().remove(*headers)
        self.save()

    def clear(self):
        """clear the document (as well the model as the linked file's contents"""
        self._ensure_sections()
        super().clear()
        self.save()

    def load(self):
        """load the document from the linked file"""
        if not os.path.isfile(self._path):
            self._sections = dict()
            return False
        self._sections = braq.read(self._path, end_of_stream="===")
        return True

    def save(self):
        """Save the document in the linked file. Return a confirmation bool"""
        if self._sections is None:
            return False
        s = list()
        for header, body in self._sections.items():
            s.append((header, body))
        braq.write(*s, dest=self._path, spacing=self._spacing)
        return True

    def _ensure_sections(self):
        if self._sections is None:
            self.load()
