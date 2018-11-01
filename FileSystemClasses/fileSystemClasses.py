#
# FileSystemClasses
#	- File Manager
#		. create file
#		. append file
#		. read file


# libraries
import os

# FileSystemClasses.py
class FileManager(object):
	def __init__(self):
		print("🍺 File Manager created.")

	def setFilePath(self, filePath="default_value"):
		self.filePath = filePath

		print("🍺 This is the file path ", filePath)


	def createFile(self):
		instanceFile = open(self.filePath, "w")
		instanceFile.write("")
		instanceFile.close

		print("🍺 -FileManager-createFileForOperation finished")
		print("🍺 -...-FilePath: ", self.filePath)
		print("🍺 -FileManager-end-method")

	def appendFile(self, content):
		self.content = content
		instanceFile = open(self.filePath, "a")
		instanceFile.write(content)
		instanceFile.close		


		print("🍺 -FileManager-appendFile finished")
		print("🍺 -...-FilePath: ", self.filePath)
		print("🍺 -...-Content: ", content)
		print("🍺 -FileManager-end-method")

	def readFile(self):
		instanceFile = open(self.filePath, "r")
		instanceFile.seek(0)

		print("🍺 -FileManager-readFile finished")
		print("🍺 -...-FilePath: ", self.filePath)

		return instanceFile.read()

