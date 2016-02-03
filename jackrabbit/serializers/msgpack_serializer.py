from ..third_party.umsgpack import loads, dumps


class MsgpackSerializer(object):
    @staticmethod
    def dumps(o):
        return dumps(o)

    @staticmethod
    def loads(s):
        return loads(s)
