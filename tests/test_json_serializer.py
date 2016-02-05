import unittest

from jackrabbit.serializers.json_serializer import JsonSerializer


class TestJsonSerializer(unittest.TestCase):
    def test_dumps(self):
        s = JsonSerializer.dumps({u"compact": True, u"schema": 0})
        self.assertEqual(s, '{"compact": true, "schema": 0}')

    def test_loads(self):
        s = JsonSerializer.loads('{"compact": true, "schema": 0}')
        self.assertEqual(s, {u"compact": True, u"schema": 0})
