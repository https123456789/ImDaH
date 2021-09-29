import sys
sys.path.append("../../Libraries/Python/")
import lib
programDone = False
while not programDone:
	action = int(input("Write a message: 1\nRead a message: 2\nClear a message: 3\nQuit: 4\nAction:"))
	if action == 1:
		lib.encode()
	elif action == 2:
		lib.decode()
	elif action == 3:
		lib.strip()
	elif action == 4:
		programDone = True
	print("\n")