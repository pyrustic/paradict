import unittest
import pathlib
import tempfile
from paradict import load, dump


class TestLoadFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        dump(data, self._path)
        r = load(self._path)
        expected = data
        self.assertEqual(expected, r)


class TestDecodeFunc(unittest.TestCase):
    """The 'decode' function is already heavily
     used in the 'decoder' test module"""
    def test(self):
        self.assertTrue(True)


class TestPackFunc(unittest.TestCase):
    """The 'unpack' function is already heavily
     used in the 'unpacker' test module"""
    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
