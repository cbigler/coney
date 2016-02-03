#!/usr/bin/env python2

import coney


class ExampleProxy(coney.ProxyBase):
    def __init__(self, uri):
        super(ExampleProxy, self).__init__(uri)

    def example_rpc(self, my_arg):
        return self.exec_rpc('test', 1, arg1=my_arg)


proxy = ExampleProxy('amqp://dev:dev@localhost/')
response = proxy.example_rpc(10)
if response:
    print('Success: {}'.format(response.return_value))
else:
    print('Error: ({}) {}'.format(response.code, response.details))
