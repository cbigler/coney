import unittest

from jackrabbit.serializers.msgpack_serializer import MsgpackSerializer


class TestMsgpackSerializer(unittest.TestCase):
    def test_dumps(self):
        s = MsgpackSerializer.dumps({u"compact": True, u"schema": 0})
        self.assertEqual(s, '\x82\xa7compact\xc3\xa6schema\x00')

    def test_loads(self):
        s = MsgpackSerializer.loads('\x82\xa7compact\xc3\xa6schema\x00')
        self.assertEqual(s, {u"compact": True, u"schema": 0})
