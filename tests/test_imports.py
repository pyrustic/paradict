import unittest


class TestImports(unittest.TestCase):

    def test_import_funcs(self):
        try:
            # import functions
            from paradict import encode
            from paradict import decode
            from paradict import encode_into
            from paradict import decode_from
            from paradict import pack
            from paradict import unpack
            from paradict import pack_into
            from paradict import unpack_from
            from paradict import scan
            from paradict import forge_bin
            from paradict import stringify_bin
            from paradict import is_valid
            from paradict import split_kv
        except ImportError:
            self.assertTrue(False)

    def test_import_classes(self):
        try:
            # import classes
            from paradict import Encoder
            from paradict import Decoder
            from paradict import Packer
            from paradict import Unpacker
            from paradict import TypeRef
            from paradict import Validator
            from paradict import Datatype
        except ImportError:
            self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
