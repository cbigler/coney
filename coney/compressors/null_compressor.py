class NullCompressor(object):
    @staticmethod
    def compress(data):
        return data

    @staticmethod
    def decompress(data):
        return data