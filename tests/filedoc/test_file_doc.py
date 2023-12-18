import unittest
import pathlib
import tempfile
from textwrap import dedent
from paradict import FileDoc


INIT_TEXT = """\
0: "opening line"

[header]
"name": "alex"
"pi": 3.14
42: 420"""


class TestFileDoc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._path = file.name
        self._document = FileDoc(self._path)

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test_get_method(self):
        # 1
        with self.subTest("Test unnamed section"):
            r = self._document.get("")
            expected = {0: "opening line"}
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Test named section"):
            r = self._document.get("header")
            expected = {"name": "alex", "pi": 3.14, 42: 420}
            self.assertEqual(expected, r)

    def test_set_method(self):
        data = {"name": "alx", "pi": 3.14}
        self._document.set("header", data)
        r = read_file(self._path)
        expected = """\
        0: "opening line"
        
        [header]
        "name": "alx"
        "pi": 3.14"""
        self.assertEqual(dedent(expected), r)

    def test_update_method(self):
        body1 = {0: 420}
        body2 = {}
        self._document.update(("", body1), ("header", body2))
        r = read_file(self._path)
        expected = """\
        0: 420
        
        [header]"""
        self.assertEqual(dedent(expected), r)

    def test_check_method(self):
        r = self._document.check()
        expected = ("", "header")
        self.assertEqual(expected, r)

    def test_render_method(self):
        r = self._document.render()
        expected = INIT_TEXT
        self.assertEqual(expected, r)

    def test_remove_method(self):
        self._document.remove("")
        r = read_file(self._path)
        expected = """\
        [header]
        "name": "alex"
        "pi": 3.14
        42: 420"""
        self.assertEqual(dedent(expected), r)

    def test_group_remove_method(self):
        self._document.remove("", "header")
        r = read_file(self._path)
        expected = ""
        self.assertEqual(expected, r)

    def test_clear_method(self):
        self._document.clear()
        r = read_file(self._path)
        expected = ""
        self.assertEqual(expected, r)

    def test_save_method(self):
        """This method is implicitly called by set, update, remove, and clear methods"""
        self.assertTrue(True)

    def test_load_method(self):
        """This method is implicitly called by other methods"""
        self.assertTrue(True)


class TestSaveToMethod(unittest.TestCase):

    def setUp(self):
        # file1
        file1 = tempfile.NamedTemporaryFile(delete=False)
        file1.write(INIT_TEXT.encode("utf-8"))
        file1.close()
        self._path1 = file1.name
        self._document = FileDoc(self._path1)
        # file2
        file2 = tempfile.NamedTemporaryFile(delete=False)
        file2.close()
        self._path2 = file2.name

    def tearDown(self):
        pathlib.Path(self._path1).unlink()
        pathlib.Path(self._path2).unlink()

    def test(self):
        self._document.save_to(self._path2)
        r = read_file(self._path2)
        expected = INIT_TEXT
        self.assertEqual(expected, r)


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    return data


if __name__ == '__main__':
    unittest.main()
