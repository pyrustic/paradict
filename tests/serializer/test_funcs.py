import unittest
import pathlib
import tempfile
from paradict import dump, pack, write, encode


class TestPackFunc(unittest.TestCase):
    """The 'pack' function is already heavily
     used in the 'packer' test module"""
    def test(self):
        self.assertTrue(True)


class TestDumpFunc(unittest.TestCase):

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
            r = file.read()
        expected = pack(data)
        self.assertEqual(expected, r)


class TestEncodeFunc(unittest.TestCase):
    """The 'encode' function is already heavily
     used in the 'encoder' test module"""
    def test(self):
        self.assertTrue(True)


class TestWriteFunc(unittest.TestCase):

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
            r = file.read()
        expected = encode(data) + "\n"
        self.assertEqual(expected, r)


if __name__ == "__main__":
    unittest.main()
