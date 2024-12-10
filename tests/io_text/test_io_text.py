import unittest
import pathlib
import tempfile
from paradict import encode
from paradict.io_text import decode_from, encode_into


class TestDecodeFromFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        with open(self._path, "w", encoding="utf-8") as file:
            encode_into(data, file)
        with open(self._path, "r", encoding="utf-8") as file:
            r = decode_from(file)
        expected = data
        self.assertEqual(expected, r)


class TestEncodeIntoFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        with open(self._path, "w", encoding="utf-8") as file:
            encode_into(data, file)
        with open(self._path, "r", encoding="utf-8") as file:
            r = file.read()
        expected = encode(data) + "\n"
        self.assertEqual(expected, r)


if __name__ == "__main__":
    unittest.main()
