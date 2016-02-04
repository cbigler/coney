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
    import jackrabbit

    def foo(arg1, arg2, arg3):
        return arg1 + arg2 + arg3

    def bar():
        return 42

    server = jackrabbit.Server('amqp://guest:guest@localhost/')
    server.register_handler('foo', 1, foo)
    server.register_handler('bar', 1, bar)
    server.run()

### Proxy/Client
    import jackrabbit

    class ExampleProxy(jackrabbit.ProxyBase):
        def __init__(self, uri):
            super(ExampleProxy, self).__init__(uri)

        def foo_v1(name, age, email):
            return self.exec_rpc('foo', 1, arg1=name, arg2=age, arg3=email)

        def bar_v1():
            return self.exec_rpc('bar', 1)

    proxy = ExampleProxy('amqp://guest:guest@localhost/')
    resp = proxy.foo(1, 'abc', ['xyz', '123'])
    if resp:
        print('Success: {}'.format(resp.return_value))
    else:
        print('Error: ({}) {}'.format(resp.code, resp.details))



