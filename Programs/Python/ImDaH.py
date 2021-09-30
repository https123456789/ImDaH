import sys
sys.path.append("../../Libraries/Python/")
import jpeg

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

programDone = False
while not programDone:
	action = int(input("Quit: 0\nWrite a message: 1\nRead a message: 2\nClear a message: 3\nPNG: 4\nAction:"))
	if action == 0:
		programDone = True
	elif action == 1:
		filename = getFileName()
		jpegWorker = jpeg.JPEG(filename)
		message = str(input("Message:"))
		print(jpegWorker.encode(message))
	elif action == 2:
		filename = getFileName()
		file = open(filename, "rb")
		binaryData = file.read()
		pointerIndex = binaryData.index(bytes.fromhex("FFD9")) + 2
		file.close()
		file = open(filename, "rb")
		file.seek(pointerIndex)
		byteData = file.read()
		message = byteData.decode("UTF-8")
		print(message)
		file.close()
	elif action == 3:
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
	elif action == 4:
		filename = getFileName()
		file = open(filename, "rb")
		binaryData = file.read()
		pointerIndex = binaryData.index(bytes.fromhex("49454E44AE426082")) + 8
		file.seek(pointerIndex)
		byteData = file.read()
		message = byteData.decode("UTF-8")
		print(message)
		file.close()

	print("\n")