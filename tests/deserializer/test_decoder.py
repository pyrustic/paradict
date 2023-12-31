import unittest
import datetime
from textwrap import dedent
from paradict import box, errors, deserializer
from paradict.serializer.encoder import Encoder


class TestEmptyData(unittest.TestCase):

    def test(self):
        d = ""
        r = decode_data(dedent(d))
        expected = dict()
        self.assertEqual(expected, r)


class TestDictInConfigMode(unittest.TestCase):

    def test_valid_dict(self):
        d = """\
        a_valid_key_42 = (dict)
            another_key = 42
            null = null
            true = true
        """
        r = decode_data(dedent(d))
        expected = {"a_valid_key_42": {"another_key": 42,
                                       "null": None,
                                       "true": True}}
        self.assertEqual(expected, r)

    def test_invalid_dict(self):
        d1 = """4 2 = null"""
        d2 = """4.2 = null"""
        d3 = """1+2i = null"""
        for i, d in enumerate((d1, d2, d3)):
            with self.subTest("Test {}".format(i + 1)):
                with self.assertRaises(errors.Error):
                    decode_data(dedent(d))

    def test_malformed_dict_key(self):
        d1 = """key_42= = null"""
        d2 = """1 key_42 = null"""
        for i, d in enumerate((d1, d2)):
            with self.subTest("Test {}".format(i + 1)):
                with self.assertRaises(errors.Error):
                    r = decode_data(dedent(d))
                    expected = {0: dict()}
                    self.assertEqual(expected, r)


class TestDict(unittest.TestCase):

    def test_empty_dict(self):
        d = """\
        0: (dict)
        """
        r = decode_data(dedent(d))
        expected = {0: dict()}
        self.assertEqual(expected, r)

    def test_dict_with_valid_keys(self):
        d = """\
        0: null
        "1": null
        "": null
        "key": null
        3.14: null
        1+2i: null
        "\\n": null
        "\\\\n": null
        """
        r = decode_data(dedent(d))
        expected = {0: None,
                    "1": None,
                    "": None,
                    "key": None,
                    3.14: None,
                    complex(1, 2): None,
                    "\n": None,
                    "\\n": None}
        self.assertEqual(expected, r)

    def test_dict_with_valid_values(self):
        d = """\
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
        7: 2020-12-31
        """
        r = decode_data(dedent(d))
        expected = {0: "hello world",
                    1: "multiline\nstring",
                    2: True,
                    3: False,
                    4: complex(1, 2),
                    5: 42,
                    6: 4.2,
                    7: datetime.date(2020, 12, 31)}
        self.assertEqual(expected, r)

    def test_dict_with_invalid_keys(self):
        d1 = """key_42: null"""
        d2 = """2020-12-31: null"""
        d3 = """10:12:59 : null"""
        d4 = """null : null"""
        d5 = """true : null"""
        for i, d in enumerate((d1, d2, d3, d4, d5)):
            with self.subTest("Test {}".format(i + 1)):
                with self.assertRaises(errors.Error):
                    decode_data(dedent(d))

    def test_nested_dict(self):
        d = """\
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
            "\\\\n": 2020-12-31
        """
        r = decode_data(dedent(d))
        expected = {0: "hello world",
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
        self.assertEqual(expected, r)


class TestList(unittest.TestCase):

    def test_empty_list(self):
        d = """\
        0: (list)
        """
        r = decode_data(dedent(d))
        expected = {0: list()}
        self.assertEqual(expected, r)

    def test_list_with_valid_data(self):
        d = """\
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
        """
        r = decode_data(dedent(d))
        expected = {0: [0,
                        4.2,
                        "1",
                        True,
                        False,
                        None,
                        complex(1, 2),
                        "hello world",
                        datetime.date(2020, 12, 31),
                        "multiline\ntext"]}
        self.assertEqual(expected, r)

    def test_nested_list(self):
        d = """\
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
                    ---
        """
        r = decode_data(dedent(d))
        expected = {0: [0,
                        4.2,
                        "1",
                        True,
                        False,
                        None,
                        complex(1, 2),
                        "hello world",
                        datetime.date(2020, 12, 31),
                        "multiline\ntext",
                        [0,
                         4.2,
                         "1",
                         True,
                         False,
                         None,
                         complex(1, 2),
                         "hello world",
                         datetime.date(2020, 12, 31),
                         "multiline\ntext"]]}
        self.assertEqual(expected, r)


class TestSet(unittest.TestCase):

    def test_empty_set(self):
        d = """\
        0: (set)
        """
        r = decode_data(dedent(d))
        expected = {0: set()}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], set)

    def test_set_deletable(self):
        d = """\
        0: (set)
            (text)
                multiline
                text
                ---
        """
        r = decode_data(dedent(d))
        expected = {0: {"multiline\ntext"}}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], set)

    def test_set_with_valid_data(self):
        d = """\
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
                ---
        """
        r = decode_data(dedent(d))
        expected = {0: {0,
                        4.2,
                        "1",
                        complex(1, 2),
                        "hello world",
                        datetime.date(2020, 12, 31),
                        "multiline\ntext"}}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], set)


class TestObj(unittest.TestCase):

    def test_empty_obj(self):
        d = """\
        0: (obj)
        """
        r = decode_data(dedent(d))
        expected = {0: box.Obj()}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], box.Obj)

    def test_obj_with_valid_keys(self):
        d = """\
        0: (obj)
            0: null
            "1": null
            "": null
            "key": null
            3.14: null
            1+2i: null
            "\\n": null
            "\\\\n": null
        """
        r = decode_data(dedent(d))
        expected = {0: box.Obj({0: None,
                                "1": None,
                                "": None,
                                "key": None,
                                3.14: None,
                                complex(1, 2): None,
                                "\n": None,
                                "\\n": None})}
        self.assertEqual(expected, r)

    def test_obj_with_valid_values(self):
        d = """\
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
            7: 2020-12-31
        """
        r = decode_data(dedent(d))
        expected = {0: box.Obj({0:"hello world",
                                1: "multiline\nstring",
                                2: True,
                                3: False,
                                4: complex(1, 2),
                                5: 42,
                                6: 4.2,
                                7: datetime.date(2020, 12, 31)})}
        self.assertEqual(expected, r)

    def test_obj_with_invalid_keys(self):
        d1 = """\
        0: (obj)
            key_42: null
        """
        d2 = """\
        0: (obj)
            2020-12-31: null
        """
        d3 = """\
        0: (obj)
            10:12:59 : null
        """
        d4 = """\
        0: (obj)
            null : null
        """
        d5 = """\
        0: (obj)
            true : null
        """
        for i, d in enumerate((d1, d2, d3, d4, d5)):
            with self.subTest("Test {}".format(i + 1)):
                with self.assertRaises(errors.Error):
                    decode_data(dedent(d))

    def test_nested_obj(self):
        d = """\
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
        """
        r = decode_data(dedent(d))
        expected = {0: "hello world",
                    "1": "multiline\nstring",
                    "": True,
                    "key": False,
                    3.14: complex(1, 2),
                    complex(1, 2): 42,
                    "\n": 4.2,
                    "\\n": datetime.date(2020, 12, 31),
                    "nested": box.Obj({0: box.Obj({0: "hello world",
                               "1": "multiline\nstring",
                               "": True,
                               "key": False,
                               3.14: complex(1, 2),
                               complex(1, 2): 42,
                               "\n": 4.2,
                               "\\n": datetime.date(2020, 12, 31)})})}
        self.assertEqual(expected, r)


class TestObjBuilder(unittest.TestCase):

    def test_simple_obj(self):
        d = """\
        0: (obj)
            'type': 'complex'
            'real': -3.14
            'imag': 4.2
        """
        r = decode_data(dedent(d),
                        obj_builder=lambda obj:
                          complex(obj["real"], obj["imag"]))
        expected = {0: complex(-3.14, 4.2)}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], complex)

    def test_nested_obj(self):
        d = """\
        0: (obj)
            'type': 'complex'
            'real': (obj)
                'type': 'number'
                'x': -3.14
            'imag': (obj)
                'type': 'number'
                'x': 4.2
        """
        r = decode_data(dedent(d), obj_builder=my_obj_builder)
        expected = {0: complex(-3.14, 4.2)}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], complex)


class TestGrid(unittest.TestCase):

    def test_empty_grid(self):
        d = """\
        0: (grid)
        """
        r = decode_data(dedent(d))
        expected = {0: box.Grid()}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], box.Grid)

    def test_with_integer(self):  #
        d = """\
        0: (grid)
            0 1 2
            3 4 5_000_000_000
            6 7 -8
        """
        r = decode_data(dedent(d))
        my_grid = [(0, 1, 2),
                   (3, 4, 5_000_000_000),
                   (6, 7, -8)]
        expected = {0: my_grid}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], box.Grid)

    def test_with_float(self):
        d = """\
        0: (grid)
            0.0 1.1 -2.2_000_000_000
        """
        r = decode_data(dedent(d))
        my_grid = [(0.0, 1.1, -2.2_000_000_000)]
        expected = {0: my_grid}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], box.Grid)

    def test_with_complex(self):
        d = """\
        0: (grid)
            1+2i 3+4.5_000_000_000i
        """
        r = decode_data(dedent(d))
        my_grid = [(1+2j, 3+4.5_000_000_000j)]
        expected = {0: my_grid}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], box.Grid)

    def test_with_illegal_data(self):
        d = """\
        0: (grid)
            "a" "b"
        """
        with self.assertRaises(errors.Error):
            decode_data(dedent(d))


class TestComment(unittest.TestCase):

    def test_empty_comment(self):
        d = """\
        #
        #
        0: (dict)
            #
            #
            0: (list)
                #
                #
                (obj)
                    #
                    #
                    0: (set)
                        #"""
        r = decode_encode(dedent(d), skip_comments=False)
        self.assertEqual(dedent(d), r)

    def test_regular_comment(self):
        d = """\
        # comment 1
        0: (dict)
            # comment 2
            0: (list)
                # comment 3
                (obj)
                    # comment 4
                    0: (set)
                        # comment 5"""
        r = decode_encode(dedent(d), skip_comments=False)
        self.assertEqual(dedent(d), r)


class TestDatetime(unittest.TestCase):

    def test_naive_datetime_lower_endpoint(self):
        d = """0: 0001-01-01T00:00:00"""
        r = decode_data(d)
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_naive_datetime_upper_endpoint(self):
        d = "0: 9999-12-31T23:59:59.999999"
        r = decode_data(d)
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_aware_datetime_lower_endpoint(self):
        d = "0: 0001-01-01T00:00:00Z"
        r = decode_data(d)
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=0, minutes=0))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_aware_datetime_upper_endpoint(self):
        d = "0: 9999-12-31T23:59:59.999999+23:59"
        r = decode_data(d)
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=23, minutes=59))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_aware_datetime_with_negative_negative_utc_timezone(self):
        d = "0: 9999-12-31T23:59:59.999999-01:30"
        r = decode_data(d)
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=-1, minutes=-30))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        expected = {0: val}
        self.assertEqual(expected, r)


class TestDate(unittest.TestCase):

    def test_date_lower_endpoint(self):
        d = """0: 0001-01-01"""
        r = decode_data(dedent(d))
        year, month, day = 1, 1, 1
        val = datetime.date(year=year, month=month, day=day)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_date_upper_endpoint(self):
        d = """0: 9999-12-31"""
        r = decode_data(dedent(d))
        year, month, day = 9999, 12, 31
        val = datetime.date(year=year, month=month, day=day)
        expected = {0: val}
        self.assertEqual(expected, r)


class TestTime(unittest.TestCase):

    def test_naive_time_lower_endpoint(self):
        d = """0: 00:00:00"""
        r = decode_data(d)
        hour, minute = 0, 0
        second, microsecond = 0, 0
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_naive_time_upper_endpoint(self):
        d = "0: 23:59:59.999999"
        r = decode_data(d)
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_aware_time_lower_endpoint(self):
        d = "0: 00:00:00Z"
        r = decode_data(d)
        hour, minute = 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=0, minutes=0))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_aware_time_upper_endpoint(self):
        d = "0: 23:59:59.999999+23:59"
        r = decode_data(d)
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=23, minutes=59))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        expected = {0: val}
        self.assertEqual(expected, r)

    def test_aware_time_with_negative_negative_utc_timezone(self):
        d = "0: 23:59:59.999999-01:30"
        r = decode_data(d)
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=-1, minutes=-30))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        expected = {0: val}
        self.assertEqual(expected, r)


class TestNull(unittest.TestCase):

    def test(self):
        d = """\
        0: null
        """
        r = decode_data(dedent(d))
        expected = {0: None}
        self.assertEqual(expected, r)


class TestBool(unittest.TestCase):

    def test(self):
        d = """\
        0: true
        1: false
        """
        r = decode_data(dedent(d))
        expected = {0: True, 1: False}
        self.assertEqual(expected, r)


class TestBin(unittest.TestCase):

    def test(self):
        d = """\
        0: (bin)
            48 65 6C 6C 6F 20 57 6F 72 6C 64 20 21 20 48 65
            6C 6C 6F 20 57 6F 72 6C 64 20 21
        1: (bin)"""
        bin_hello = b'Hello World ! Hello World !'
        r = decode_data(dedent(d))
        expected = {0: bin_hello, 1: b''}
        self.assertEqual(expected, r)


class TestInt(unittest.TestCase):

    def test_int(self):
        d = """\
        0: (list)
            0
            1
            2_000_000
        """
        r = decode_data(dedent(d))
        expected = {0: [0, 1, 2_000_000]}
        self.assertEqual(expected, r)

    def test_hex_oct_bin_int(self):
        d = """\
        0: (list)
            0xffff_ffff
            0o37_777_777_777
            0b1111_1111_1111_1111_1111_1111_1111_1111
        """
        r = decode_data(dedent(d))
        x = 2**32-1
        expected = {0: [box.HexInt(x),
                        box.OctInt(x),
                        box.BinInt(x)]}
        self.assertEqual(expected, r)


class TestFloat(unittest.TestCase):

    def test(self):
        d = """\
        0: (list)
            0.0
            1.0
            2_000_000.000_001
            3.14E10
            3.14E-10
            3.000001
            0.0004
            0.0009E10
            -0.0009E-10
        """
        r = decode_data(dedent(d))
        expected = {0: [float("0.0"),
                        float("1.0"),
                        float("2_000_000.000_001"),
                        float("3.14E10"),
                        float("3.14E-10"),
                        float("3.000001"),
                        float("0.0004"),
                        float("0.0009E10"),
                        float("-0.0009E-10")]}
        self.assertEqual(expected, r)


class TestComplex(unittest.TestCase):

    def test(self):
        d = """\
        0: (list)
            1+2i
            -3-4i
            2_000_000i
            3.14+1i
        """
        r = decode_data(dedent(d))
        expected = {0: [complex(1, 2),
                        complex(-3, -4),
                        complex(0, 2000000),
                        complex(3.14, 1)]}
        self.assertEqual(expected, r)

    def test_hex_oct_bin_int(self):
        d = """\
        0: (list)
            0xffff_ffff
            0o37_777_777_777
            0b1111_1111_1111_1111_1111_1111_1111_1111
        """
        r = decode_data(dedent(d))
        x = 2**32-1
        expected = {0: [box.HexInt(x),
                        box.OctInt(x),
                        box.BinInt(x)]}
        self.assertEqual(expected, r)


class TestString(unittest.TestCase):

    def test_ordinary_str(self):
        d = """\
        0: (list)
            "hello˫ world\\u02eb"
            "hello \\n world"
            "hello \\\\ world\\\\u02eb"
        """
        r = decode_data(dedent(d))
        expected = {0: ["hello˫ world\u02eb", "hello \n world",
                        "hello \\ world\\u02eb"]}
        self.assertEqual(expected, r)

    def test_raw_str(self):
        d = """\
        0: (list)
            'hello˫ world\\u02eb'
            'hello \\n world'
            'hello \\\\ world\\\\u02eb'
        """
        r = decode_data(dedent(d))
        expected = {0: ["hello˫ world\\u02eb", "hello \\n world",
                        "hello \\\\ world\\\\u02eb"]}
        self.assertEqual(expected, r)


class TestMultilineString(unittest.TestCase):

    def test_ordinary_str(self):
        d = """\
        0: (text)
            Hello˫ world
               ***
                ***
            This\\u02eb is a \\n multiline
            string\\\\
            .
            
            
            ---
        """
        r = decode_data(dedent(d))
        expected = {0: "Hello˫ world\n   ***\n    ***\n"
                       "This\u02eb is a \n multiline\nstring\\\n.\n\n"}
        self.assertEqual(expected, r)

    def test_raw_str(self):
        d = """\
        0: (raw)
            Hello˫ world
               ***
                ***
            This\\u02eb is a \\n multiline
            string\\\\
            .


            ---
        """
        r = decode_data(dedent(d))
        expected = {0: "Hello˫ world\n   ***\n    ***\n"
                       "This\\u02eb is a \\n multiline\nstring\\\\\n.\n\n"}
        self.assertEqual(expected, r)


class TestRaw(unittest.TestCase):

    def test_raw_string(self):
        d = """\
        0: (list)
            'hello˫ world\\u02eb'
            'hello \\n world'
            'hello \\ world\\\\u02eb'
        """
        r = decode_data(dedent(d))
        expected = {0: ["hello˫ world\\u02eb", "hello \\n world",
                        "hello \\ world\\\\u02eb"]}
        self.assertEqual(expected, r)
        for i, item in enumerate(r[0]):
            with self.subTest("subtest index: {}".format(i)):
                self.assertEqual(str, type(item))

    def test_multiline_raw_string(self):
        d = """\
        0: (raw)
            Hello˫ world
               ***
                ***
            This\\u02eb is a \\n multiline
            string\\
            .
            
            
            ---
        """
        r = decode_data(dedent(d))
        expected = {0: "Hello˫ world\n   ***\n    ***\n"
                       "This\\u02eb is a \\n multiline\nstring\\\n.\n\n"}
        self.assertEqual(expected, r)


class TestCommand(unittest.TestCase):

    def test_cmd(self):
        d = """\
        0: (list)
            `my --command 
            `hello˫ world\\u02eb
            `hello \\n world
            `hello \\\\ world\\\\u02eb
        """
        r = decode_data(dedent(d))
        expected = {0: ["my --command",
                        "hello˫ world\u02eb",
                        "hello \n world",
                        "hello \\ world\\u02eb"]}
        self.assertEqual(expected, r)
        for item in r[0]:
            with self.subTest():
                self.assertIsInstance(item, box.Command)


class TestMultilineCommand(unittest.TestCase):

    def test_cmd(self):
        d = """\
        0: (cmd)
            Hello˫ world
               ***
                ***
            This\\u02eb is a \\n multiline
            command\\\\
            .


        """
        r = decode_data(dedent(d))
        expected = {0: "Hello˫ world\n   ***\n    ***\n"
                       "This\u02eb is a \n multiline\ncommand\\\n."}
        self.assertEqual(expected, r)
        self.assertIsInstance(r[0], box.Command)


def decode_data(s, **kwargs):
    return deserializer.decode(s, **kwargs)


def decode_encode(s, **kwargs):
    data = decode_data(s, **kwargs)
    buffer = list()
    encoder = Encoder(**kwargs)
    for line in encoder.encode(data):
        buffer.append(line)
    return "\n".join(buffer)


def my_obj_builder(obj):
    datatype = obj["type"]
    if datatype == "number":
        return obj["x"]
    elif datatype == "complex":
        return complex(obj["real"], obj["imag"])


if __name__ == '__main__':
    unittest.main()
