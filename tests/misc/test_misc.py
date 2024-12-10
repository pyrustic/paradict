import unittest
from paradict import misc, xtypes


class TestPrettifyGridFunc(unittest.TestCase):

    def test(self):
        grid = xtypes.Grid([[10, 1, 0],
                            [0,  100, 0],
                            [0,  1,   10000]])
        r = misc.prettify_grid(grid)
        expected = [("10", "1  ", "0    "),
                    ("0 ", "100", "0    "),
                    ("0 ", "1  ", "10000")]
        self.assertEqual(expected, r)


class TestAddLeadingZerosFunc(unittest.TestCase):

    def test_with_int(self):
        for key, val in {0: "0000000",
                         100: "0000100",
                         1000: "0001000",
                         1000000: "1000000",
                         -100: "-0000100",
                         -1000: "-0001000",
                         -1000000: "-1000000"}.items():
            with self.subTest("Key: '{}'".format(key)):
                r = misc.left_pad_int(key, width=7)
                self.assertEqual(val, r)

    def test_with_hex(self):
        for key, val in {"0x0": "0x0000000",
                         "0x100": "0x0000100",
                         "0x1000": "0x0001000",
                         "0x1000000": "0x1000000",
                         "-0x100": "-0x0000100",
                         "-0x1000": "-0x0001000",
                         "-0x1000000": "-0x1000000"}.items():
            with self.subTest("Key: '{}'".format(key)):
                r = misc.left_pad_int(key, width=7)
                self.assertEqual(val, r)

    def test_with_oct(self):
        for key, val in {"0o0": "0o0000000",
                         "0o100": "0o0000100",
                         "0o1000": "0o0001000",
                         "0o1000000": "0o1000000",
                         "-0o100": "-0o0000100",
                         "-0o1000": "-0o0001000",
                         "-0o1000000": "-0o1000000"}.items():
            with self.subTest("Key: '{}'".format(key)):
                r = misc.left_pad_int(key, width=7)
                self.assertEqual(val, r)

    def test_with_bin(self):
        for key, val in {"0b0": "0b0000000",
                         "0b100": "0b0000100",
                         "0b1000": "0b0001000",
                         "0b1000000": "0b1000000",
                         "-0b100": "-0b0000100",
                         "-0b1000": "-0b0001000",
                         "-0b1000000": "-0b1000000"}.items():
            with self.subTest("Key: '{}'".format(key)):
                r = misc.left_pad_int(key, width=7)
                self.assertEqual(val, r)


if __name__ == '__main__':
    unittest.main()
