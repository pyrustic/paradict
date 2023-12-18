"""A FIFO queue for processing binary Paradict data"""
from collections import namedtuple
from paradict import tags, errors
from paradict.tags.misc import SIZE_TO_STR
from paradict import misc

# a datum is made of a header and payload
# The header is made of a tag and optional bytes to store the size of the payload
# The width is the size of the datum: size of header + size of payload
Datum = namedtuple("Datum", ["tag", "payload", "width"])


class BinQueue:
    """A FIFO queue for processing binary Paradict data"""
    def __init__(self):
        self._tag = None
        self._buffer = bytearray()
        self._expected_width = 0

    @property
    def buffer(self):
        return self._buffer

    def put(self, raw):
        """Store binary data in the buffer. This data will then be iteratively
        extracted by the 'get' method"""
        self._buffer.extend(raw)

    def get(self):
        """Generator for iteratively getting each tag-payload tuple composing the
        raw data stored in the buffer"""
        while True:
            r = self._read()
            if not r:
                break
            tag, payload = r
            yield tag, payload

    def _read(self):
        if not self._buffer:
            return
        # update tag
        self._update_tag_var()
        # update span
        self._update_expected_width_var()
        if len(self._buffer) < self._expected_width:
            return
        # STRx
        if tags.STR_8 <= self._tag <= tags.STR_256:
            return self._read_buffer(read_strx)
        # STR
        elif self._tag in (tags.STR_SHORT,
                           tags.STR_MEDIUM,
                           tags.STR_LONG,
                           tags.STR_HEAVY):
            return self._read_buffer(read_str)
        # BIN
        elif self._tag in (tags.BIN_SHORT,
                           tags.BIN_MEDIUM,
                           tags.BIN_LONG,
                           tags.BIN_HEAVY):
            return self._read_buffer(read_bin)
        # PINTx
        elif tags.PINT_8 <= self._tag <= tags.PINT_64:
            return self._read_buffer(read_pintx)
        # PINT_BIG
        elif self._tag == tags.PINT_BIG:
            return self._read_buffer(read_pint_big)
        # PINT_HEAVY
        elif self._tag == tags.PINT_HEAVY:
            return self._read_buffer(read_pint_heavy)
        # NINTx
        elif tags.NINT_8 <= self._tag <= tags.NINT_64:
            return self._read_buffer(read_nintx)
        # NINT_BIG
        elif self._tag == tags.NINT_BIG:
            return self._read_buffer(read_nint_big)
        # NINT_HEAVY
        elif self._tag == tags.NINT_HEAVY:
            return self._read_buffer(read_nint_heavy)
        # else...
        else:
            return self._read_buffer(read_tag)

    def _read_buffer(self, reader):
        r = reader(self._tag, self._buffer)
        if r is None:
            return
        if r.payload is None:
            self._expected_width = r.width
            return
        self._buffer[:] = self._buffer[r.width:]
        self._clear_status()
        return r.tag, r.payload

    def _update_tag_var(self):
        if self._tag is None:
            self._tag = self._buffer[0].to_bytes(length=1,
                                                 byteorder="little",
                                                 signed=False)

    def _update_expected_width_var(self):
        if self._expected_width or self._tag is None:
            return
        if self._tag in (tags.PINT_8, tags.NINT_8, tags.STR_8):
            self._expected_width = 2
        elif self._tag in (tags.PINT_16, tags.NINT_16, tags.STR_16):
            self._expected_width = 3
        elif self._tag in (tags.PINT_24, tags.NINT_24, tags.STR_24):
            self._expected_width = 4
        elif self._tag in (tags.PINT_32, tags.NINT_32, tags.STR_32):
            self._expected_width = 5
        elif self._tag in (tags.PINT_40, tags.NINT_40, tags.STR_40):
            self._expected_width = 6
        elif self._tag in (tags.PINT_48, tags.NINT_48, tags.STR_48):
            self._expected_width = 7
        elif self._tag in (tags.PINT_56, tags.NINT_56, tags.STR_56):
            self._expected_width = 8
        elif self._tag in (tags.PINT_64, tags.NINT_64, tags.STR_64):
            self._expected_width = 9
        elif self._tag == tags.STR_72:
            self._expected_width = 10
        elif self._tag == tags.STR_80:
            self._expected_width = 11
        elif self._tag == tags.STR_88:
            self._expected_width = 12
        elif self._tag == tags.STR_96:
            self._expected_width = 13
        elif self._tag == tags.STR_104:
            self._expected_width = 14
        elif self._tag == tags.STR_112:
            self._expected_width = 15
        elif self._tag == tags.STR_120:
            self._expected_width = 16
        elif self._tag == tags.STR_128:
            self._expected_width = 17
        elif self._tag == tags.STR_136:
            self._expected_width = 18
        elif self._tag == tags.STR_144:
            self._expected_width = 19
        elif self._tag == tags.STR_152:
            self._expected_width = 20
        elif self._tag == tags.STR_160:
            self._expected_width = 21
        elif self._tag == tags.STR_168:
            self._expected_width = 22
        elif self._tag == tags.STR_176:
            self._expected_width = 23
        elif self._tag == tags.STR_184:
            self._expected_width = 24
        elif self._tag == tags.STR_192:
            self._expected_width = 25
        elif self._tag == tags.STR_200:
            self._expected_width = 26
        elif self._tag == tags.STR_208:
            self._expected_width = 27
        elif self._tag == tags.STR_216:
            self._expected_width = 28
        elif self._tag == tags.STR_224:
            self._expected_width = 29
        elif self._tag == tags.STR_232:
            self._expected_width = 30
        elif self._tag == tags.STR_240:
            self._expected_width = 31
        elif self._tag == tags.STR_248:
            self._expected_width = 32
        elif self._tag == tags.STR_256:
            self._expected_width = 33
        elif self._tag in (tags.STR_SHORT, tags.BIN_SHORT):
            self._expected_width = 3
        elif self._tag in (tags.STR_MEDIUM, tags.BIN_MEDIUM):
            self._expected_width = 4
        elif self._tag in (tags.STR_LONG, tags.BIN_LONG):
            self._expected_width = 5
        elif self._tag in (tags.STR_HEAVY, tags.BIN_HEAVY):
            self._expected_width = 6
        else:
            self._expected_width = 1

    def _clear_status(self):
        self._tag = None
        self._expected_width = 0


def read_payload_size(buffer, nb=1, offset=1):
    """
    Read the expected size of payload
    Note that nb is the number of bytes encoding the size of payload
    """
    r = buffer[offset: offset+nb]
    return int.from_bytes(r, "little", signed=False)


def extract_datum(buffer, tag, nb=1):
    """
    This function is used read STR_SHORT, STR_MEDIUM, STR_LONG,
     STR_HEAVY, BIN_SHORT, BIN_MEDIUM, BIN_LONG and BIN_HEAVY datums.

    nb is the number of bytes to encode the size of payload

    This function returns a Datum
    """
    # header_size
    header_size = 1 + nb
    if len(buffer) < header_size:
        return
    payload_size = read_payload_size(buffer, nb) + 1
    # Width is the size (bytes) of the datum (header + payload)
    # note that the header is made of tag + byte(s) to store payload size
    width = header_size + payload_size
    if len(buffer) < width:
        payload = None
    else:
        payload = buffer[header_size:width]
    return Datum(tag, payload, width)


def read_tag(tag, buffer):
    payload = b''
    width = 1
    return Datum(tag, payload, width)


def read_str(tag, buffer):
    containers = {tags.STR_SHORT: 1,
                  tags.STR_MEDIUM: 2,
                  tags.STR_LONG: 3,
                  tags.STR_HEAVY: 4}
    # nb is the number of bytes to encode the size of payload
    nb = containers.get(tag)
    return extract_datum(buffer, tag, nb)


def read_strx(tag, buffer):
    size = None
    for s, t in SIZE_TO_STR.items():
        if t == tag:
            size = s
            break
    if size is None:
        raise errors.Error("Unknown string tag '{}'".format(tag))
    width = 1 + size
    if len(buffer) < width:
        payload = None
    else:
        payload = buffer[1:width]
    return Datum(tag, payload, width)


def read_bin(tag, buffer):
    containers = {tags.BIN_SHORT: 1,
                  tags.BIN_MEDIUM: 2,
                  tags.BIN_LONG: 3,
                  tags.BIN_HEAVY: 4}
    # nb is the number of bytes to encode the size of payload
    nb = containers.get(tag)
    return extract_datum(buffer, tag, nb)


def read_pint_big(tag, buffer):
    n = len(buffer)
    if n < 2:  # here, 2 == 1 byte tag + 1 byte to store the size of payload
        return
    payload_size = read_payload_size(buffer) + 1
    width = 2 + payload_size
    if len(buffer) < width:
        payload = None
    else:
        payload = buffer[2:width]
    return Datum(tag, payload, width)


def read_pint_heavy(tag, buffer):
    n = len(buffer)
    if n < 3:  # here, 3 == 1 byte tag + 2 byte to store the size of payload
        return
    payload_size = read_payload_size(buffer, nb=2) + 1
    width = 3 + payload_size
    if len(buffer) < width:
        payload = None
    else:
        payload = buffer[3:width]
    return Datum(tag, payload, width)


def read_pintx(tag, buffer):
    sizes = {tags.PINT_8: 1, tags.PINT_16: 2,
             tags.PINT_24: 3, tags.PINT_32: 4,
             tags.PINT_40: 5, tags.PINT_48: 6,
             tags.PINT_56: 7, tags.PINT_64: 8}
    payload_size = sizes.get(tag)
    width = 1 + payload_size
    if len(buffer) < width:
        payload = None
    else:
        payload = buffer[1:width]
    return Datum(tag, payload, width)


def read_nint_big(tag, buffer):
    return read_pint_big(tag, buffer)


def read_nint_heavy(tag, buffer):
    return read_pint_heavy(tag, buffer)


def read_nintx(tag, buffer):
    sizes = {tags.NINT_8: 1, tags.NINT_16: 2,
             tags.NINT_24: 3, tags.NINT_32: 4,
             tags.NINT_40: 5, tags.NINT_48: 6,
             tags.NINT_56: 7, tags.NINT_64: 8}
    payload_size = sizes.get(tag)
    width = 1 + payload_size
    if len(buffer) < width:
        payload = None
    else:
        payload = buffer[1:width]
    return Datum(tag, payload, width)
