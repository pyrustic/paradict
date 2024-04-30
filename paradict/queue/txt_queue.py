"""A FIFO queue for processing textual Paradict data"""
from collections import namedtuple


__all__ = ["TxtQueue"]


class TxtQueue:
    """A FIFO queue for processing textual Paradict data"""
    def __init__(self):
        self._buffer = list()

    @property
    def buffer(self):
        return self._buffer

    def enqueue(self, s):
        """Store textual data in the buffer. This data will then be iteratively
        extracted by the 'get' method, line by line.
        Note: make sure that each line is ended with a newline '\n' character"""
        self._buffer.append(s)

    def dequeue(self):
        """Generator for iteratively getting each line composing the
        textual data stored in the buffer.
        Note that lines yielded won't end with a newline '\n' character"""
        yield from self._read()

    def _read(self):
        if not self._buffer:
            return
        text = "".join(self._buffer)
        del self._buffer[:]
        cache = list()
        i = None
        for i, char in enumerate(text):
            cache.append(char)
            if char == "\n":
                line = "".join(cache)
                del cache[:]
                yield line
        if cache and i is not None:
            self._buffer.insert(0, "".join(cache))
