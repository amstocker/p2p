# Python p2p

*This is a work in progress!*  I'm just tryin to wrap my mind around IPFS,
libp2p, and distributed systems.


## Built on asyncio

This is a Python implementation of libp2p as described in more detail
[here](https://github.com/ipfs/specs/tree/master/libp2p).  The interface described
in the specs uses callbacks, but in the spirit of Python's `asyncio` this
implentation will make use of coroutines.

A lot of the libp2p functionality can actually be mapped one-to-one `asyncio`
classes:

```python
# duplex stream
p2p.Stream = asyncio.protocols.Protocol

# generic transport
p2p.Transport = asyncio.transports.Transport

```


## p2p Node

The base functionality of libp2p comes from the `Node` class for which the
user provides support for any protocols:

```python
from p2p import Node, BaseProtocolHandler


class MyProtocolHandler(BaseProtocolHandler):
  pass


if __name__ == "__main__":
  
  # build new node
  node = Node(
    config="~/.p2p.conf",
    handlers={
      '<multicodec>': MyProtocolHandler
    }
  )

  # start event loop
  node.run()

```
