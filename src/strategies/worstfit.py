from strategies import strategy

class WorstFit(strategy.Strategy):
	def calculate(self, servers, job):

		#Servers data format: servers = [...,[server_type, server_type_id, server_state, server_avail_time, server_cores, server_mem, server_disk_space],...,]

		worst_fit = None
		alt_fit = None
		worst_nonavailable = None

		for server in servers:
			
			# Individual checks for 3 different categories of possible returns
			if server.is_available():
				# if immediately available and new best worst fit
				if server.get_state() == 3 and (worst_nonavailable is None  or (server.cores_left(job) > worst_fit.cores_left(job))):
					worst_fit = server
				# If not immediately available but still will be available and new worst fit
				elif server.get_available_time() < worst_difference.get_available_time() and 
				(alt_fit is None or (server.cores_left(job) > alt_fit.cores_left(job))):
					alt_fit = server
			# if won't be available, but still a new worst fit
			elif worst_nonavailable is None or (server.cores_left(job) > worst_nonavailable.cores_left(job)):
				best_nonavailable = server
	
		#if worstFit found, return it
		if worst_fit is not None:
			return worst_fit
		#Otherwise, if alt_fit found, return this
		if alt_fit is not None:
			return alt_fit
		# otherwise just determine the worsed based on whatever is capable of running a job
		return best_nonavailable
			
