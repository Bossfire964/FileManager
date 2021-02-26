import os
import sys
import arguments
import shutil

user = os.path.realpath(__file__).split('/')[2]
aph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def split(word):
    return [char for char in word] 

def contains(table, item):
	try:
		table.index(item)
	except Exception:
		return False
	finally:
		return True

def moveitem(path, name, fname):
	global user
	global aph
	global contains
	global split
	global shutil

	if (fname == ".DS_Store"):
		os.remove(path)
	else:

		if contains(aph, split(fname)[0]):
			shutil.move(path, "/Users/%s/FileManager/%s/%s" % (user, name, split(fname)[0]))
			filename, ext = os.path.splitext("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0], fname))
			


			if ext == "":
				if os.path.isdir("/Users/%s/FileManager/%s/%s/folder/%s" % (user, name, split(fname)[0].lower(), fname)):
					shutil.move("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0].lower(), fname), path)
					print("Returned %s" % (fname))

				if os.path.isdir("/Users/%s/FileManager/%s/%s/folder" % (user, name, split(fname)[0])):
					shutil.move("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0], fname), "/Users/%s/FileManager/%s/%s/folder/%s" % (user, name, split(fname)[0], fname))
				else:
					os.mkdir("/Users/%s/FileManager/%s/%s/folder" % (user, name, split(fname)[0]))
					shutil.move("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0], fname), "/Users/%s/FileManager/%s/%s/folder/%s" % (user, name, split(fname)[0], fname))

			else:

				ext = ext[1:]

				if os.path.exists("/Users/%s/FileManager/%s/%s/%s/%s" % (user, name, split(fname)[0].lower(), ext, fname)):
					shutil.move("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0].lower(),fname), path)
					print("Returned %s" % (fname))
				else:
					if os.path.isdir("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0], ext)):
						shutil.move("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0], fname), "/Users/%s/FileManager/%s/%s/%s/%s" % (user, name, split(fname)[0], ext, fname))
					else:
						os.mkdir("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0], ext))
						shutil.move("/Users/%s/FileManager/%s/%s/%s" % (user, name, split(fname)[0], fname), "/Users/%s/FileManager/%s/%s/%s/%s" % (user, name, split(fname)[0], ext, fname))


		else:
			shutil.move(path, "/Users/%s/FileManager/%s/Misc" % (user, name))
			filename, ext = os.path.splitext("/Users/%s/FileManager/%s/Misc/%s" % (user, name, fname))
			ext = ext[1:]

			if os.path.isdir("/Users/%s/FileManager/%s/Misc/%s" % (user, name, ext)):
				shutil.move("/Users/%s/FileManager/%s/Misc/%s" % (user, name, fname), "/Users/%s/FileManager/%s/Misc/%s/%s" % (user, name, ext, fname))
			else:
				os.mkdir("/Users/%s/FileManager/%s/Misc/%s" % (user, name, ext))
				shutil.move("/Users/%s/FileManager/%s/Misc/%s" % (user, name, fname), "/Users/%s/FileManager/%s/Misc/%s/%s" % (user, name, ext, fname))


	
if os.path.isdir("/Users/%s/FileManager/%s" % (user, arguments.args[0])):
	print(os.listdir("/Users/%s/Desktop/%s" % (user, "FileInput")))
	files = os.listdir("/Users/%s/Desktop/%s" % (user, "FileInput"))
	for file in files:
		moveitem("/Users/%s/Desktop/FileInput/%s" % (user, file), arguments.args[0], file)
else:
	print("FileManager does not exist")