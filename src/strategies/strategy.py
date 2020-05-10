import xml.etree.ElementTree as ET

class Strategy:

	def readSystemData(self):
		self.tree = ET.parse('../simulator/system.xml')

	'''
	def loadParameters(self, jobParams):
		self.submit_time = int(jobParams[0])
		self.job_id = int(jobParams[1])
		self.estimated_runtime = int(jobParams[2])
		self.cores = int(jobParams[3])
		self.memory = int(jobParams[4])
		self.disk = int(jobParams[5])
		print("hey")
	'''

	def calculate(self, servers, job):
		#self.loadParameters(jobParams)
		#return self.calculate_(jobParams)
		raise Exception("Not implemented")

	'''
	def calculate_(self):
		raise Exception("Not implemented")
	'''

