from strategies import strategy

class WorstFit(strategy.Strategy):
	def calculate(self, servers, job):

		#Might just use same variable to store values and server data in future due to python magic, leaving this for now.
                worstFit = sys.minsize
		worstFitServer = sys.minsize
		altFit = sys.minsize
                altFitServer = sys.minsize
                defShortTime = 100
		
		#Temporary, we can used loadParam() later, all these variables are purely for testing phase
		submit_time = job[0]
		submit_job_id = job[1]
		estimated_runtime = job[2]
		cores = job[3]
		memory = job[4]
		disk = job[5]

		#sysxml server types are: "tiny","small","medium","large","xlarge" -> map too serverType IDs -> 0, 1, 2, 3, 4, 5
		sysxml = [0,1,2,3,4,5]

		for serverType in sysxml:
			for server in servers:
				#if server type is same and number of cores on server are more than or equal to how many the job requires. Also, note that:
		                #Documentation defines fitness Value as difference between job cores and available server cores.
                                #server[4] = number of server cores.
                                #server[3] = avaiable server time.
                                #server[2] = server state -> 0:inactive, 1:booting, 2:idle, 3:active, 4:unavailable.
				
				if serverType == server[1] and server[4] >= cores:
					fitnessVal = server[4] - cores

                                        # server[2] == 3 : server status is Available
					if fitnessVal > worstFit and server[2] == 3:
						worstFit = fitnessVal
						worstFitServer = server
                                        #server[3] : server available in short amount of time.
					elif fitnessVal > altFit and server[3] < defShortTime:
                                                altFit = fitnessVal
		
                #if: worstFit found, return worstFitServer	
		if worstFit:
			return worstFitServer
                #elif: altFit found, return altFitServer
                elif altFit:
			return altFitServer
                #else: Return the worst-fit Active server based on  initial resource capacity.
                else:
                         return server[0] 
            
            return servers[0]
