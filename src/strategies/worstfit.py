from strategies import strategy

class WorstFit(strategy.Strategy):
	def calculate(self, servers, job):

		bestFit = sys.maxsize
		bestFitServer = sys.maxsize
		minAvail = sys.maxsize
		
		#Temporary, we can used loadParam() later, all these variables are purely for testing phase
		submit_time = job[0]
		submit_job_id = job[1]
		estimated_runtime = job[2]
		cores = job[3]
		memory = job[4]
		disk = job[5]

		#sysxml server types are: "tiny","small","medium","large","xlarge" -> map too serverType IDs -> 0, 1, 2, 3, 4, 5
		sysxml = [0,1,2,3,4,5]		
            
            
            return servers[0]
