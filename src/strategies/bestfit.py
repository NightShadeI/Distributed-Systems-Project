from strategies import strategy

class BestFit(strategy.Strategy):
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

		#sysxml server types are: "tiny","small","medium","large","xlarge" -> map too -> 0, 1, 2, 3, 4, 5
		sysxml = [0,1,2,3,4,5]

		```
		Note that:		
		The fitness value of a job to a server is defined as the difference between the number of cores the job 		requires and that in the server.		
		If server is idle -> availTime = serverType[boottime] + job[submit_time].
		```
