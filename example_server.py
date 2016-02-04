#!/usr/bin/env python2
import jackrabbit
import logging
import sys


def foo(arg1, arg2, arg3):
    return '{}:{}:{}'.format(arg1, arg2, arg3)


def bar():
    return 42

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
server = jackrabbit.Server('amqp://guest:guest@localhost/')
server.register_handler('foo', 1, foo)
server.register_handler('bar', 1, bar)
server.run()
