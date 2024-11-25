import io
import unittest
from datetime import datetime
from datetime import timezone
from paradict import scan, pack


utc_datetime = datetime(2024, 7, 25,
                        14, 30, 59,
                        tzinfo=timezone.utc)


DATA = {"id": 42, "name": "alex", "pi": 3.14,
        "created_at": utc_datetime, "weight": None,
        "photo": b'avatar.png', "music": {},
        "books": {"thriller": ["book 1", "book 2"],
                  "sci-fi": {"book 3", "book 4"}}}


class TestScanFunction(unittest.TestCase):

    def test_with_integer(self):
        data = pack(42)
        with io.BytesIO(data) as file:
            buffer = bytearray()
            i = 0
            for tag, slice_obj in scan(file):
                buffer.extend(data[slice_obj])
                i += 1
        self.assertEqual(1, i)
        self.assertEqual(bytes(buffer), data)

    def test_with_string(self):
        data = pack("alex")
        with io.BytesIO(data) as file:
            buffer = bytearray()
            i = 0
            for tag, slice_obj in scan(file):
                buffer.extend(data[slice_obj])
                i += 1
        self.assertEqual(1, i)
        self.assertEqual(bytes(buffer), data)

    def test_with_none_value(self):
        data = pack(None)
        with io.BytesIO(data) as file:
            buffer = bytearray()
            i = 0
            for tag, slice_obj in scan(file):
                buffer.extend(data[slice_obj])
                i += 1
        self.assertEqual(1, i)
        self.assertEqual(bytes(buffer), data)

    def test_with_long_str(self):
        data = pack("A"*50000)
        with io.BytesIO(data) as file:
            buffer = bytearray()
            i = 0
            for tag, slice_obj in scan(file):
                buffer.extend(data[slice_obj])
                i += 1
        self.assertEqual(1, i)
        self.assertEqual(bytes(buffer), data)

    def test_with_complex_data(self):
        data = pack(DATA)
        with io.BytesIO(data) as file:
            buffer = bytearray()
            i = 0
            for tag, slice_obj in scan(file):
                buffer.extend(data[slice_obj])
                i += 1
        self.assertEqual(35, i)
        self.assertEqual(bytes(buffer), data)


if __name__ == "__main__":
    unittest.main()
