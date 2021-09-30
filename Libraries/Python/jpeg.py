class JPEG:
	def __init__(self, filename):
		self.filename = filename
	def encode(self, message):
		file = open(self.filename, "ab")
		file.write(bytes(message, "UTF-8"))
		file.close()
	def decode(self):
		file = open(self.filename, "rb")
		binaryData = file.read()
		pointerIndex = binaryData.index(bytes.fromhex("FFD9")) + 2
		file.close()
		file = open(self.filename, "rb")
		file.seek(pointerIndex)
		byteData = file.read()
		message = byteData.decode("UTF-8")
		file.close()
		return message
	def strip(self):
		file = open(self.filename, "rb")
		binary = file.read()
		pointerIndex = binary.index(bytes.fromhex("FFD9")) + 2
		file.close()
		file = open(self.filename, "rb")
		done = False
		binaryData = b""
		while not done:
			byte = file.read(1)
			binaryData += byte
			pos = file.tell()
			if pos == pointerIndex:
				done = True
				break
		file.close()
		file = open(self.filename, "wb")
		file.write(binaryData)
		file.close()
