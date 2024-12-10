import unittest
from paradict import xtypes


class TestHexInt(unittest.TestCase):

    def test_with_int(self):
        for key, val in {0: 0,
                         1: 1,
                         -255: -255}.items():
            with self.subTest("Val: {}".format(key)):
                r = xtypes.HexInt(key)
                self.assertEqual(val, r)

    def test_with_str_int(self):
        for key, val in {"0": 0,
                         "1": 1,
                         "-255": -255,
                         "0x0": 0,
                         "0x1": 1,
                         "-0xff": -255}.items():
            with self.subTest("Val: {}".format(key)):
                r = xtypes.HexInt(key)
                self.assertEqual(val, r)

    def test_string_output(self):
        for key, val in {0: "0x0",
                         1: "0x1",
                         -255: "-0xff",
                         "0x0": "0x0",
                         "0x1": "0x1",
                         "-0x000000ff": "-0x0000_00ff"}.items():
            with self.subTest("Val: {}".format(key)):
                r = str(xtypes.HexInt(key)).lower()
                self.assertEqual(val, r)

    def test_with_different_base(self):
        r = xtypes.HexInt("-0b11111111")
        self.assertEqual(-255, r)

    def test_string_output_with_different_base(self):
        r = xtypes.HexInt("-0b1111_1111")  # the number of digits counts
        self.assertEqual("-0xff", str(r).lower())


class TestOctInt(unittest.TestCase):

    def test_with_int(self):
        for key, val in {0: 0,
                         1: 1,
                         -255: -255}.items():
            with self.subTest("Val: {}".format(key)):
                r = xtypes.OctInt(key)
                self.assertEqual(val, r)

    def test_with_str_int(self):
        for key, val in {"0": 0,
                         "1": 1,
                         "-255": -255,
                         "0o0": 0,
                         "0o1": 1,
                         "-0o377": -255}.items():
            with self.subTest("Val: {}".format(key)):
                r = xtypes.OctInt(key)
                self.assertEqual(val, r)

    def test_string_output(self):
        for key, val in {0: "0o0",
                         1: "0o1",
                         -255: "-0o377",
                         "0o0": "0o0",
                         "0o1": "0o1",
                         "-0o000377": "-0o000_377"}.items():
            with self.subTest("Val: {}".format(key)):
                r = str(xtypes.OctInt(key)).lower()
                self.assertEqual(val, r)

    def test_with_different_base(self):
        r = xtypes.OctInt("-0xff")
        self.assertEqual(-255, r)

    def test_string_output_with_different_base(self):
        r = xtypes.OctInt("-0x00ff")
        self.assertEqual("-0o377", str(r).lower())


class TestBinInt(unittest.TestCase):

    def test_with_int(self):
        for key, val in {0: 0,
                         1: 1,
                         -255: -255}.items():
            with self.subTest("Val: {}".format(key)):
                r = xtypes.BinInt(key)
                self.assertEqual(val, r)

    def test_with_str_int(self):
        for key, val in {"0": 0,
                         "1": 1,
                         "-255": -255,
                         "0b0": 0,
                         "0b1": 1,
                         "-0b11111111": -255}.items():
            with self.subTest("Val: {}".format(key)):
                r = xtypes.BinInt(key)
                self.assertEqual(val, r)

    def test_string_output(self):
        for key, val in {0: "0b0",
                         1: "0b1",
                         -255: "-0b1111_1111",
                         "0b0": "0b0",
                         "0b1": "0b1",
                         "-0b000011111111": "-0b0000_1111_1111"}.items():
            with self.subTest("Val: {}".format(key)):
                r = str(xtypes.BinInt(key)).lower()
                self.assertEqual(val, r)

    def test_with_different_base(self):
        r = xtypes.BinInt("-0xff")
        self.assertEqual(-255, r)

    def test_string_output_with_different_base(self):
        r = xtypes.BinInt("-0xff")
        self.assertEqual("-0b1111_1111", str(r).lower())


if __name__ == '__main__':
    unittest.main()
