import unittest
from paradict.deserializer.buffered_text_stream import BufferedTextStream


class TestQueue(unittest.TestCase):

    def test_with_complete_data(self):
        s = "first line\nsecond line\n"
        queue = BufferedTextStream()
        r = put_and_get(queue, s)
        self.assertEqual(s, r)
        self.assertTrue(queue.is_empty())

    def test_with_incomplete_data(self):
        s = "first line\nsecond lin"
        queue = BufferedTextStream()
        r = put_and_get(queue, s)
        self.assertEqual("first line\n", r)
        self.assertFalse(queue.is_empty())


def put_and_get(queue, s):
    queue.put(s)
    buffer = list()
    for s in queue.get_all():
        buffer.append(s)
    return "".join(buffer)


if __name__ == "__main__":
    unittest.main()
