# FileProcessor.py
# this a sample program that will use module FileSystemClasses.py for iterating with files
# production version

## Modules
import fileSystemClasses

# -------------------
# Function Definition
# -------------------
def createFile(filePath):
	# file system classes - file manager object - create a new file
	fsc = fileSystemClasses.FileManager()
	# set file path
	fsc.setFilePath(filePath)
	# create file for writing
	fsc.createFile()

def appendFile(filePath, fileContent):
	# file system classes - file manager object - create a new file
	fsc = fileSystemClasses.FileManager()
	# set file path
	fsc.setFilePath(filePath)
	# create file for writing
	fsc.appendFile(fileContent)


# -------------------
# Main Body
# -------------------

fileNamePath = "/Users/marcelo/Documents/MAS/Python_Production/FileSystemClasses/outputFile.txt"

# ----------------------
# crete the working file
# ----------------------
createFile(fileNamePath)


# -----------------------------
# append some content to a file
# -----------------------------
content = "Second line has been appended\n"
appendFile(fileNamePath, content)




