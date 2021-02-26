import os
import sys
import arguments
import shutil

user = os.path.realpath(__file__).split('/')[2]
aph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def MakeFileFolder(name):
	global user
	global aph

	os.mkdir("/Users/%s/FileManager/%s" % (user, name))
	for letter in aph:
		os.mkdir("/Users/%s/FileManager/%s/%s" % (user, name, letter))
	os.mkdir("/Users/%s/FileManager/%s/Misc" % (user, name))

if arguments.args[0] == "new":
	if os.path.isdir("/Users/%s/FileManager" % (user)):
		MakeFileFolder(arguments.args[1])
		print("Made file %s" % (arguments.args[1]))
if arguments.args[0] == "fd":
	shutil.copytree("/Users/%s/FileManager/%s/%s/%s" % (user, arguments.args[1], arguments.args[2], arguments.args[3]), "/Users/%s/Desktop/%s" % (user, arguments.args[3]))
if arguments.args[0] == "over":
	file = os.listdir("/Users/" + user + "/Desktop/FolderInput")[0]
	shutil.rmtree("/Users/%s/FileManager/%s/%s/folder/%s" % (user, arguments.args[1], arguments.args[2], file))
	shutil.move("/Users/%s/Desktop/FolderInput/%s" % (user, file), os.path.join("/Users/%s/FileManager/%s/%s/folder" % (user, arguments.args[1], arguments.args[2]),file))
if arguments.args[0] == "clear":
	if os.path.isdir("/Users/%s/FileManager/%s" % (user, arguments.args[1])):
		despath = "/Users/%s/Desktop/FileSystemOutput" % (user)
		os.mkdir(despath)
		fullcontents = os.listdir("/Users/%s/FileManager/%s" % (user, arguments.args[1]))
		for folder in fullcontents:
			if folder == ".DS_Store":
				os.remove("/Users/%s/FileManager/%s/.DS_Store" % (user, arguments.args[1]))
			else :
				contents = os.listdir("/Users/%s/FileManager/%s/%s" % (user, arguments.args[1], folder))
				for subfolder in contents:
					if subfolder == ".DS_Store":
						os.remove("/Users/%s/FileManager/%s/%s/.DS_Store" % (user, arguments.args[1], folder))
					else:
						subcontents = os.listdir("/Users/%s/FileManager/%s/%s/%s" % (user, arguments.args[1], folder, subfolder))
						for item in subcontents:
							if item == ".DS_Store":
								os.remove("/Users/%s/FileManager/%s/%s/%s/.DS_Store" % (user, arguments.args[1], folder, subfolder))
							else:
								shutil.move("/Users/%s/FileManager/%s/%s/%s/%s" % (user, arguments.args[1], folder, subfolder, item), despath)
			print("Cleared File system")
	else:
		print("That is not a current file system")