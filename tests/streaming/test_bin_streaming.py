import unittest
from paradict.serializer.packer import Packer
from paradict.deserializer.unpacker import Unpacker


class TestBinStreaming(unittest.TestCase):

    def test(self):
        # This stream is made of messages
        # Each message is a dictionary that serves as envelope
        stream = [{0: "a"}, {0: "b"}, {0: "c"}]
        # Result will hold the unpacked messages
        result = list()
        # instantiate packer and unpacker
        packer = Packer()
        # the receiver takes as argument the reference to the unpacker
        unpacker = Unpacker(receiver=lambda ref: result.append(ref.data))
        # iterate over the stream to pack each message into datums
        # that will feed the unpacker which will call the receiver
        # after each complete unpacking of a message.
        # The unpacker holds a reference to the latest
        # unpacked message via the "unpacker.data" property
        for i, msg in enumerate(stream):
            for datum in packer.pack(msg):
                unpacker.feed(datum)
            # check if datum is well unpacked
            with self.subTest("Message At Index: {}".format(i)):
                # unpacker.data holds unpacked data
                self.assertEqual(msg, unpacker.data)
        # check if the original stream contents is mirrored in
        # the result variable
        self.assertEqual(stream, result)


if __name__ == '__main__':
    unittest.main()
