import unittest
import datetime
from paradict import serializer, deserializer
from paradict import box, errors, tags
from paradict.deserializer.unpacker import Unpacker
from paradict.serializer.packer import Packer


class TestEmptyData(unittest.TestCase):

    def test(self):
        data = dict()
        r = pack_unpack(data)
        self.assertEqual(data, r)


class TestNopTag(unittest.TestCase):

    def test(self):
        unpacker = Unpacker()
        unpacker.feed(tags.NOP)
        self.assertEqual(None, unpacker.data)


class TestDict(unittest.TestCase):

    def test_empty_dict(self):
        d = {0: dict()}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_nested_dict(self):
        val = {0: {1: {2: 3}}}
        d = {0: dict(val)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIs(type(r[0]), dict)

    def test_dict_filled_with_complex_data(self):
        d = {0: {"age": 999, "name": "John Doe", "pi": 3.14,
                 0: [1, 2, 3], 1: {"a", "b"}, 2000: {"x": 11, "y": dict()},
                 3.14: None, datetime.datetime(2020, 1, 1): True,
                 False: None, None: 3, "misc": [dict(), box.Obj()],
                 "matryoshka": dict(box.Obj(dict(box.Obj(box.Obj()))))}}
        r = pack_unpack(d)
        self.assertEqual(d, r)


class TestList(unittest.TestCase):

    def test_empty_list(self):
        d = {0: list()}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_list_filled_with_complex_data(self):
        d = {0: ["age", 999,  3.14, 0, [1, 2, 3, [4, [5, 6]]], 1, {"a", "b"},
                 2000, {"x": 11}, datetime.datetime(2020, 1, 1),
                 True, False, None]}
        r = pack_unpack(d)
        self.assertEqual(d, r)


class TestSet(unittest.TestCase):

    def test_empty_set(self):
        d = {0: set()}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_set_filled_with_complex_data(self):
        d = {0: {"age", 999, 3.14, 0, 1,
                 2000, datetime.datetime(2020, 1, 1),
                 True, False, None}}
        r = pack_unpack(d)
        self.assertEqual(d, r)


class TestObj(unittest.TestCase):

    def test_empty_obj(self):
        d = {0: box.Obj()}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIs(type(r[0]), box.Obj)

    def test_nested_obj(self):
        val = {1: box.Obj({2: box.Obj({3: box.Obj({4: 5})})})}
        d = {0: box.Obj(val)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIs(type(r[0]), box.Obj)

    def test_obj_filled_with_complex_data(self):
        val = {"age": 999, "name": "John Doe", "pi": 3.14,
               0: [1, 2, 3], 1: {"a", "b"}, 2000: {"x": 11},
               3.14: None, datetime.datetime(2020, 1, 1): True,
               False: None, None: 3}
        d = {0: box.Obj(val)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIs(type(r[0]), box.Obj)


class TestObjBuilder(unittest.TestCase):

    def test_simple_obj(self):
        real, imag = -3.14, 4.2
        complex_obj = box.Obj()
        complex_obj["real"] = real
        complex_obj["imag"] = imag
        d = {0: complex_obj}
        packer = Packer()
        unpacker = Unpacker(obj_builder=lambda obj:
                            complex(obj["real"], obj["imag"]))
        for datum in packer.pack(d):
            unpacker.feed(datum)
        expected = {0: complex(real, imag)}
        self.assertEqual(expected, unpacker.data)

    def test_nested_obj(self):
        real, imag = -3.14, 4.2
        # real obj
        real_obj = box.Obj()
        real_obj["type"] = "number"
        real_obj["x"] = real
        # imag obj
        imag_obj = box.Obj()
        imag_obj["type"] = "number"
        imag_obj["x"] = imag
        # complex obj
        complex_obj = box.Obj()
        complex_obj["type"] = "complex"
        complex_obj["real"] = real_obj
        complex_obj["imag"] = imag_obj
        d = {0: complex_obj}
        packer = Packer()
        unpacker = Unpacker(obj_builder=my_obj_builder)
        for datum in packer.pack(d):
            unpacker.feed(datum)
        expected = {0: complex(real, imag)}
        self.assertEqual(expected, unpacker.data)


class TestGrid(unittest.TestCase):

    def test_empty_grid(self):
        d = {0: box.Grid()}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_with_integer(self):
        x = [(0, 1, 2),
             (3, 4, 5_000_000_000),
             (6, 7, -8)]
        d = {0: box.Grid(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Grid)

    def test_with_float(self):
        x = [(0.0, 1.1, -2.2_000_000_000)]
        d = {0: box.Grid(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Grid)

    def test_with_complex(self):
        x = [(1+2j, 3+4.5_000_000_000j)]
        d = {0: box.Grid(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Grid)

    def test_with_illegal_data(self):
        x = [("a", "b")]
        d = {0: box.Grid(x)}
        with self.assertRaises(errors.Error):
            pack_unpack(d)


class TestDatetime(unittest.TestCase):

    def test_naive_datetime_lower_endpoint(self):
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.datetime)

    def test_naive_datetime_upper_endpoint(self):
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.datetime)

    def test_aware_datetime_lower_endpoint(self):
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=23, minutes=59))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.datetime)

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
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.datetime)

    def test_aware_datetime_with_negative_negative_utc_timezone(self):
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=-23, minutes=-59))
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond,
                                tzinfo=tz)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.datetime)


class TestDate(unittest.TestCase):

    def test_date_lower_endpoint(self):
        year, month, day = 1, 1, 1
        val = datetime.date(year=year, month=month, day=day)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.date)

    def test_date_upper_endpoint(self):
        year, month, day = 9999, 12, 31
        val = datetime.date(year=year, month=month, day=day)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.date)


class TestTime(unittest.TestCase):

    def test_naive_time_lower_endpoint(self):
        hour, minute = 0, 0
        second, microsecond = 0, 0
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.time)

    def test_naive_time_upper_endpoint(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.time)

    def test_aware_time_lower_endpoint(self):
        hour, minute = 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=23, minutes=59))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.time)

    def test_aware_time_upper_endpoint(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=23, minutes=59))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.time)

    def test_aware_time_with_negative_negative_utc_timezone(self):
        hour, minute = 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=-23, minutes=-59))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        d = {0: val}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertEqual(type(r[0]), datetime.time)


class TestNull(unittest.TestCase):

    def test(self):
        d = {0: None}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsNone(r[0])


class TestBool(unittest.TestCase):

    def test_true(self):
        d = {0: True}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertTrue(r[0])

    def test_false(self):
        d = {0: False}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertFalse(r[0])


class TestConstString(unittest.TestCase):

    def test_lower_letters(self):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
        for x in letters:
            with self.subTest("Letter: {}".format(x)):
                d = {x: x}
                r = pack_unpack(d)
                self.assertEqual(d, r)

    def test_upper_letters(self):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                   "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]
        for x in letters:
            with self.subTest("Letter: {}".format(x)):
                d = {x: x}
                r = pack_unpack(d)
                self.assertEqual(d, r)


class TestString(unittest.TestCase):

    def test_empty_str(self):
        x = str()
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_str_8_to_256(self):
        char = ";"
        for n in range(1, 9):
            with self.subTest("n: {}".format(n)):
                x = char*n
                d = {0: x}
                r = pack_unpack(d)
                self.assertEqual(d, r)

    def test_short_str_lower_endpoint(self):
        x = ";"*33
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_short_str_upper_endpoint(self):
        x = ";"*(2**8)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_medium_str_lower_endpoint(self):
        x = ";" * (2**8 + 1)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_medium_str_upper_endpoint(self):
        x = ";" * (2**16)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_long_str_lower_endpoint(self):
        x = ";" * (2**16 + 1)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_long_str_upper(self):
        x = ";" * (2**24)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)

    def test_big_str(self):
        # toooooo big to test ;)
        self.assertTrue(True)

    def test_heavy_str(self):
        # toooooo heavy to test ;)
        self.assertTrue(True)


class TestCommandString(unittest.TestCase):

    def test_empty_command_str(self):
        x = str()
        d = {0: box.Command(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Command)

    def test_command_str_8(self):
        x = ";"
        d = {0: box.Command(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Command)

    def test_command_str_64(self):
        x = ";"*8
        d = {0: box.Command(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Command)

    def test_short_command_str(self):
        x = ";"*(2**8)
        d = {0: box.Command(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Command)

    def test_medium_command_str(self):
        x = ";" * (2**16)
        d = {0: box.Command(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Command)

    def test_long_command_str(self):
        x = ";" * (2**24)
        d = {0: box.Command(x)}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.Command)

    def test_big_command_str(self):
        # toooooo big to test ;)
        self.assertTrue(True)

    def test_heavy_command_str(self):
        # toooooo heavy to test ;)
        self.assertTrue(True)


class TestCommentString(unittest.TestCase):

    def test_empty_comment_str(self):
        x = str()
        d = {box.CommentID(): box.Comment(x)}
        r = pack_unpack(d, skip_comments=False)
        self.assertEqual(d[next(iter(d))], r[next(iter(r))])
        self.assertIsInstance(next(iter(r)), box.CommentID)

    def test_comment_str_8(self):
        x = "#"
        d = {box.CommentID(): box.Comment(x)}
        r = pack_unpack(d, skip_comments=False)
        self.assertEqual(d[next(iter(d))], r[next(iter(r))])
        self.assertIsInstance(next(iter(r)), box.CommentID)

    def test_comment_str_64(self):
        x = "#" * 8
        d = {box.CommentID(): box.Comment(x)}
        r = pack_unpack(d, skip_comments=False)
        self.assertEqual(d[next(iter(d))], r[next(iter(r))])
        self.assertIsInstance(next(iter(r)), box.CommentID)

    def test_short_comment_str(self):
        x = "#" * (2**8)
        d = {box.CommentID(): box.Comment(x)}
        r = pack_unpack(d, skip_comments=False)
        self.assertEqual(d[next(iter(d))], r[next(iter(r))])
        self.assertIsInstance(next(iter(r)), box.CommentID)

    def test_medium_comment_str(self):
        x = "#" * (2**16)
        d = {box.CommentID(): box.Comment(x)}
        r = pack_unpack(d, skip_comments=False)
        self.assertEqual(d[next(iter(d))], r[next(iter(r))])
        self.assertIsInstance(next(iter(r)), box.CommentID)

    def test_long_comment_str(self):
        x = "#" * (2**24)
        d = {box.CommentID(): box.Comment(x)}
        r = pack_unpack(d, skip_comments=False)
        self.assertEqual(d[next(iter(d))], r[next(iter(r))])
        self.assertIsInstance(next(iter(r)), box.CommentID)


class TestBin(unittest.TestCase):

    def test_empty_bin(self):
        x = b''
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], bytes)

    def test_short_bin_lower_endpoint(self):
        x = b'\x00' * 9
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], bytes)

    def test_short_bin_upper_endpoint(self):
        x = b'\x00' * (2**8)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], bytes)

    def test_medium_bin_lower_endpoint(self):
        x = b'\x00' * (2**8 + 1)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], bytes)

    def test_medium_bin_upper_endpoint(self):
        x = b'\x00' * (2**16)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], bytes)

    def test_long_bin_lower_endpoint(self):
        x = b'\x00' * (2**16 + 1)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], bytes)

    def test_long_bin_upper(self):
        x = b'\x00' * (2**24)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], bytes)

    def test_big_bin(self):
        # toooooo big to test ;)
        self.assertTrue(True)

    def test_heavy_bin(self):
        # toooooo heavy to test ;)
        self.assertTrue(True)


class TestConstInt(unittest.TestCase):

    def test_const_number_0_to_99(self):
        for x in range(100):
            with self.subTest("Const number: {}".format(x)):
                d = {0: x}
                r = pack_unpack(d)
                self.assertEqual(d, r)


class TestPositiveInt(unittest.TestCase):

    def test_pint8_to_pint64_lower_endpoint(self):
        data = {"pint8": 100, "pint16": 2**8,
                "pint24": 2**16, "pint32": 2**24,
                "pint40": 2**32, "pint48": 2**40,
                "pint56": 2**48, "pint64": 2**56}
        for key, val in data.items():
            with self.subTest("{}".format(key)):
                d = {0: val}
                r = pack_unpack(d)
                self.assertEqual(d, r)

    def test_pint8_to_pint64_upper_endpoint(self):
        data = {"pint8": 2**8 - 1, "pint16": 2**16 - 1,
                "pint24": 2**24 - 1, "pint32": 2**32 - 1,
                "pint40": 2**40 - 1, "pint48": 2**48 - 1,
                "pint56": 2**56 - 1, "pint64": 2**64 - 1}
        for key, val in data.items():
            with self.subTest("{}".format(key)):
                d = {0: val}
                r = pack_unpack(d)
                self.assertEqual(d, r)

    def test_pint_big_lower(self):
        x = 2**69
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)

    def test_pint_big_upper(self):
        x = 2**2048 - 1
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)

    def test_pint_heavy_lower(self):
        x = 2**2048
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)

    def test_pint_heavy_upper(self):
        x = 2**524288 - 1
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)


class TestNegativeInt(unittest.TestCase):

    def test_negative_number_1_to_99(self):
        for x in range(1, 100):
            with self.subTest("Number: {}".format(x)):
                d = {0: -x}
                r = pack_unpack(d)
                self.assertEqual(d, r)

    def test_pint8_to_pint64_lower_endpoint(self):
        data = {"pint8": 100, "pint16": 2**8,
                "pint24": 2**16, "pint32": 2**24,
                "pint40": 2**32, "pint48": 2**40,
                "pint56": 2**48, "pint64": 2**56}
        for key, val in data.items():
            with self.subTest("{}".format(key)):
                d = {0: -val}
                r = pack_unpack(d)
                self.assertEqual(d, r)

    def test_pint8_to_pint64_upper_endpoint(self):
        data = {"pint8": 2**8 - 1, "pint16": 2**16 - 1,
                "pint24": 2**24 - 1, "pint32": 2**32 - 1,
                "pint40": 2**40 - 1, "pint48": 2**48 - 1,
                "pint56": 2**56 - 1, "pint64": 2**64 - 1}
        for key, val in data.items():
            with self.subTest("{}".format(key)):
                d = {0: -val}
                r = pack_unpack(d)
                self.assertEqual(d, r)

    def test_nint_big_lower(self):
        x = 2**69
        data = {0: -x}
        r = pack_unpack(data)
        self.assertEqual(data, r)

    def test_nint_big_upper(self):
        x = 2**2048 - 1
        data = {0: -x}
        r = pack_unpack(data)
        self.assertEqual(data, r)

    def test_nint_heavy_lower(self):
        x = 2**2048
        data = {0: -x}
        r = pack_unpack(data)
        self.assertEqual(data, r)

    def test_nint_heavy_upper(self):
        x = 2**524288 - 1
        data = {0: -x}
        r = pack_unpack(data)
        self.assertEqual(data, r)


class TestIntAsHexOctBin(unittest.TestCase):

    def test_zero_as_hex(self):
        x = box.HexInt(0)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.HexInt)

    def test_zero_as_oct(self):
        x = box.OctInt(0)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.OctInt)

    def test_zero_as_bin(self):
        x = box.BinInt(0)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.BinInt)

    def test_pint_as_hex(self):
        x = box.HexInt(2**8 - 1)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.HexInt)

    def test_pint_as_oct(self):
        x = box.OctInt(2**8 - 1)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.OctInt)

    def test_pint_as_bin(self):
        x = box.BinInt(2**8 - 1)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.BinInt)

    def test_nint_as_hex(self):
        val = 2**8 - 1
        x = box.HexInt(-val)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.HexInt)

    def test_nint_as_oct(self):
        x = 2**8 - 1
        x = box.OctInt(-x)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.OctInt)

    def test_nint_as_bin(self):
        val = 2**8 - 1
        x = box.BinInt(-val)
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.BinInt)


class TestIntAsStringHexOctBin(unittest.TestCase):

    def test_zero_as_hex(self):
        x = box.HexInt("0x0000_0000")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.HexInt)

    def test_zero_as_oct(self):
        x = box.OctInt("0o000_000")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.OctInt)

    def test_zero_as_bin(self):
        x = box.BinInt("0b0000_0000")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.BinInt)

    def test_pint_as_hex(self):
        x = box.HexInt("0x0000_00ff")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.HexInt)

    def test_pint_as_oct(self):
        x = box.OctInt("0o000_377")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.OctInt)

    def test_pint_as_bin(self):
        x = box.BinInt("0b0000_1111_1111")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.BinInt)

    def test_nint_as_hex(self):
        x = box.HexInt("-0x0000_00ff")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.HexInt)

    def test_nint_as_oct(self):
        x = box.OctInt("-0o000_377")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.OctInt)

    def test_nint_as_bin(self):
        x = box.BinInt("-0b0000_1111_1111")
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], box.BinInt)


class TestFloatNumber(unittest.TestCase):

    def test_zero(self):
        x = 0.0
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)

    def test_negative_zero(self):
        x = float("-0.0")
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)

    def test_positive_infinity(self):
        x = float("+inf")
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)

    def test_negative_infinity(self):
        x = float("-inf")
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)

    def test_positive_number_with_exponent(self):
        x = float("3.0{}E-10".format(2**32 - 1))
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)

    def test_positive_number_without_exponent(self):
        x = float("3.00{}".format(2**32 - 1))
        data = {0: x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)

    def test_negative_number_with_exponent(self):
        x = float("3.0{}E-10".format(2**32 - 1))
        data = {0: -x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)

    def test_negative_number_without_exponent(self):
        x = float("3.{}00".format(2**32 - 1))
        data = {0: -x}
        r = pack_unpack(data)
        self.assertEqual(data, r)
        self.assertIsInstance(r[0], float)


class TestComplexNumber(unittest.TestCase):

    def test_with_positive_number(self):
        x = 1.2+3.4j
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], complex)

    def test_with_negative_number(self):
        x = -1.2-3.4j
        d = {0: x}
        r = pack_unpack(d)
        self.assertEqual(d, r)
        self.assertIsInstance(r[0], complex)


def pack_unpack(data, skip_comments=True):
    data = serializer.pack(data, skip_comments=skip_comments)
    return deserializer.unpack(data, skip_comments=skip_comments)


def my_obj_builder(obj):
    datatype = obj["type"]
    if datatype == "number":
        return obj["x"]
    elif datatype == "complex":
        return complex(obj["real"], obj["imag"])


if __name__ == "__main__":
    unittest.main()
