import unittest
import pathlib
import tempfile
from paradict import pack
from paradict.io_bin import load, dump


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


if __name__ == "__main__":
    unittest.main()
