import socket

class Client:
	def __init__(self, host, port=5555, byteSize=2048, encoding="utf-8"):
		self.host = host
		self.port = port
		self.byteSize = byteSize
		self.encoding = encoding
		self.addr = (self.host, self.port)

		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect(self.addr)

	def getMessages(self):
		messages = self.client.recv(self.byteSize).decode(self.encoding)
		return messages

	def sendMessage(self, data):
		self.client.send(data.encode(self.encoding))