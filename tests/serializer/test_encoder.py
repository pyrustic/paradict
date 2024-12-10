import os
import os.path
import unittest
import datetime
import tempfile
from decimal import Decimal
from textwrap import dedent

import paradict.io_text
from paradict import serializer
from paradict import xtypes, const, errors


class TestEmptyData(unittest.TestCase):

    def test(self):
        data = dict()
        r = encode_data(data)
        expected = ""
        self.assertEqual(expected, r)


class TestDictInConfigMode(unittest.TestCase):

    def test_valid_dict(self):
        d = {"a_valid_key_42": {"another_key": 42}}
        r = encode_data(d, mode=const.CONFIG_MODE)
        expected = """\
        a_valid_key_42 = (dict)
            another_key = 42"""
        self.assertEqual(dedent(expected), r)

    def test_invalid_dict(self):  # in CONFIG_MODE, only string is allowed as dict key
        d1 = {42: None}
        d2 = {None: None}
        d3 = {True: None}
        d4 = {4.2: None}
        d5 = {complex(1, 2): None}
        d6 = {datetime.datetime(2020, 12, 31): None}
        for i, d in enumerate((d1, d2, d3, d4, d5, d6)):
            with self.subTest("Test {}".format(i + 1)):
                with self.assertRaises(errors.Error):
                    encode_data(d, mode=const.CONFIG_MODE)

    def test_malformed_dict_key(self):
        d1 = {"key_42=": None}
        d2 = {"1_key 42": None}
        for i, d in enumerate((d1, d2)):
            with self.subTest("Test {}".format(i+1)):
                with self.assertRaises(errors.Error):
                    encode_data(d, mode=const.CONFIG_MODE)


class TestDict(unittest.TestCase):

    def test_empty_dict(self):
        d = {0: dict()}
        r = encode_data(d)
        expected = "0: (dict)"
        self.assertEqual(expected, r)

    def test_dict_with_valid_keys(self):
        # are valid keys: integer (int, xtypes.HexInt, ...),
        # float, complex and string
        d = {0: None,
             "1": None,
             "": None,
             "key": None,
             3.14: None,
             complex(1, 2): None,
             "\n": None,
             "\\n": None}
        r = encode_data(d)
        expected = """\
        0: null
        "1": null
        "": null
        "key": null
        3.14: null
        1+2i: null
        "\\n": null
        "\\\\n": null"""
        self.assertEqual(dedent(expected), r)

    def test_dict_with_valid_values(self):
        d = {0: "hello world",
             1: "multiline\nstring",
             2: True,
             3: False,
             4: complex(1, 2),
             5: 42,
             6: 4.2,
             7: datetime.date(2020, 12, 31)}
        r = encode_data(d)
        expected = """\
        0: "hello world"
        1: (text)
            multiline
            string
            ---
        2: true
        3: false
        4: 1+2i
        5: 42
        6: 4.2
        7: 2020-12-31"""
        self.assertEqual(dedent(expected), r)

    def test_dict_with_invalid_keys(self):
        d1 = {None: None}
        d2 = {True: None}
        d3 = {datetime.datetime(2020, 12, 31): None}
        for i, d in enumerate((d1, d2, d3)):
            with self.subTest("Test {}".format(i + 1)):
                with self.assertRaises(errors.Error):
                    encode_data(d, mode=const.CONFIG_MODE)

    def test_nested_dict(self):
        d = {0: "hello world",
             "1": "multiline\nstring",
             "": True,
             "key": False,
             3.14: complex(1, 2),
             complex(1, 2): 42,
             "\n": 4.2,
             "\\n": datetime.date(2020, 12, 31),
             "nested": {0: "hello world",
                        "1": "multiline\nstring",
                        "": True,
                        "key": False,
                        3.14: complex(1, 2),
                        complex(1, 2): 42,
                        "\n": 4.2,
                        "\\n": datetime.date(2020, 12, 31)}}
        r = encode_data(d)
        expected = """\
                0: "hello world"
                "1": (text)
                    multiline
                    string
                    ---
                "": true
                "key": false
                3.14: 1+2i
                1+2i: 42
                "\\n": 4.2
                "\\\\n": 2020-12-31
                "nested": (dict)
                    0: "hello world"
                    "1": (text)
                        multiline
                        string
                        ---
                    "": true
                    "key": false
                    3.14: 1+2i
                    1+2i: 42
                    "\\n": 4.2
                    "\\\\n": 2020-12-31"""
        self.assertEqual(dedent(expected), r)


class TestList(unittest.TestCase):

    def test_empty_list(self):
        d = {0: list()}
        r = encode_data(d)
        expected = "0: (list)"
        self.assertEqual(expected, r)

    def test_list_with_valid_data(self):
        d = {0: [0, 4.2, "1", True, False, None,
                 complex(1, 2), "hello world",
                 datetime.date(2020, 12, 31),
                 "multiline\ntext"]}
        r = encode_data(d)
        expected = """\
        0: (list)
            0
            4.2
            "1"
            true
            false
            null
            1+2i
            "hello world"
            2020-12-31
            (text)
                multiline
                text
                ---"""
        self.assertEqual(dedent(expected), r)

    def test_nested_list(self):
        d = {0: [0, 4.2, "1", True, False, None,
                 complex(1, 2), "hello world",
                 datetime.date(2020, 12, 31),
                 "multiline\ntext",
                 [0, 4.2, "1", True, False, None,
                  complex(1, 2), "hello world",
                  datetime.date(2020, 12, 31),
                  "multiline\ntext"]]}
        r = encode_data(d)
        expected = """\
        0: (list)
            0
            4.2
            "1"
            true
            false
            null
            1+2i
            "hello world"
            2020-12-31
            (text)
                multiline
                text
                ---
            (list)
                0
                4.2
                "1"
                true
                false
                null
                1+2i
                "hello world"
                2020-12-31
                (text)
                    multiline
                    text
                    ---"""
        self.assertEqual(dedent(expected), r)


class TestSet(unittest.TestCase):

    def test_empty_set(self):
        d = {0: set()}
        r = encode_data(d)
        expected = "0: (set)"
        self.assertEqual(expected, r)

    def test_set_with_valid_data(self):
        d = {0: {0, 4.2, "1",
                 complex(1, 2), "hello world",
                 datetime.date(2020, 12, 31),
                 "multiline\ntext"}}
        r = encode_data(d)
        expected = """\
        0: (set)
            0
            4.2
            "1"
            1+2i
            "hello world"
            2020-12-31
            (text)
                multiline
                text
                ---"""
        self.assertEqual(len(dedent(expected)), len(r))

    def test_set_with_invalid_data(self):
        d = {0: {0, 4.2, "1", True, False, None,
                 complex(1, 2), "hello world",
                 datetime.date(2020, 12, 31),
                 "multiline\ntext"}}
        with self.assertRaises(errors.Error):
            encode_data(d)


class TestObj(unittest.TestCase):

    def test_empty_obj(self):
        d = {0: xtypes.Obj()}
        r = encode_data(d)
        expected = "0: (obj)"
        self.assertEqual(expected, r)

    def test_obj_with_valid_keys(self):
        # are valid keys: integer (int, xtypes.HexInt, ...),
        # float, complex and string (str, xtypes.Raw)
        x = {0: None,
             "1": None,
             "": None,
             "key": None,
             3.14: None,
             complex(1, 2): None,
             "\n": None,
             "\\n": None}
        d = {0: xtypes.Obj(x)}
        r = encode_data(d)
        expected = """\
        0: (obj)
            0: null
            "1": null
            "": null
            "key": null
            3.14: null
            1+2i: null
            "\\n": null
            "\\\\n": null"""
        self.assertEqual(dedent(expected), r)

    def test_obj_with_valid_values(self):
        x = {0: "hello world",
             1: "multiline\nstring",
             2: True,
             3: False,
             4: complex(1, 2),
             5: 42,
             6: 4.2,
             7: datetime.date(2020, 12, 31)}
        d = {0: xtypes.Obj(x)}
        r = encode_data(d)
        expected = """\
        0: (obj)
            0: "hello world"
            1: (text)
                multiline
                string
                ---
            2: true
            3: false
            4: 1+2i
            5: 42
            6: 4.2
            7: 2020-12-31"""
        self.assertEqual(dedent(expected), r)

    def test_obj_with_invalid_keys(self):
        x1 = {None: None}
        x2 = {True: None}
        x3 = {datetime.datetime(2020, 12, 31): None}
        for i, x in enumerate((x1, x2, x3)):
            d = {0: xtypes.Obj(x)}
            with self.subTest("Test {}".format(i + 1)):
                with self.assertRaises(errors.Error):
                    encode_data(d, mode=const.CONFIG_MODE)

    def test_nested_obj(self):
        x = {0: "hello world",
             "1": "multiline\nstring",
             "": True,
             "key": False,
             3.14: complex(1, 2),
             complex(1, 2): 42,
             "\n": 4.2,
             "\\n": datetime.date(2020, 12, 31),
             "nested": xtypes.Obj({0: "hello world",
                        "1": "multiline\nstring",
                        "": True,
                        "key": False,
                                   3.14: complex(1, 2),
                                   complex(1, 2): 42,
                        "\n": 4.2,
                        "\\n": datetime.date(2020, 12, 31)})}
        d = {0: xtypes.Obj(x)}
        r = encode_data(d)
        expected = """\
                0: (obj)
                    0: "hello world"
                    "1": (text)
                        multiline
                        string
                        ---
                    "": true
                    "key": false
                    3.14: 1+2i
                    1+2i: 42
                    "\\n": 4.2
                    "\\\\n": 2020-12-31
                    "nested": (obj)
                        0: "hello world"
                        "1": (text)
                            multiline
                            string
                            ---
                        "": true
                        "key": false
                        3.14: 1+2i
                        1+2i: 42
                        "\\n": 4.2
                        "\\\\n": 2020-12-31"""
        self.assertEqual(dedent(expected), r)


class TestGrid(unittest.TestCase):

    def test_valid_grid(self):
        x = [(0, 1, 2.3, 4 + 5j, xtypes.HexInt("0xffff_ffff")),
             (0, 1, 2.3, 4 + 5j, xtypes.BinInt("0b0000_1111")),
             (0, 1, 2.3, 4 + 5j, xtypes.OctInt("0o0_000_777"))]
        d = {0: xtypes.Grid(x)}
        r = encode_data(d)
        expected = """\
        0: (grid)
            0 1 2.3 4+5i 0xFFFF_FFFF
            0 1 2.3 4+5i 0b0000_1111
            0 1 2.3 4+5i 0o0_000_777"""
        self.assertEqual(dedent(expected), r)

    def test_inconsistent_grid(self):
        x = [(0, 1, 2.3, 4 + 5j, xtypes.HexInt("0xff"), xtypes.HexInt("0xff")),
             (0, 1, 2.3, 4 + 5j, xtypes.HexInt("0xff")),
             (0, 1, 2.3, 4 + 5j, xtypes.HexInt("0xff"))]
        d = {0: xtypes.Grid(x)}
        with self.assertRaises(errors.Error):
            encode_data(d)

    def test_invalid_grid(self):
        x = [("a", "b", "c", "d", xtypes.HexInt("0xff")),
             (0, 1, 2.3, 4 + 5j, xtypes.HexInt("0xff")),
             (0, 1, 2.3, 4 + 5j, xtypes.HexInt("0xff"))]
        d = {0: xtypes.Grid(x)}
        with self.assertRaises(errors.Error):
            encode_data(d)


class TestBool(unittest.TestCase):

    def test_true(self):
        d = {0: True}
        r = encode_data(d)
        expected = "0: true"
        self.assertEqual(expected, r)

    def test_false(self):
        d = {0: False}
        r = encode_data(d)
        expected = "0: false"
        self.assertEqual(expected, r)


class TestNull(unittest.TestCase):

    def test(self):
        d = {0: None}
        r = encode_data(d)
        expected = "0: null"
        self.assertEqual(expected, r)


class TestDatetime(unittest.TestCase):

    def test_naive_datetime_lower_endpoint(self):
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 0001-01-01T00:00:00"
        self.assertEqual(expected, r)

    def test_naive_datetime_upper_endpoint(self):
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 9999-12-31T23:59:59.999999"
        self.assertEqual(expected, r)

    def test_aware_datetime_lower_endpoint(self):
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=0, minutes=0))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 0001-01-01T00:00:00Z"
        self.assertEqual(expected, r)

    def test_aware_datetime_upper_endpoint(self):
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=23, minutes=59))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 9999-12-31T23:59:59.999999+23:59"
        self.assertEqual(expected, r)

    def test_aware_datetime_with_negative_negative_utc_timezone(self):
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=-1, minutes=-30))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 9999-12-31T23:59:59.999999-01:30"
        self.assertEqual(expected, r)


class TestDate(unittest.TestCase):

    def test_date_lower_endpoint(self):
        year, month, day = 1, 1, 1
        val = datetime.date(year=year, month=month, day=day)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 0001-01-01"
        self.assertEqual(expected, r)

    def test_date_upper_endpoint(self):
        year, month, day = 9999, 12, 31
        val = datetime.date(year=year, month=month, day=day)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 9999-12-31"
        self.assertEqual(expected, r)


class TestTime(unittest.TestCase):

    def test_naive_time_lower_endpoint(self):
        hour, minute = 0, 0
        second, microsecond = 0, 0
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 00:00:00"
        self.assertEqual(expected, r)

    def test_naive_time_upper_endpoint(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 23:59:59.999999"
        self.assertEqual(expected, r)

    def test_aware_time_lower_endpoint(self):
        hour, minute = 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=0, minutes=0))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 00:00:00+00:00"
        self.assertEqual(expected, r)

    def test_aware_time_upper_endpoint(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=23, minutes=59))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 23:59:59.999999+23:59"
        self.assertEqual(expected, r)

    def test_aware_time_with_negative_negative_utc_timezone(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=-1, minutes=-30))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        d = {0: val}
        r = encode_data(d)
        expected = "0: 23:59:59.999999-01:30"
        self.assertEqual(expected, r)


class TestInteger(unittest.TestCase):

    def test_positive_int(self):
        d = {0: 10_000_000_000}
        r = encode_data(d)
        expected = "0: 10_000_000_000"
        self.assertEqual(expected, r)

    def test_negative_int(self):
        d = {0: -10_000_000_000}
        r = encode_data(d)
        expected = "0: -10_000_000_000"
        self.assertEqual(expected, r)

    def test_positive_hex_int(self):
        x = 2**32-1
        d = {0: xtypes.HexInt(x)}
        r = encode_data(d)
        expected = "0: 0xFFFF_FFFF"
        self.assertEqual(expected, r)

    def test_negative_hex_int(self):
        x = -(2**32-1)
        d = {0: xtypes.HexInt(x)}
        r = encode_data(d)
        expected = "0: -0xFFFF_FFFF"
        self.assertEqual(expected, r)

    def test_positive_oct_int(self):
        x = 2**32-1
        d = {0: xtypes.OctInt(x)}
        r = encode_data(d)
        expected = "0: 0o37_777_777_777"
        self.assertEqual(expected, r)

    def test_negative_oct_int(self):
        x = -(2**32-1)
        d = {0: xtypes.OctInt(x)}
        r = encode_data(d)
        expected = "0: -0o37_777_777_777"
        self.assertEqual(expected, r)

    def test_positive_bin_int(self):
        x = 2**8-1
        d = {0: xtypes.BinInt(x)}
        r = encode_data(d)
        expected = "0: 0b1111_1111"
        self.assertEqual(expected, r)

    def test_negative_bin_int(self):
        x = -(2**8-1)
        d = {0: xtypes.BinInt(x)}
        r = encode_data(d)
        expected = "0: -0b1111_1111"
        self.assertEqual(expected, r)


class TestIntWithLeadingZeros(unittest.TestCase):

    def test_hex(self):
        d = {0: xtypes.HexInt("-0x0000_FFFF")}
        r = encode_data(d)
        expected = "0: -0x0000_FFFF"
        self.assertEqual(expected, r)

    def test_oct(self):
        d = {0: xtypes.OctInt("-0o000_777")}
        r = encode_data(d)
        expected = "0: -0o000_777"
        self.assertEqual(expected, r)

    def test_bin(self):
        d = {0: xtypes.BinInt("-0b0000_1111")}
        r = encode_data(d)
        expected = "0: -0b0000_1111"
        self.assertEqual(expected, r)


class TestFloat(unittest.TestCase):

    def test_positive_float(self):
        d = {0: 10_000_000_000.000_01}
        r = encode_data(d)
        expected = "0: 10_000_000_000.000_01"
        self.assertEqual(expected, r)

    def test_negative_float(self):
        d = {0: -10_000_000_000.000_01}
        r = encode_data(d)
        expected = "0: -10_000_000_000.000_01"
        self.assertEqual(expected, r)

    def test_positive_float_with_scientific_notation(self):
        d = {0: float("1e-10")}
        r = encode_data(d)
        expected = "0: 1.0E-10"
        self.assertEqual(expected, r)

    def test_negative_float_with_scientific_notation(self):
        d = {0: float("-1e-10")}
        r = encode_data(d)
        expected = "0: -1.0E-10"
        self.assertEqual(expected, r)


class TestDecimalFloat(unittest.TestCase):

    def test_positive_float(self):
        d = {0: Decimal("1.000_234_56")}
        r = encode_data(d)
        expected = "0: 1.000_234_56"
        self.assertEqual(expected, r)

    def test_negative_float(self):
        d = {0: Decimal("-1.000_234_56")}
        r = encode_data(d)
        expected = "0: -1.000_234_56"
        self.assertEqual(expected, r)

    def test_positive_float_with_scientific_notation(self):
        d = {0: Decimal("1.000_234_56E10")}
        r = encode_data(d)
        expected = "0: 1.000_234_56E10"
        self.assertEqual(expected, r)

    def test_negative_float_with_scientific_notation(self):
        d = {0: Decimal("-1.000_234_56E-10")}
        r = encode_data(d)
        expected = "0: -1.000_234_56E-10"
        self.assertEqual(expected, r)


class TestMultilineNumber(unittest.TestCase):

    def test_int(self):
        d = {0: -1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000}
        r = encode_data(d)
        expected = """\
        0: (int)
            -1_000_000_000_000_000_000_000_000_000_000
            _000_000_000_000_000_000_000_000"""
        self.assertEqual(dedent(expected), r)

    def test_hex_int(self):
        d = {0: xtypes.HexInt("-0x100_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000")}
        r = encode_data(d)
        expected = """\
        0: (int)
            -0x100_0000_0000_0000_0000_0000_0000_0000_
            0000_0000_0000_0000_0000_0000"""
        self.assertEqual(dedent(expected), r)

    def test_oct_int(self):
        d = {0: xtypes.OctInt("-0o1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000")}
        r = encode_data(d)
        expected = """\
        0: (int)
            -0o1_000_000_000_000_000_000_000_000_000_0
            00_000_000_000_000_000_000_000_000"""
        self.assertEqual(dedent(expected), r)

    def test_bin_int(self):
        d = {0: xtypes.BinInt("-0b100_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000")}
        r = encode_data(d)
        expected = """\
        0: (int)
            -0b100_0000_0000_0000_0000_0000_0000_0000_
            0000_0000_0000_0000_0000_0000"""
        self.assertEqual(dedent(expected), r)


    def test_float(self):
        d = {0: Decimal("-1.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_111E-10")}
        r = encode_data(d)
        expected = """\
        0: (float)
            -1.000_000_000_000_000_000_000_000_000_000
            _000_000_000_000_000_000_000_111E-10"""
        self.assertEqual(dedent(expected), r)


class TestComplexNumber(unittest.TestCase):

    def test_1(self):
        d = {0: complex(0, 1)}
        r = encode_data(d)
        expected = "0: 0+1i"
        self.assertEqual(expected, r)

    def test_2(self):
        d = {0: complex(-1, -1)}
        r = encode_data(d)
        expected = "0: -1-1i"
        self.assertEqual(expected, r)

    def test_3(self):
        d = {0: complex(-1.0, -1000.0)}
        r = encode_data(d)
        expected = "0: -1-1_000i"
        self.assertEqual(expected, r)

    def test_4(self):
        d = {0: complex(-1.234_567_89, -1000.0)}
        r = encode_data(d)
        expected = "0: -1.234_567_89-1_000i"
        self.assertEqual(expected, r)

    def test_5(self):
        d = {0: complex(-1.234_567_89E-10, 1.234_567_89E-10)}
        r = encode_data(d)
        expected = "0: -1.234_567_89E-10+1.234_567_89E-10i"
        self.assertEqual(expected, r)


class TestString(unittest.TestCase):

    def test_empty_str(self):
        d = {0: ""}
        r = encode_data(d)
        expected = '0: ""'
        self.assertEqual(expected, r)

    def test_str(self):
        d = {0: "hello \u02eb world"}
        r = encode_data(d)
        expected = '0: "hello ˫ world"'
        self.assertEqual(expected, r)

    def test_str_with_backlash(self):
        d = {0: "hello \u02eb \\ world"}
        r = encode_data(d)
        expected = r"0: 'hello ˫ \ world'"
        self.assertEqual(expected, r)


class TestMultilineString(unittest.TestCase):

    def test_str(self):
        d = {0: "this is \u02eb a\nmultiline string"}
        r = encode_data(d)
        expected = """\
        0: (text)
            this is ˫ a
            multiline string
            ---"""
        self.assertEqual(dedent(expected), r)

    def test_str_with_backlash(self):
        d = {0: "this is \u02eb a\nmultiline \\string"}
        r = encode_data(d)
        expected = """\
        0: (raw)
            this is ˫ a
            multiline \\string
            ---"""
        self.assertEqual(dedent(expected), r)


class TestBin(unittest.TestCase):

    def test_empty_bin_data(self):
        d = {0: b""}
        r = encode_data(d)
        expected = """0: (bin)"""
        self.assertEqual(dedent(expected), r)

    def test_bin_data(self):
        d = {0: b"hello world hello world hello world hello world hello world hello world hello world"}
        r = encode_data(d)
        expected = """\
        0: (bin)
            68 65 6C 6C 6F 20 77 6F 72 6C 64 20 68 65 6C 6C
            6F 20 77 6F 72 6C 64 20 68 65 6C 6C 6F 20 77 6F
            72 6C 64 20 68 65 6C 6C 6F 20 77 6F 72 6C 64 20
            68 65 6C 6C 6F 20 77 6F 72 6C 64 20 68 65 6C 6C
            6F 20 77 6F 72 6C 64 20 68 65 6C 6C 6F 20 77 6F
            72 6C 64"""
        self.assertEqual(dedent(expected), r)


class TestAttachments(unittest.TestCase):

    def setUp(self):
        self._tempdir = tempfile.TemporaryDirectory()
        self._dirname = self._tempdir.name
        self._filename = os.path.join(self._dirname, "my_file.txt")
        self._cached_cwd = os.getcwd()
        os.chdir(self._tempdir.name)

    def tearDown(self):
        os.chdir(self._cached_cwd)
        # the Try/Except is needed here because I can only
        # benefit from the constructor's "ignore_cleanup_errors=True"
        # in Python 3.10
        try:
            self._tempdir.cleanup()
        except Exception as e:
            pass

    def test_default_value(self):
        d = {0: b"hello world hello world hello world hello world hello world hello world hello world"}
        for i in range(1, 6):
            with self.subTest(str(i)):
                with open(self._filename, "w", encoding="utf-8") as file:
                    r = paradict.io_text.encode_into(d, file, bin_to_text=False)
                with open(self._filename, "r", encoding="utf-8") as file:
                    r = file.read()
                expected = """\
                0: load('attachments/{}')\n""".format(str(i))
                self.assertEqual(dedent(expected), r)
                attachment_filename = os.path.join(self._dirname, "attachments", str(i))
                self.assertTrue(os.path.isfile(attachment_filename))

    def test_with_custom_relative_attachments_dirname(self):
        d = {0: b"hello world hello world hello world hello world hello world hello world hello world"}
        for i in range(1, 6):
            with self.subTest(str(i)):
                with open(self._filename, "w", encoding="utf-8") as file:
                    paradict.io_text.encode_into(d, file, bin_to_text=False,
                                                 attachments_dir="my/attachments")
                with open(self._filename, "r", encoding="utf-8") as file:
                    r = file.read()
                expected = """\
                0: load('my/attachments/{}')\n""".format(str(i))
                self.assertEqual(dedent(expected), r)
                attachment_filename = os.path.join(self._dirname, "my",
                                                   "attachments", str(i))
                self.assertTrue(os.path.isfile(attachment_filename))

    def test_with_empty_attachments_dirname(self):
        d = {0: b"hello world hello world hello world hello world hello world hello world hello world"}
        for i in range(1, 6):
            with self.subTest(str(i)):
                with open(self._filename, "w", encoding="utf-8") as file:
                    paradict.io_text.encode_into(d, file, bin_to_text=False,
                                                 attachments_dir=None)
                with open(self._filename, "r", encoding="utf-8") as file:
                    r = file.read()
                attachment_filename = os.path.join(self._dirname, str(i))
                expected = """\
                0: load('{}')\n""".format(str(i))
                self.assertEqual(dedent(expected), r)
                self.assertTrue(os.path.isfile(attachment_filename))


def encode_data(data, **kwargs):
    return serializer.encode(data, **kwargs)


if __name__ == "__main__":
    unittest.main()
