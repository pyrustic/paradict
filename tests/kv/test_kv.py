import unittest
from paradict import kv, const


class TestSplitFuncInDataMode(unittest.TestCase):

    def test_with_single_quote_and_compact_string(self):
        key = "'this_is_the_key'"
        val = "this_is_the_val"
        sep = ":"
        d = "{key}{sep} {val}".format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)

    def test_with_single_quote_and_spaced_string(self):
        key = "'this is the key'"
        val = "this is the val"
        sep = ":"
        d = "{key}{sep} {val}".format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)

    def test_with_double_quote_and_compact_string(self):
        key = '"this_is_the key"'
        val = "this_is_the_val"
        sep = ":"
        d = '{key}{sep} {val}'.format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)

    def test_with_double_quote_and_spaced_string(self):
        key = '"this is the key"'
        val = "this is the val"
        sep = ":"
        d = '{key}{sep} {val}'.format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)

    def test_with_escaped_single_quote(self):
        key = r"'this \' is the key'"
        key_bis = r"'this ' is the key'"
        val = "this is the val"
        sep = ":"
        d = "{key}{sep} {val}".format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key_bis, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)

    def test_with_escaped_double_quote(self):
        key = r'"this \" is the key"'
        key_bis = r'"this " is the key"'
        val = "this is the val"
        sep = ":"
        d = '{key}{sep} {val}'.format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key_bis, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)

    def test_with_backslash(self):
        key = r'"this \ is the key"'
        val = "this is the val"
        sep = ":"
        d = '{key}{sep} {val}'.format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)

    def test_with_double_backslash(self):
        key = r'"this \\ is the key"'
        val = "this is the val"
        sep = ":"
        d = '{key}{sep} {val}'.format(key=key, sep=sep, val=val)
        r = kv.split(d)
        expected = kv.Info(key, val, sep, const.DATA_MODE)
        self.assertEqual(expected, r)


if __name__ == '__main__':
    unittest.main()
