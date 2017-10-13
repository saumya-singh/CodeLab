import requests
import os


class File:

	base_url = "http://192.168.43.190:8080/CodeGrader2"
	base_directory = "/tmp"
	
	
	def __init__(self, submission_id, file_name):
		self.submission_id = submission_id
		self.file_name = file_name.strip()
		self.filename_noext, file_ext = os.path.splitext(self.file_name)
		self.file_ext = file_ext[1:]
		


	def downloadFile(self):     
		r = requests.get(self.getRemoteFileUrl())
		if not os.path.exists(self.getLocalDestinationDir()):  
			os.makedirs(self.getLocalDestinationDir())  
		print self.getRemoteFileUrl()
		output = open( self.getLocalFileLocation() , 'w')
		output.write(r.text)
		output.close()
		return True

	def getRemoteFileUrl(self):
		return File.base_url+"/"+self.submission_id+"/"+self.file_name


	def getLocalDestinationDir(self):
		return File.base_directory+"/sol_"+self.submission_id

	def getLocalFileLocation(self):
		return self.getLocalDestinationDir()+"/" + self.file_name

	def getLanguage(self):
		return self.file_ext.lower()

	def getClassName(self):
		return self.filename_noext

	def getFileName(self):
		return self.file_name  

	

if __name__ == "__main__":
	f = File("1234", "armstrong.c", "1")
	#print f.downloadFile()
	#print f.getFileContent()
	print f.getTestFilePath("1")

