import socket

"""
- AF: Address Family
- PF: Protocol Family.
- INET: INTERNET in AF_INET, PF_INET

- AF_INET refers to addresses from the internet, IP addresses specifically
- PF_INET refers to anything in the protocol, usually sockets/ports

AF_INET is an address family that is used to designate
the type of addresses that your socket can communicate with
(in this case, Internet Protocol v4 addresses)

When you create a socket, you have to specify its address family,
and then you can only use addresses of that type with the socket.

For the most part, sticking with AF_INET for socket programming
over a network is the safest option.
There is also AF_INET6 for Internet Protocol v6 addresses.
Same logic for Sock_stream.
"""
HEADER_SIZE = 10


# socket is an endpoint of communication (receives data)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(5) # this is queue for incoming messages
# don't know what the message is yet


def header_construction(message):
    return f"{len(message):<{HEADER_SIZE}}" + message

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established")
    # can also do string.encode(...) or something else 
    clientsocket.send(bytes(header_construction("welcome! to the server!"), "utf-8"))
