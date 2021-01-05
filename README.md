# Basic Server and Client For Python

 A server and client for online Python Projects.

---

To use the server and the client, you need to create a `server.py` and `client.py` file.

You need to import the Server class into your server.py file.

The parameters of Server are:

`Host`: IP Address that you want your server to run on [127.0.0.1].

`Port`: The Port that you want your server to run on [5555].

`maxPeople`: The maximum amount of people you want on your server [10].

`byteSize`: The amount of bytes you want sent to clients [2048].

`encoding`: The encoding for encoding and decoding messages [utf-8].

Use the listen method to activate your server.

---

You need to import the Client class into your client.py file.

The parameters of Client are:

`Host`: IP Address that your server is runming on.

`Port`: The Port that your server is running on [5555].

`byteSize`: The amount of bytes you want sent to the server [2048].

`encoding`: The encoding for encoding and decoding messages [utf-8].

You can use the getMessages method to get the messages and the send method to send a message.
