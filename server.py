import socket
from _thread import *

CLIENT = "[CLIENT]"
ERROR = "[ERROR]"
SERVER = "[SERVER]"
CONNECTION = "[CONNECTION]"

class Server:
	def __init__(self, host=socket.gethostbyname(socket.gethostname()), port=5555, maxPeople=10, byteSize=2048, encoding="utf-8"):
		self.host = host
		self.port = port
		self.maxPeople = maxPeople
		self.byteSize = byteSize
		self.encoding = encoding
		self.addr = (self.host, self.port)

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print(SERVER, "Server is starting")
		self.server.bind(self.addr)
		try:
			self.server.listen(self.maxPeople)
		except socket.error as e:
			print(ERROR, e)

		print(SERVER, "Server is listening on", self.host, "on port", self.port)

	def connectedClient(self, conn, addr):
		try:
			while 1:
				data = conn.recv(self.byteSize).decode(self.encoding)
				print(f"{addr} {data}")
				if not data:
					break

				#conn.send("Message sent".encode(self.encoding))
				conn.sendall(data.encode(self.encoding))
		except socket.error as e:
			print(ERROR, e)

		conn.close()
		print(CLIENT, addr, "has disconnected.")

	def listen(self):
		while 1:
			conn, addr = self.server.accept()
			print(CONNECTION, "New connection:", addr)

			start_new_thread(self.connectedClient, (conn, addr))