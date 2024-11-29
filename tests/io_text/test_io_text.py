import unittest
import pathlib
import tempfile
from paradict import encode
from paradict.io_text import load, dump


class TestLoadFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        data = {0: "hello world", "pi": 3.14}
        with open(self._path, "w", encoding="utf-8") as file:
            dump(data, file)
        with open(self._path, "r", encoding="utf-8") as file:
            r = load(file)
        expected = data
        self.assertEqual(expected, r)


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
            dump(data, file)
        with open(self._path, "r", encoding="utf-8") as file:
            r = file.read()
        expected = encode(data) + "\n"
        self.assertEqual(expected, r)


if __name__ == "__main__":
    unittest.main()
