"""A FIFO queue for processing textual Paradict data"""
from collections import namedtuple


__all__ = ["BufferedTextStream"]


class BufferedTextStream:
    """A FIFO queue for processing textual Paradict data"""
    def __init__(self):
        self._buffer = list()
        self._partial_s = ""

    def is_empty(self):
        if not self._buffer and not self._partial_s:
            return True
        return False

    def put(self, s):
        """Store textual data in the buffer. This data will then be iteratively
        extracted by the 'get' method, line by line.
        Note: make sure that each line is ended with a newline '\n' character"""
        if not s:
            return
        # split lines and store first and last
        lines = s.splitlines(keepends=True)
        first = lines.pop(0)
        try:
            last = lines.pop()
        except IndexError as e:
            last = ""
        # handle self._partial_s
        if self._partial_s:
            self._buffer.append(self._partial_s + first)
            self._partial_s = ""
        else:
            self._buffer.append(first)
        # update buffer with splitted lines
        self._buffer.extend(lines)
        # update buffer/partial_s with the value of last
        if last:
            if last.endswith("\n"):
                self._buffer.append(last)
            else:
                self._partial_s = last

    def get(self):
        if self._buffer:
            return self._buffer.pop(0)

    def get_all(self):
        """Generator for iteratively getting each line composing the
        textual data stored in the buffer.
        Note that lines yielded won't end with a newline '\n' character"""
        while self._buffer:
            yield self._buffer.pop(0)
