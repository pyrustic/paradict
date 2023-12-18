import unittest
import pathlib
import tempfile
from textwrap import dedent
from paradict import Document, box


INIT_TEXT = """\
0: "opening line"

[header]
"name": "alex"
"pi": 3.14
42: 420"""


SCHEMA = {"": {0: "str"},
          "header": {"name": "str",
                     "pi": "float",
                     42: "int"}}


SCHEMA_TEXT = """\
0: "str"

[header]
"name": "str"
"pi": "float"
42: "int"
"""


class TestEmptyDocument(unittest.TestCase):

    def setUp(self):
        self._document = Document()

    def test_get_method(self):
        r = self._document.get("header")
        expected = None
        self.assertEqual(expected, r)

    def test_set_method(self):
        data = {"name": "alex", "pi": 3.14, 42: 420}
        self._document.set("header", data)
        r = self._document.get("header")
        expected = data
        self.assertEqual(expected, r)

    def test_check_method(self):
        r = self._document.check()
        expected = tuple()
        self.assertEqual(expected, r)

    def test_render_method(self):
        r = self._document.render()
        expected = str()
        self.assertEqual(expected, r)

    def test_remove_method(self):
        # 1
        with self.subTest("Test 'remove' method without argument"):
            try:
                self._document.remove()
            except Exception as e:
                self.assertTrue(False)
        # 2
        with self.subTest("Test 'remove' method with argument"):
            try:
                self._document.remove("header")
            except Exception as e:
                self.assertTrue(False)

    def test_clear_method(self):
        try:
            self._document.clear()
        except Exception as e:
            self.assertTrue(False)


class TestDocument(unittest.TestCase):

    def setUp(self):
        self._document = Document(INIT_TEXT)

    def test_get_method(self):
        r = self._document.get("header")
        expected = {"name": "alex", "pi": 3.14, 42: 420}
        self.assertEqual(expected, r)

    def test_set_method(self):
        data = {"name": "alex", "pi": 3.14}
        self._document.set("header", data)
        r = self._document.get("header")
        expected = data
        self.assertEqual(expected, r)

    def test_check_method(self):
        r = self._document.check()
        expected = ("", "header")
        self.assertEqual(expected, r)

    def test_render_method(self):
        # 1
        with self.subTest("Render the entire doc"):
            r = self._document.render()
            expected = INIT_TEXT
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Render the unnamed section"):
            r = self._document.render("")
            expected = '0: "opening line"'
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Render the named section"):
            r = self._document.render("header")
            expected = """\
            [header]
            "name": "alex"
            "pi": 3.14
            42: 420"""
            self.assertEqual(dedent(expected), r)

    def test_remove_method(self):
        # 1
        with self.subTest("Test 'remove' method without argument"):
            self._document.remove()
            r = self._document.check()
            expected = ("", "header")
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Test 'remove' method with argument"):
            self._document.remove("header")
            r = self._document.check()
            expected = ("", )
            self.assertEqual(expected, r)

    def test_clear_method(self):
        self._document.clear()
        r = self._document.check()
        expected = tuple()
        self.assertEqual(expected, r)


class TestDocumentWithComment(unittest.TestCase):

    def setUp(self):
        text = """\
        # this is a comment
        0: 42"""
        self._document = Document(dedent(text))

    def test_get_method_default_behavior(self):
        r = self._document.get("")
        expected = {0: 42}
        self.assertEqual(expected, r)

    def test_get_method_with_comments_on(self):
        r = self._document.get("", skip_comments=False)
        r = tuple(r.values())
        expected = ("this is a comment", 42)
        self.assertEqual(expected, r)

    def test_creating_section_with_comment(self):
        body = {box.CommentID(): box.Comment("This is a comment !"),
                0: 42}
        self._document.set("header", body)
        r = self._document.get("header", skip_comments=False)
        r = tuple(r.values())
        expected = ("This is a comment !", 42)
        self.assertEqual(expected, r)


class TestLoadFromFileOperation(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._path = file.name
        self._document = Document()

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        self._document.load_from(self._path)
        r = self._document.get("header")
        expected = {"name": "alex", "pi": 3.14, 42: 420}
        self.assertEqual(expected, r)


class TestSaveToFileOperation(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name
        self._document = Document(INIT_TEXT)

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test(self):
        self._document.save_to(self._path)
        with open(self._path, "r", encoding="utf-8") as file:
            r = file.read()
        expected = INIT_TEXT
        self.assertEqual(expected, r)


class TestDocumentWithSchema(unittest.TestCase):

    def setUp(self):
        self._document = Document(INIT_TEXT, schema=SCHEMA)

    def test_schema_property(self):
        r = self._document.schema
        expected = SCHEMA
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._document.validate()
            expected = True
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate the unnamed and the named sections"):
            r = self._document.validate("", "header")
            expected = True
            self.assertEqual(expected, r)


class TestDocumentWithEmptySchemaFile(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path = file.name
        self._document = Document()
        self._document.load_schema(self._path)

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test_schema_property(self):
        r = self._document.schema
        expected = dict()
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._document.validate()
            expected = True
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate the named section"):
            r = self._document.validate("header")
            expected = True
            self.assertEqual(expected, r)


class TestDocumentWithSchemaFile(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(SCHEMA_TEXT.encode("utf-8"))
        file.close()
        self._path = file.name
        self._document = Document()
        self._document.load_schema(self._path)

    def tearDown(self):
        pathlib.Path(self._path).unlink()

    def test_schema_property(self):
        r = self._document.schema
        expected = SCHEMA
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._document.validate()
            expected = True
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate the named and the unnamed sections"):
            r = self._document.validate("", "header")
            expected = True
            self.assertEqual(expected, r)


if __name__ == '__main__':
    unittest.main()
