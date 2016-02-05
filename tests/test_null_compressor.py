import unittest

from jackrabbit.compressors.null_compressor import NullCompressor


class TestNullCompressor(unittest.TestCase):
    def test_compress(self):
        s = 'The quick brown fox jumps over the lazy dog'
        c = NullCompressor.compress(s)
        self.assertEqual(s, c)

    def test_decompress(self):
        s = 'The quick brown fox jumps over the lazy dog'
        c = NullCompressor.decompress(s)
        self.assertEqual(s, c)
