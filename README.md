# Basic Server and Client For Python

 A server and client for online Python Projects.

---

To use the server and the client, you need to create a `server.py` and `client.py` file.

server.py:
from BasicServerAndClient.server import Server
server = Server(host="127.0.0.1", port=5555)
server.listen()

The parameters of Server are:

`Host`: IP Address that you want your server to run on [127.0.0.1].

`Port`: The Port that you want your server to run on [5555].

`maxPeople`: The maximum amount of people you want on your server [10].

`byteSize`: The amount of bytes you want sent to clients [2048].

`encoding`: The encoding for encoding and decoding messages [utf-8].

---

client.py:

    from BasicServerAndClient.client import Client
    client = Client(host="127.0.0.1", port=5555)
    while 1:

        message = client.getMessages()

        if len(message) != 0:

            print(message)

        client.send("Message recived")

The parameters of Client are:

`Host`: IP Address that your server is runming on.

`Port`: The Port that your server is running on [5555].

`byteSize`: The amount of bytes you want sent to the server [2048].

`encoding`: The encoding for encoding and decoding messages [utf-8].
