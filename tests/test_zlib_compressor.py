import unittest
import zlib

from jackrabbit.compressors.zlib_compressor import ZlibCompressor


class TestZlibCompressor(unittest.TestCase):
    def test_compress(self):
        s = 'The quick brown fox jumps over the lazy dog'
        c = ZlibCompressor.compress(s)
        self.assertEqual(zlib.compress(s), c)

    def test_decompress(self):
        c = 'x\x9c\x0b\xc9HU(,\xcdL\xceVH*\xca/\xcfSH\xcb\xafP\xc8*\xcd-(V\xc8/K-R(\x01J\xe7$VU*\xa4\xe4\xa7\x03\x00[\xdc\x0f\xda'
        s = ZlibCompressor.decompress(c)
        self.assertEqual('The quick brown fox jumps over the lazy dog', s)
