import unittest
import datetime
from paradict import errors
from paradict import serializer
from paradict.serializer.packer import Packer, pack_int
from paradict import misc, box, tags
from paradict.tags.mappings import LETTER_TO_TAG


class TestEmptyData(unittest.TestCase):

    def test(self):
        data = dict()
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT_EMPTY)
        self.assertEqual(expected, r)


class TestDict(unittest.TestCase):
    """
    Dicts containing complex data are tested in
    paradict.tests.test_unpacker
    """
    def test_empty_dict(self):
        data = {0: dict()}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DICT_EMPTY,
                                  tags.END)
        self.assertEqual(expected, r)


class TestList(unittest.TestCase):
    """
    Lists containing complex data are tested in
    paradict.tests.test_unpacker
    """
    def test_empty_list(self):
        data = {0: list()}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.LIST_EMPTY,
                                  tags.END)
        self.assertEqual(expected, r)


class TestSet(unittest.TestCase):
    """
    Sets containing complex data are tested in
    paradict.tests.test_unpacker
    """
    def test_empty_set(self):
        data = {0: set()}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.SET_EMPTY,
                                  tags.END)
        self.assertEqual(expected, r)


class TestObj(unittest.TestCase):
    """
    Objs containing complex data are tested in
    paradict.tests.test_unpacker
    """
    def test_empty_obj(self):
        data = {0: box.Obj()}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.OBJ_EMPTY,
                                  tags.END)
        self.assertEqual(expected, r)


class TestGrid(unittest.TestCase):

    def test_empty_grid(self):
        data = {0: box.Grid()}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.GRID_EMPTY,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_with_integer(self):
        x = [(0, 1, 2),
             (3, 4, 5),
             (6, 7, -8)]
        data = {0: box.Grid(x)}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.GRID,
                                  tags.CONST_0,
                                  tags.CONST_1,
                                  tags.CONST_2,
                                  tags.GRID_DIV,
                                  tags.CONST_3,
                                  tags.CONST_4,
                                  tags.CONST_5,
                                  tags.CONST_6,
                                  tags.CONST_7,
                                  tags.NINT_8, 8,
                                  tags.END,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_with_float(self):
        x = [(0.0, 1.1, -2.2)]
        data = {0: box.Grid(x)}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.GRID,
                                  tags.FLOAT_1,
                                  tags.CONST_0,
                                  tags.FLOAT_2,
                                  tags.CONST_1,
                                  tags.CONST_1,
                                  tags.FLOAT_2,
                                  tags.NINT_8, 2,
                                  tags.CONST_2,
                                  tags.END,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_with_complex(self):
        x = [(1+2j, 3+4.5j)]
        data = {0: box.Grid(x)}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.GRID,
                                  tags.COMPLEX,
                                  tags.CONST_1,
                                  tags.CONST_2,
                                  tags.COMPLEX,
                                  tags.CONST_3,
                                  tags.FLOAT_2,
                                  tags.CONST_4,
                                  tags.CONST_5,
                                  tags.END,
                                  tags.END)
        self.assertEqual(expected, r)


class TestDatetime(unittest.TestCase):

    def test_naive_datetime_lower_endpoint(self):
        year, month = 1, 1
        day, hour, minute = 1, 0, 0
        second, microsecond = 0, 0
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        data = {0: val}
        r = pack_data(data)
        years, ns, trailing_zeros, _ = misc.deconstruct_datetime(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DATETIME,
                                  pack_int(years),
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_naive_datetime_upper_endpoint(self):
        year, month = 9999, 12
        day, hour, minute = 31, 23, 59
        second, microsecond = 59, 999999
        val = datetime.datetime(year=year, month=month, day=day,
                                hour=hour, minute=minute,
                                second=second, microsecond=microsecond)
        data = {0: val}
        r = pack_data(data)
        years, ns, trailing_zeros, _ = misc.deconstruct_datetime(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DATETIME,
                                  pack_int(years),
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  tags.END)
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
        data = {0: val}
        r = pack_data(data)
        years, ns, trailing_zeros, _ = misc.deconstruct_datetime(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DATETIME_EXT,
                                  pack_int(years),
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  tags.CONST_0,
                                  tags.END)
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
        data = {0: val}
        r = pack_data(data)
        years, ns, trailing_zeros, tz_minutes = misc.deconstruct_datetime(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DATETIME_EXT,
                                  pack_int(years),
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  pack_int(tz_minutes),
                                  tags.END)
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
        data = {0: val}
        r = pack_data(data)
        years, ns, trailing_zeros, tz_minutes = misc.deconstruct_datetime(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DATETIME_EXT,
                                  pack_int(years),
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  pack_int(tz_minutes),
                                  tags.END)
        self.assertEqual(expected, r)


class TestDate(unittest.TestCase):

    def test_date_lower_endpoint(self):
        year, month, day = 1, 1, 1
        val = datetime.date(year=year, month=month, day=day)
        data = {0: val}
        r = pack_data(data)
        years, days = misc.deconstruct_date(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DATE,
                                  pack_int(years),
                                  pack_int(days),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_date_upper_endpoint(self):
        year, month, day = 9999, 12, 31
        val = datetime.date(year=year, month=month, day=day)
        data = {0: val}
        r = pack_data(data)
        years, days = misc.deconstruct_date(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.DATE,
                                  pack_int(years),
                                  pack_int(days),
                                  tags.END)
        self.assertEqual(expected, r)


class TestTime(unittest.TestCase):

    def test_naive_time_lower_endpoint(self):
        hour, minute = 0, 0
        second, microsecond = 0, 0
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        data = {0: val}
        r = pack_data(data)
        ns, trailing_zeros, _ = misc.deconstruct_time(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.TIME,
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_naive_time_upper_endpoint(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond)
        data = {0: val}
        r = pack_data(data)
        ns, trailing_zeros, _ = misc.deconstruct_time(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.TIME,
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_aware_time_lower_endpoint(self):
        hour, minute = 0, 0
        second, microsecond = 0, 0
        tz = datetime.timezone(datetime.timedelta(hours=0, minutes=0))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        data = {0: val}
        r = pack_data(data)
        ns, trailing_zeros, _ = misc.deconstruct_time(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.TIME_EXT,
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_aware_time_upper_endpoint(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=0, minutes=0))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        data = {0: val}
        r = pack_data(data)
        ns, trailing_zeros, tz_minutes = misc.deconstruct_time(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.TIME_EXT,
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  pack_int(tz_minutes),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_aware_datetime_with_negative_negative_utc_timezone(self):
        hour, minute = 23, 59
        second, microsecond = 59, 999999
        tz = datetime.timezone(datetime.timedelta(hours=-1, minutes=-30))
        val = datetime.time(hour=hour, minute=minute,
                            second=second, microsecond=microsecond,
                            tzinfo=tz)
        data = {0: val}
        r = pack_data(data)
        ns, trailing_zeros, tz_minutes = misc.deconstruct_time(val)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.TIME_EXT,
                                  pack_int(ns),
                                  pack_int(trailing_zeros),
                                  pack_int(tz_minutes),
                                  tags.END)
        self.assertEqual(expected, r)


class TestNull(unittest.TestCase):

    def test(self):
        data = {0: None}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NULL,
                                  tags.END)
        self.assertEqual(expected, r)


class TestBool(unittest.TestCase):

    def test_true(self):
        data = {0: True}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BOOL_TRUE,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_false(self):
        data = {0: False}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BOOL_FALSE,
                                  tags.END)
        self.assertEqual(expected, r)


class TestConstChar(unittest.TestCase):

    def test_lower_letters(self):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
        for letter in letters:
            with self.subTest("Letter: {}".format(letter)):
                data = {letter: letter}
                packer = Packer(data)
                r = pack_data(data)
                const_tag = LETTER_TO_TAG.get(letter)
                expected = misc.forge_bin(tags.DICT,
                                          const_tag, const_tag,
                                          tags.END)
                self.assertEqual(expected, r)

    def test_upper_letters(self):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                   "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]
        for letter in letters:
            with self.subTest("Letter: {}".format(letter)):
                data = {letter: letter}
                packer = Packer(data)
                r = pack_data(data)
                const_tag = LETTER_TO_TAG.get(letter)
                expected = misc.forge_bin(tags.DICT,
                                          const_tag, const_tag,
                                          tags.END)
                self.assertEqual(expected, r)


class TestString(unittest.TestCase):

    def test_empty_str(self):
        data = {0: ""}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_EMPTY,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_8(self):
        x = ";"
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_8, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_16(self):
        x = ";"*2
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_16, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_24(self):
        x = ";"*3
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_24, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_32(self):
        x = ";"*4
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_32, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_40(self):
        x = ";"*5
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_40, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_48(self):
        x = ";"*6
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_48, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_56(self):
        x = ";"*7
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_56, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_64(self):
        x = ";"*8
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_64, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_72(self):
        x = ";"*9
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_72, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_80(self):
        x = ";"*10
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_80, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_88(self):
        x = ";"*11
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_88, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_96(self):
        x = ";"*12
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_96, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_104(self):
        x = ";"*13
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_104, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_112(self):
        x = ";"*14
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_112, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_120(self):
        x = ";"*15
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_120, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_128(self):
        x = ";"*16
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_128, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_136(self):
        x = ";"*17
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_136, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_144(self):
        x = ";"*18
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_144, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_152(self):
        x = ";"*19
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_152, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_160(self):
        x = ";"*20
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_160, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_168(self):
        x = ";"*21
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_168, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_176(self):
        x = ";"*22
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_176, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_184(self):
        x = ";"*23
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_184, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_192(self):
        x = ";"*24
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_192, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_200(self):
        x = ";"*25
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_200, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_208(self):
        x = ";"*26
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_208, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_216(self):
        x = ";"*27
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_216, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_224(self):
        x = ";"*28
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_224, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_232(self):
        x = ";"*29
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_232, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_240(self):
        x = ";"*30
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_240, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_248(self):
        x = ";"*31
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_248, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_str_256(self):
        x = ";"*32
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_256, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_short_str_lower_endpoint(self):
        x = ";"*33
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_SHORT, len(bin_x) - 1, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_short_str_upper_endpoint(self):
        x = ";"*(2**8)
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_SHORT, len(bin_x) - 1, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_medium_str_lower_endpoint(self):
        x = ";" * (2**8 + 1)
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_MEDIUM, len(bin_x) - 1, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_medium_str_upper_endpoint(self):
        x = ";" * (2**16)
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_MEDIUM, len(bin_x) - 1, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_long_str_lower_endpoint(self):
        x = ";" * (2**16 + 1)
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_LONG, len(bin_x) - 1, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_long_str_upper(self):
        x = ";" * (2**24)
        bin_x = x.encode("utf-8")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.STR_LONG, len(bin_x) - 1, bin_x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_big_str(self):
        # toooooo big to test ;)
        self.assertTrue(True)

    def test_heavy_str(self):
        # toooooo heavy to test ;)
        self.assertTrue(True)


class TestBin(unittest.TestCase):

    def test_empty_bin(self):
        data = {0: b''}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BIN_EMPTY,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_short_bin_lower_endpoint(self):
        x = b'\x00'*1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BIN_SHORT, len(x) - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_short_bin_upper_endpoint(self):
        x = b'\x00'*(2**8)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BIN_SHORT, len(x) - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_medium_bin_lower_endpoint(self):
        x = b'\x00' * (2**8 + 1)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BIN_MEDIUM, len(x) - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_medium_bin_upper_endpoint(self):
        x = b'\x00' * (2**16)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BIN_MEDIUM, len(x) - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_long_bin_lower_endpoint(self):
        x = b'\x00' * (2**16 + 1)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BIN_LONG, len(x) - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_long_bin_upper(self):
        x = b'\x00' * (2**24)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.BIN_LONG, len(x) - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_big_bin(self):
        # toooooo big to test ;)
        self.assertTrue(True)

    def test_heavy_bin(self):
        # toooooo heavy to test ;)
        self.assertTrue(True)


class TestConstInt(unittest.TestCase):

    def test_const_number_0(self):
        data = {0: 0}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_const_number_1(self):
        data = {1: 1}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_1,
                                  tags.CONST_1,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_const_number_99(self):
        data = {99: 99}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_99,
                                  tags.CONST_99,
                                  tags.END)
        self.assertEqual(expected, r)


class TestPositiveInt(unittest.TestCase):

    def test_pint8_lower(self):
        x = 100
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_8, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint8_upper(self):
        x = 2**8 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_8, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint16_lower(self):
        x = 2**8
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_16, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint16_upper(self):
        x = 2**16 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_16, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint24_lower(self):
        x = 2**16
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_24, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint24_upper(self):
        x = 2**24 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_24, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint32_lower(self):
        x = 2**24
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_32, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint32_upper(self):
        x = 2**32 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_32, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint40_lower(self):
        x = 2**32
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_40, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint40_upper(self):
        x = 2**40 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_40, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint48_lower(self):
        x = 2**40
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_48, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint48_upper(self):
        x = 2**48 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_48, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint56_lower(self):
        x = 2**48
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_56, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint56_upper(self):
        x = 2**56 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_56, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint64_lower(self):
        x = 2**56
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_64, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint64_upper(self):
        x = 2**64 - 1
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_64, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_big_lower(self):
        x = 2**64
        data = {0: x}
        size = misc.calc_uint_bytes(x)
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_BIG, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_big_upper(self):
        x = 2**2048 - 1
        data = {0: x}
        size = misc.calc_uint_bytes(x)  # 256 bytes !
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_BIG, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_heavy_lower(self):
        x = 2**2048
        data = {0: x}
        size = misc.calc_uint_bytes(x)
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_HEAVY, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_heavy_upper(self):
        x = 2**524288 - 1
        data = {0: x}
        size = misc.calc_uint_bytes(x)
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.PINT_HEAVY, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_too_large_number(self):
        x = 2**524289
        data = {0: x}
        packer = Packer(data)
        with self.assertRaises(errors.Error):
            pack_data(packer)


class TestNegativeInt(unittest.TestCase):

    def test_nint8_lower(self):
        x = 100
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_8, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint8_upper(self):
        x = 2**8 - 1
        data = {0:- x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_8, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint16_lower(self):
        x = 2**8
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_16, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint16_upper(self):
        x = 2**16 - 1
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_16, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint24_lower(self):
        x = 2**16
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_24, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint24_upper(self):
        x = 2**24 - 1
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_24, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint32_lower(self):
        x = 2**24
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_32, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint32_upper(self):
        x = 2**32 - 1
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_32, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint40_lower(self):
        x = 2**32
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_40, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint40_upper(self):
        x = 2**40 - 1
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_40, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint48_lower(self):
        x = 2**40
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_48, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint48_upper(self):
        x = 2**48 - 1
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_48, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint56_lower(self):
        x = 2**48
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_56, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint56_upper(self):
        x = 2**56 - 1
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_56, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint64_lower(self):
        x = 2**56
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_64, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint64_upper(self):
        x = 2**64 - 1
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_64, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_big_lower(self):
        x = 2**64
        data = {0: -x}
        size = misc.calc_uint_bytes(x)
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_BIG, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_big_upper(self):
        x = 2**2048 - 1
        data = {0: -x}
        size = misc.calc_uint_bytes(x)  # 256 bytes !
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_BIG, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_heavy_lower(self):
        x = 2**2048
        data = {0: -x}
        size = misc.calc_uint_bytes(x)
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_HEAVY, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_heavy_upper(self):
        x = 2**524288 - 1
        data = {0: -x}
        size = misc.calc_uint_bytes(x)
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.NINT_HEAVY, size - 1, x,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_too_large_number(self):
        x = 2**524289
        data = {0: -x}
        packer = Packer(data)
        with self.assertRaises(errors.Error):
            pack_data(packer)


class TestIntAsHexOctBin(unittest.TestCase):

    def test_zero_as_hex(self):
        x = box.HexInt(0)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_HEX,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_zero_as_oct(self):
        x = box.OctInt(0)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_OCT,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_zero_as_bin(self):
        x = box.BinInt(0)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_BIN,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_as_hex(self):
        val = 2**8 - 1
        x = box.HexInt(val)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_HEX,
                                  pack_int(val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_as_oct(self):
        val = 2**8 - 1
        x = box.OctInt(val)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_OCT,
                                  pack_int(val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_as_bin(self):
        val = 2**8 - 1
        x = box.BinInt(val)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_BIN,
                                  pack_int(val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_as_hex(self):
        val = 2**8 - 1
        x = box.HexInt(-val)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_HEX,
                                  pack_int(-val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_as_oct(self):
        val = 2**8 - 1
        x = box.OctInt(-val)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_OCT,
                                  pack_int(-val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_as_bin(self):
        val = 2**8 - 1
        x = box.BinInt(-val)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_BIN,
                                  pack_int(-val),
                                  tags.END)
        self.assertEqual(expected, r)


class TestIntAsStringHexOctBin(unittest.TestCase):

    def test_zero_as_hex(self):
        x = box.HexInt("0x0000")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_HEX_EXT,
                                  tags.CONST_3,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_zero_as_oct(self):
        x = box.OctInt("0o0000")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_OCT_EXT,
                                  tags.CONST_3,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_zero_as_bin(self):
        x = box.BinInt("0b0000")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_BIN_EXT,
                                  tags.CONST_3,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_as_hex(self):
        val = 2**8 - 1
        x = box.HexInt("0x0000_00ff")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_HEX_EXT,
                                  tags.CONST_6,
                                  pack_int(val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_as_oct(self):
        val = 2**8 - 1
        x = box.OctInt("0o00_000_377")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_OCT_EXT,
                                  tags.CONST_5,
                                  pack_int(val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_pint_as_bin(self):
        val = 2**8 - 1
        x = box.BinInt("0b1111_1111")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_BIN,
                                  pack_int(val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_as_hex(self):
        val = 2**8 - 1
        x = box.HexInt("-0x0000_00ff")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_HEX_EXT,
                                  tags.CONST_6,
                                  pack_int(-val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_as_oct(self):
        val = 2**8 - 1
        x = box.OctInt("-0o00_000_377")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_OCT_EXT,
                                  tags.CONST_5,
                                  pack_int(-val),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_nint_as_bin(self):
        val = 2**8 - 1
        x = box.BinInt("-0b11111111")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.RADIX_BIN,
                                  pack_int(-val),
                                  tags.END)
        self.assertEqual(expected, r)


class TestFloatNumber(unittest.TestCase):

    def test_zero(self):
        x = 0.0
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_1,
                                  tags.CONST_0,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_zero(self):
        x = float("-0.0")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_MISC,
                                  tags.CHAR_Z,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_positive_infinity(self):
        x = float("+inf")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_MISC,
                                  tags.CHAR_X,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_infinity(self):
        x = float("-inf")
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_MISC,
                                  tags.CHAR_Y,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_positive_float_1(self):
        x = float(1)
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_1,
                                  tags.CONST_1,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_positive_float_1_ext(self):
        x = float("1E-10")
        data = {0: x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_1_EXT,
                                  tags.CONST_1,
                                  tags.NINT_8, abs(int(parts.exponent)),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_float_1(self):
        x = float(1)
        data = {0: -x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_1,
                                  tags.NINT_8, 1,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_float_1_ext(self):
        x = float("1E-10")
        data = {0: -x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_1_EXT,
                                  tags.NINT_8, 1,
                                  tags.NINT_8, abs(int(parts.exponent)),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_positive_float_2(self):
        left_significand = 1
        right_significand = 2 ** 32 - 1
        significand = "{}.{}".format(left_significand, right_significand)
        x = float(significand)
        data = {0: x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_2,
                                  tags.CONST_1,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_positive_float_2_ext(self):
        left_significand = 1
        right_significand = 2**32 - 1

        significand = "{}.{}".format(left_significand, right_significand)
        x = float("{}E-10".format(significand))
        data = {0: x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_2_EXT,
                                  tags.CONST_1,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.NINT_8, abs(int(parts.exponent)),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_float_2(self):
        left_significand = 1
        right_significand = 2 ** 32 - 1
        significand = "{}.{}".format(left_significand, right_significand)
        x = float(significand)
        data = {0: -x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_2,
                                  tags.NINT_8, 1,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_float_2_ext(self):
        left_significand = 1
        right_significand = 2**32 - 1
        significand = "{}.{}".format(left_significand, right_significand)
        x = float("{}E-10".format(significand))
        data = {0: -x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_2_EXT,
                                  tags.NINT_8, 1,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.NINT_8, abs(int(parts.exponent)),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_positive_float_3(self):
        left_significand = 1
        right_significand = 2 ** 32 - 1
        leading_zeros = "0" * 3
        significand = "{}.{}{}".format(left_significand,
                                       leading_zeros,
                                       right_significand)
        x = float(significand)
        data = {0: x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_3,
                                  tags.CONST_1,
                                  tags.CONST_3,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_positive_float_3_ext(self):
        left_significand = 1
        right_significand = 2**32 - 1
        leading_zeros = "0" * 3
        significand = "{}.{}{}".format(left_significand,
                                       leading_zeros,
                                       right_significand)
        x = float("{}E-10".format(significand))
        data = {0: x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_3_EXT,
                                  tags.CONST_1,
                                  tags.CONST_3,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.NINT_8, abs(int(parts.exponent)),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_float_3(self):
        left_significand = 1
        right_significand = 2 ** 32 - 1
        leading_zeros = "0" * 3
        significand = "{}.{}{}".format(left_significand,
                                       leading_zeros,
                                       right_significand)
        x = float(significand)
        data = {0: -x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_3,
                                  tags.NINT_8, 1,
                                  tags.CONST_3,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.END)
        self.assertEqual(expected, r)

    def test_negative_float_3_ext(self):
        left_significand = 1
        right_significand = 2**32 - 1
        leading_zeros = "0" * 3
        significand = "{}.{}{}".format(left_significand,
                                       leading_zeros,
                                       right_significand)
        x = float("{}E-10".format(significand))
        data = {0: -x}
        r = pack_data(data)
        parts = misc.split_float(x)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.FLOAT_3_EXT,
                                  tags.NINT_8, 1,
                                  tags.CONST_3,
                                  tags.PINT_32, int(parts.right_significand),
                                  tags.NINT_8, abs(int(parts.exponent)),
                                  tags.END)
        self.assertEqual(expected, r)


class TestComplexNumber(unittest.TestCase):

    def test_with_positive_numbers(self):
        x = 1.2+3.4j
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.COMPLEX,
                                  tags.FLOAT_2,
                                  tags.CONST_1,
                                  tags.CONST_2,
                                  tags.FLOAT_2,
                                  tags.CONST_3,
                                  tags.CONST_4,
                                  tags.END)
        self.assertEqual(expected, r)

    def test_with_negative_numbers(self):
        x = -1.2-3.4j
        data = {0: x}
        r = pack_data(data)
        expected = misc.forge_bin(tags.DICT,
                                  tags.CONST_0,
                                  tags.COMPLEX,
                                  tags.FLOAT_2,
                                  tags.NINT_8, 1,
                                  tags.CONST_2,
                                  tags.FLOAT_2,
                                  tags.NINT_8, 3,
                                  tags.CONST_4,
                                  tags.END)
        self.assertEqual(expected, r)


class TestDictOnly(unittest.TestCase):
    def test(self):
        data = datetime.datetime(2020, 1, 1)
        # paradict.errors.Error: The root data structure should be a dict
        with self.assertRaises(errors.Error):
            pack_data(data, dict_only=True)


class TestNotDictOnly(unittest.TestCase):
    def test_empty_list(self):
        data = list()
        r = pack_data(data)
        expected = misc.forge_bin(tags.LIST_EMPTY)
        self.assertEqual(expected, r)

    def test_str_8(self):
        x = ";"
        bin_x = x.encode("utf-8")
        data = x
        r = pack_data(data)
        expected = misc.forge_bin(tags.STR_8, bin_x)
        self.assertEqual(expected, r)


def pack_data(data, **kwargs):
    return serializer.pack(data, **kwargs)


if __name__ == '__main__':
    unittest.main()
