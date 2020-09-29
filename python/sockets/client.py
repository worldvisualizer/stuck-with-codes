import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))

# attempt to concatenate buffered messages
# without closing connection from the server
# makes client waiting

# from the server-side, there's: clientsocket.close()
HEADER_SIZE = 10


while True:
    full_message = ''
    new_message = True
    while True:
        # sockets are communicating by byte streams
        message = s.recv(8) # this is buffer, how big of a chunk of data 
        # do we want to receive at a time
        if new_message:
            print(message)
            print(f"new message length: {message[:HEADER_SIZE]}")
            message_length = int(message[:HEADER_SIZE])
            new_message = False    
        
        full_message += message.decode("utf-8")
        if len(full_message) - HEADER_SIZE == message_length:
            print("full message received", full_message[:HEADER_SIZE])
            new_message = True

    print(full_message)
