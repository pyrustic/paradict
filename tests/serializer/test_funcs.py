import unittest
import pathlib
import tempfile
from paradict import dump, pack


class TestDumpFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        dump(data, self._path)
        with open(self._path, "rb") as file:
            r = file.read()
        expected = pack(data)
        self.assertEqual(expected, r)


class TestEncodeFunc(unittest.TestCase):
    """The 'encode' function is already heavily
     used in the 'encoder' test module"""
    def test(self):
        self.assertTrue(True)


class TestPackFunc(unittest.TestCase):
    """The 'pack' function is already heavily
     used in the 'packer' test module"""
    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
