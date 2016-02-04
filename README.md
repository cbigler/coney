# jackrabbit
Jackrabbit is a simple, light-weight remote procedure call (RPC) library for RabbitMQ.
It includes tools for quickly building both RPC servers and client proxies.

## Design Goals
- quick and easy to get started
- simple to use
- fast and efficient

Jackrabbit was designed as a transport implementation for a micro-service application bus. Remote calls
are proxied through RabbitMQ in msgpack format, the server routes the request to the matching registered
handler, and the return value is sent back across RabbitMQ and returned to the caller.

## Requirements
- pika

## Examples
For this example, we'll create a simple server which implements a couple of callable methods and
we'll also create a proxy to remotely call the method.

### Server
```python
import jackrabbit

def foo(arg1, arg2, arg3):
    return '{}:{}:{}'.format(arg1, arg2, arg3)

def bar():
    return 42

server = jackrabbit.Server('amqp://guest:guest@localhost/')
server.register_handler('foo', 1, foo)
server.register_handler('bar', 1, bar)
server.run()
```

### Proxy/Client
```python
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
```


