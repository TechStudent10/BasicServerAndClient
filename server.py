import socket
from _thread import *

CLIENT = "[CLIENT]"
ERROR = "[ERROR]"
SERVER = "[SERVER]"
CONNECTION = "[CONNECTION]"

class Server:
	def __init__(self, host=socket.gethostbyname(socket.gethostname()), port=5555, maxPeople=10):
		self.host = host
		self.port = port
		self.maxServer = maxPeople
		self.addr = (self.port, self.port)

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(self.addr)
		try:
			self.server.listen(self.maxPeople)
		except socket.error as e:
			print(ERROR, e)

	def connectedClient(self, conn, addr):
		try:
			while 1:
				pass
		except socket.error as e:
			print(ERROR, e)

	def listen(self):
		while 1:
			conn, addr = self.server.accept()
			print(CONNECTION, "New connection:", addr)

			start_new_thread(self.connectedClient, args=(conn, addr))