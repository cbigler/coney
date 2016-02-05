import zlib


class ZlibCompressor(object):
    @staticmethod
    def compress(data):
        return zlib.compress(data)

    @staticmethod
    def decompress(data):
        return zlib.decompress(data)
