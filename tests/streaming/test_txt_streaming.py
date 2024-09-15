import unittest
from paradict.serializer.encoder import Encoder
from paradict.deserializer.decoder import Decoder


class TestTxtStreaming(unittest.TestCase):

    def test(self):
        # This stream is made of messages
        # Each message is a dictionary that serves as envelope
        stream = [{0: "a"}, {0: "b"}, {0: "c"}]
        # Result will hold the unpacked messages
        result = list()
        # instantiate encoder and decoder
        encoder = Encoder()
        # the receiver takes as argument the reference to the decoder
        decoder = Decoder(receiver=lambda ref: result.append(ref.data))
        # iterate over the stream to pack each message into datums
        # that will feed the decoder which will call the receiver
        # after each complete unpacking of a message.
        # The decoder holds a reference to the latest
        # unpacked message via the "decoder.data" property
        for i, msg in enumerate(stream):
            for line in encoder.encode(msg):
                decoder.feed(line + "\n")
            decoder.feed("===\n")
            # check if datum is well unpacked
            with self.subTest("Message At Index: {}".format(i)):
                # decoder.data holds unpacked data
                self.assertEqual(msg, decoder.data)
        # check if the original stream contents is mirrored in
        # the result variable
        self.assertEqual(stream, result)


if __name__ == '__main__':
    unittest.main()
