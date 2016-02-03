#!/usr/bin/env python2
import coney
import logging
import sys


def rpc_func(arg1):
    return arg1 + 1


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
server = coney.Server('amqp://dev:dev@localhost/')
server.register_handler('test', 1, rpc_func)
server.run()
