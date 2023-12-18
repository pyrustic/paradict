import unittest
from paradict.queue.txt_queue import TxtQueue


class TestQueue(unittest.TestCase):

    def test_with_complete_data(self):
        s = "first line\nsecond line\n"
        queue = TxtQueue()
        r = put_and_get(queue, s)
        self.assertEqual(s, r)
        self.assertEqual(0, len(queue.buffer))

    def test_with_incomplete_data(self):
        s = "first line\nsecond lin"
        queue = TxtQueue()
        r = put_and_get(queue, s)
        self.assertEqual("first line\n", r)
        self.assertNotEqual(0, len(queue.buffer))


def put_and_get(queue, s):
    queue.put(s)
    buffer = list()
    for s in queue.get():
        buffer.append(s)
    return "".join(buffer)


if __name__ == '__main__':
    unittest.main()
