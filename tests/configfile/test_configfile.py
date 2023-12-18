import unittest
import tempfile
import pathlib
from textwrap import dedent
from paradict import ConfigFile


class TestConfigFile(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name
        self._document = ConfigFile(self._path)

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        body1 = {"_0": "opening line"}
        body2 = {"name": "alex", "pi": 3.14, "_42": 420}
        self._document.update(("", body1), ("header", body2))
        # 1
        with self.subTest():
            r = self._document.get("")
            expected = body1
            self.assertEqual(expected, r)
        # 2
        with self.subTest():
            r = self._document.get("header")
            expected = body2
            self.assertEqual(expected, r)
        # 3
        with self.subTest():
            r = self._document.render()
            expected = """\
            _0 = "opening line"
            
            [header]
            name = "alex"
            pi = 3.14
            _42 = 420"""
            self.assertEqual(dedent(expected), r)


if __name__ == '__main__':
    unittest.main()
