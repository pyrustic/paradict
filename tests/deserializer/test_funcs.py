import unittest
import pathlib
import tempfile

from docutils.parsers.rst.directives import encoding

from paradict import load, dump, read, write


class TestLoadFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        with open(self._path, "wb") as file:
            dump(data, file)
        with open(self._path, "rb") as file:
            r = load(file)
        expected = data
        self.assertEqual(expected, r)


class TestDecodeFunc(unittest.TestCase):
    """The 'decode' function is already heavily
     used in the 'decoder' test module"""
    def test(self):
        self.assertTrue(True)


class TestUnpackFunc(unittest.TestCase):
    """The 'unpack' function is already heavily
     used in the 'unpacker' test module"""
    def test(self):
        self.assertTrue(True)


class TestReadFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        with open(self._path, "w", encoding="utf-8") as file:
            write(data, file)
        with open(self._path, "r", encoding="utf-8") as file:
            r = read(file)
        expected = data
        self.assertEqual(expected, r)


if __name__ == "__main__":
    unittest.main()
