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


