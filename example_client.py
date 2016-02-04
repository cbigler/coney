#!/usr/bin/env python2

import jackrabbit


class ExampleProxy(jackrabbit.ProxyBase):
    def __init__(self, uri):
        super(ExampleProxy, self).__init__(uri)

    def foo_v1(self, name, age, email):
        return self.exec_rpc('foo', 1, arg1=name, arg2=age, arg3=email)

    def bar_v1(self):
        return self.exec_rpc('bar', 1)


proxy = ExampleProxy('amqp://dev:dev@localhost/')

response = proxy.foo_v1('John Doe', 41, 'john_doe@email.com')
if response:
    print('Success: {}'.format(response.return_value))
else:
    print('Error: ({}) {}'.format(response.code, response.details))

response = proxy.bar_v1()
if response:
    print('Success: {}'.format(response.return_value))
else:
    print('Error: ({}) {}'.format(response.code, response.details))
