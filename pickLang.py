#!/usr/bin/python3
import sys
import random

path = "langList" # Path to file

## Check if file exists or can make a new one
try:
	f = open(path, "r+")
except:
	try:
		f.close()
	except:
		pass
	print("Err:\n\tOpening file")
	exit(1)

## Allow to append languages
if "add" in sys.argv:
	f.close()
	f = open(path, "a+")
	toAdd = []
	print("Enter new languages (stop with \"END\"):")
	while True:
		newInp = input()
		if newInp == "END":
			break
		toAdd.append(newInp + "\n")
	for x in toAdd:
		f.write(x)
	f.close()
	exit(0)

langs = []
for x in f.readlines():
	langs.append(x.strip())
ind = random.randint(0, len(langs) - 1)
print("You will be writing in:\n####################\n####\t{}\t####\n####################".format(langs[ind]))
f.close()
