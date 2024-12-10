import unittest
import pathlib
import tempfile
from paradict import pack
from paradict.io_bin import unpack_from, pack_into


class TestUnpackFromFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        with open(self._path, "wb") as file:
            pack_into(data, file)
        with open(self._path, "rb") as file:
            r = unpack_from(file)
        expected = data
        self.assertEqual(expected, r)


class TestPackIntoFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        with open(self._path, "wb") as file:
            pack_into(data, file)
        with open(self._path, "rb") as file:
            r = file.read()
        expected = pack(data)
        self.assertEqual(expected, r)


if __name__ == "__main__":
    unittest.main()
