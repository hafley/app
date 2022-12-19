# app.py
# version 0.1

import os
import subprocess
import sys
import importlib

try:
	import readchar
except ImportError:
	print("Installing readchar module. You're welcome.")
	importlib.import_module("pip").main(["install", "readchar"])
	import readchar

def main():
	os.system('clear') 
	last_command = ""
	print("Welcome to the app • Greet • Exit • Restart\n\nEnter a command:")

	actions = {
		"g": lambda: print("Gangster"),
		"r": lambda: (subprocess.run(["python3", "app.py"]), sys.exit())
	}

	while True:
		command = readchar.readkey()
		if isinstance(command, bytes):
			command = str(command, "utf-8")
		if command == "e":
			os.system('clear')
			sys.exit()
		if command == "\x1b[A":
			command = last_command
		elif command != "KEY_UP":
			if command in actions:
				last_command = command
			else:
				continue

		action = actions.get(command)
		if action:
			action()

if __name__ == "__main__":
	main()
