#!/usr/bin/env python2
import jackrabbit
import logging
import sys


def rpc_func(arg1):
    return arg1 + 1


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
server = jackrabbit.Server('amqp://dev:dev@localhost/')
server.register_handler('test', 1, rpc_func)
server.run()
