from strategies import strategy

class BestFit(strategy.Strategy):
	def calculate(self, servers, job):

                #Data in servers = nested array servers[0][0] containing resource information from ds-server.
                #Servers data format: servers = [...,[server_type, server_type_id, server_state, server_avail_time, server_cores, server_mem, server_disk_space],...,]

                #According to pseudocode: set bestFit and MinAvail to large number e.g. MAX_INT.
		bestFit = sys.maxsize
		bestFitServer = sys.maxsize
		minAvail = sys.maxsize
		
		#Temporary, we can used loadParam() later, all these variables are purely for testing phase
                #job data format:   JOBN 240 1566 1 200 1200
                #jobN's data is simply stored in below variables
		submit_time = job[0]
		submit_job_id = job[1]
		estimated_runtime = job[2]
		cores = job[3]
		memory = job[4]
		disk = job[5]

		#ServerTypes as defined by system.xml: "tiny","small","medium","large","xlarge" -> map to serverType IDs -> 0, 1, 2, 3, 4, 5
		sysxml = [0,1,2,3,4,5]

		#Note that:		
		#The fitness value of a job to a server is defined as the difference between the number of cores the job requires and that in the server.	
		#If server is idle -> availTime = serverType[boottime] + job[submit_time].
		
		for serverType in sysxml:
			for server in servers:
		        	
                                #Note that:
				#Documentation defines fitness value as the difference between job cores and server cores.
                                #server[4] = number of server cores.
				#server[3] = available server time.

				#if serverType matches server[server_type_id] in servers.
				if serverType == server[1] and server[4] > cores:
					fitnessVal = server[4] - cores
                                        
                                        #if fitness value is less than bestfit or fitness value is same as bestFit and server available time is less than minAvail
					if fitnessVal < bestFit or (fitnessVal == bestFit and server[3] < minAvail):
						bestFit = fitnessVal
						bestFitServer = server
						minAvail = server[3]

                #This if-else will look like: if bestFit : return bestFit : else : return bestFit Active server based on initial resource capacity. 
		if bestFitServer != sys.maxsize:
			return bestFitServer
		else:
			return servers[0]
