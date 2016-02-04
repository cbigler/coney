# jackrabbit
Jackrabbit is a simple, light-weight remote procedure call (RPC) library for RabbitMQ.
It includes tools for quickly building both RPC servers and client proxies.

Remote calls are proxied through RabbitMQ, the server routes the request to the matching
registered handler, and the method's return value is sent back across RabbitMQ and returned
to the caller.

## Design Goals
- quick and easy to get started
- simple to use
- fast and efficient

## Requirements
- pika

## Basic Features
- create servers that implement remotely callable functionality
- easily create proxy classes to remotely call methods

### Additional Features
- default transport serialization is through msgpack to minimize the size of data sent through RabbitMQ;
other encodings can be used and the library includes a JSON serializer to make debugging easier. User supplied
serializers are also supported.
- optional (off by default) compression of the data sent through RabbitMQ; jackrabbit comes with a zlib
implementation, user supplied implementations are also supported.
- server prefetch count defaults to 10, but is configurable as a parameter when the `Server` is created.
- dedicated error code, with method provided error details in the `Response` provides a mechanism to report
rich error messages to the caller.
- exceptions thrown within RPC handlers are automatically caught and converted to a `Response`, you don't need
to write extensive exception handlers in every method to ensure a stray exception won't crash your server.
- the proxy base implements a re-connect mechanism so that a severed connection to RabbitMQ is re-established before a
call is made (e.g. due to missed heartbeat for long-lived proxies)

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


