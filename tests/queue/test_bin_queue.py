import unittest
from paradict.queue.bin_queue import BinQueue
from paradict import misc, tags


class TestQueueWithINT(unittest.TestCase):

    def test_complete_pint_datum(self):
        data = misc.forge_bin(tags.PINT_BIG, 1, b'\x00' * 2)
        queue = BinQueue()
        r = put_and_get(queue, data)
        expected = misc.forge_bin(tags.PINT_BIG, b'\x00' * 2)
        self.assertEqual(expected, r)
        self.assertEqual(0, len(queue.buffer))

    def test_complete_nint_datum(self):
        data = misc.forge_bin(tags.NINT_BIG, 1, b'\x00' * 2)
        queue = BinQueue()
        r = put_and_get(queue, data)
        expected = misc.forge_bin(tags.NINT_BIG, b'\x00' * 2)
        self.assertEqual(expected, r)
        self.assertEqual(0, len(queue.buffer))

    def test_complete_pintx_datum(self):
        i = 0
        for tag in [tags.PINT_8, tags.PINT_16, tags.PINT_24,
                    tags.PINT_32, tags.PINT_40, tags.PINT_48,
                    tags.PINT_56, tags.PINT_64]:
            i += 8
            with self.subTest("PINT_{} tag".format(i)):
                n = i//8
                data = misc.forge_bin(tag, b'\x00'*n)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertEqual(data, r)
                self.assertEqual(0, len(queue.buffer))

    def test_complete_nintx_datum(self):
        i = 0
        for tag in [tags.NINT_8, tags.NINT_16, tags.NINT_24,
                    tags.NINT_32, tags.NINT_40, tags.NINT_48,
                    tags.NINT_56, tags.NINT_64]:
            i += 8
            with self.subTest("NINT_{} tag".format(i)):
                n = i//8
                data = misc.forge_bin(tag, b'\x00'*n)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertEqual(data, r)
                self.assertEqual(0, len(queue.buffer))

    def test_incomplete_pint_datum(self):
        data = misc.forge_bin(tags.PINT_BIG, 1, b'\x00' * 1)
        queue = BinQueue()
        r = put_and_get(queue, data)
        self.assertIsNone(r)
        self.assertNotEqual(0, len(queue.buffer))

    def test_incomplete_nint_datum(self):
        data = misc.forge_bin(tags.NINT_BIG, 1, b'\x00' * 1)
        queue = BinQueue()
        r = put_and_get(queue, data)
        self.assertIsNone(r)
        self.assertNotEqual(0, len(queue.buffer))

    def test_incomplete_pintx_datum(self):
        i = 0
        for tag in [tags.PINT_8, tags.PINT_16, tags.PINT_24,
                    tags.PINT_32, tags.PINT_40, tags.PINT_48,
                    tags.PINT_56, tags.PINT_64]:
            i += 8
            with self.subTest("PINT_{} tag".format(i)):
                n = (i//8) - 1
                data = misc.forge_bin(tag, b'\x00'*n)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertIsNone(r)
                self.assertNotEqual(0, len(queue.buffer))

    def test_incomplete_nintx_datum(self):
        i = 0
        for tag in [tags.NINT_8, tags.NINT_16, tags.NINT_24,
                    tags.NINT_32, tags.NINT_40, tags.NINT_48,
                    tags.NINT_56, tags.NINT_64]:
            i += 8
            with self.subTest("NINT_{} tag".format(i)):
                n = (i//8) - 1
                data = misc.forge_bin(tag, b'\x00'*n)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertIsNone(r)
                self.assertNotEqual(0, len(queue.buffer))


class TestQueueWithSTR(unittest.TestCase):

    def test_complete_str_datum(self):
        i = 0
        for name, tag in {"STR_SHORT": tags.STR_SHORT,
                          "STR_MEDIUM": tags.STR_MEDIUM,
                          "STR_LONG": tags.STR_LONG}.items():
            i += 8
            with self.subTest("{} tag".format(name)):
                n = i // 8
                size = 2**(8*n)
                data = misc.forge_bin(tag, size-1,  b'\x00' * size)
                queue = BinQueue()
                r = put_and_get(queue, data)
                expected = misc.forge_bin(tag, b'\x00' * size)
                self.assertEqual(expected, r)
                self.assertEqual(0, len(queue.buffer))

    def test_complete_strx_datum(self):
        i = 0
        for tag in [tags.STR_8, tags.STR_16, tags.STR_24,
                    tags.STR_32, tags.STR_40, tags.STR_48,
                    tags.STR_56, tags.STR_64, tags.STR_72,
                    tags.STR_80, tags.STR_88, tags.STR_96,
                    tags.STR_104, tags.STR_112, tags.STR_120,
                    tags.STR_128, tags.STR_136, tags.STR_144,
                    tags.STR_152, tags.STR_160, tags.STR_168,
                    tags.STR_176, tags.STR_184, tags.STR_192,
                    tags.STR_200, tags.STR_208]:
            i += 8
            with self.subTest("STR_{} tag".format(i)):
                n = i // 8
                data = misc.forge_bin(tag, b'\x00' * n)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertEqual(data, r)
                self.assertEqual(0, len(queue.buffer))

    def test_incomplete_str_datum(self):
        i = 0
        for name, tag in {"STR_SHORT": tags.STR_SHORT,
                          "STR_MEDIUM": tags.STR_MEDIUM,
                          "STR_LONG": tags.STR_LONG}.items():
            i += 8
            with self.subTest("{} tag".format(name)):
                n = (i // 8) - 1
                size = 2**(8*n)
                data = misc.forge_bin(tag, size-1,  b'\x00' * size)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertIsNone(r)
                self.assertNotEqual(0, len(queue.buffer))

    def test_incomplete_strx_datum(self):
        i = 0
        for tag in [tags.STR_8, tags.STR_16, tags.STR_24,
                    tags.STR_32, tags.STR_40, tags.STR_48,
                    tags.STR_56, tags.STR_64, tags.STR_72,
                    tags.STR_80, tags.STR_88, tags.STR_96,
                    tags.STR_104, tags.STR_112, tags.STR_120,
                    tags.STR_128, tags.STR_136, tags.STR_144,
                    tags.STR_152, tags.STR_160, tags.STR_168,
                    tags.STR_176, tags.STR_184, tags.STR_192,
                    tags.STR_200, tags.STR_208]:
            i += 8
            with self.subTest("STR_{} tag".format(i)):
                n = (i // 8) - 1
                data = misc.forge_bin(tag, b'\x00' * n)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertIsNone(r)
                self.assertNotEqual(0, len(queue.buffer))


class TestQueueWithBIN(unittest.TestCase):

    def test_complete_bin_datum(self):
        i = 0
        for name, tag in {"BIN_SHORT": tags.BIN_SHORT,
                          "BIN_MEDIUM": tags.BIN_MEDIUM,
                          "BIN_LONG": tags.BIN_LONG}.items():
            i += 8
            with self.subTest("{} tag".format(name)):
                n = i // 8
                size = 2**(8*n)
                data = misc.forge_bin(tag, size-1,  b'\x00' * size)
                queue = BinQueue()
                r = put_and_get(queue, data)
                expected = misc.forge_bin(tag, b'\x00' * size)
                self.assertEqual(expected, r)
                self.assertEqual(0, len(queue.buffer))

    def test_incomplete_bin_datum(self):
        i = 0
        for name, tag in {"BIN_SHORT": tags.BIN_SHORT,
                          "BIN_MEDIUM": tags.BIN_MEDIUM,
                          "BIN_LONG": tags.BIN_LONG}.items():
            i += 8
            with self.subTest("{} tag".format(name)):
                n = (i // 8) - 1
                size = 2**(8*n)
                data = misc.forge_bin(tag, size-1,  b'\x00' * size)
                queue = BinQueue()
                r = put_and_get(queue, data)
                self.assertIsNone(r)
                self.assertNotEqual(0, len(queue.buffer))


def put_and_get(queue, raw):
    queue.put(raw)
    buffer = bytearray()
    for tag, payload in queue.get():
        buffer.extend(tag)
        buffer.extend(payload)
    return None if not buffer else buffer


if __name__ == "__main__":
    unittest.main()
