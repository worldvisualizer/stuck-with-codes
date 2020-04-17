### Telnet Chat

Build a simple Telnet Chat Server.

Once user connects to the chat server using Telnet, they can use the following commands to talk to the server:

- `/nick <name>` - reserve a name, name is mandatory for sending messages.
- `/join <room>` - join a room, if room doesn't exist the new room will be created.
- `/say	<msg>` - send message to everyone in a room.
- `/quit` - disconnects from the chat server.

### Example

```bash
telnet localhost 8080
Trying ::1...
Connected to localhost.
Escape character is '^]'.

/nick john
/join golang
/say Hi Gophers!
```