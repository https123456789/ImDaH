import os

def getFileName():
	done = False
	filename = ""
	while not done:
		filename = str(input("Filename:"))
		try:
			f = open(filename, "rb")
			done = True
			f.close()
		except:
			print("Invalid filename.")
	return filename

def encode():
	filename = getFileName()
	file = open(filename, "ab")
	message = str(input("Message:"))
	file.write(bytes(message, "UTF-8"))
	file.close()

def decode():
	filename = getFileName()
	file = open(filename, "rb")
	binaryData = file.read()
	pointerIndex = binaryData.index(bytes.fromhex("FFD9")) + 2
	file.close()
	file = open(filename, "rb")
	file.seek(pointerIndex)
	byteData = file.read()
	message = byteData.decode("UTF-8")
	os.system("clear")
	print(message)
	file.close()

def strip():
	filename = getFileName()
	file = open(filename, "rb")
	binary = file.read()
	pointerIndex = binary.index(bytes.fromhex("FFD9")) + 2
	file.close()
	file = open(filename, "rb")
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
	file = open(filename, "wb")
	file.write(binaryData)
	file.close()
