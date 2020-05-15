"""
Distributed Systems group project
Authors: Thomas Tapner
Student ID: 45387168
Practical session: Friday 10:00am
"""

from strategies import strategy


class FirstFit(strategy.Strategy):
	def calculate(self, servers, job):
		my_dict = {}
		# get the root element
		system = self.tree.getroot()
		# Iterate over server types and sizes, stored in dictionary ordered by key value (coreCount)
		for serverDefinitions in system[0]:
			serverType = serverDefinitions.attrib["type"]
			my_dict[serverType] = int(serverDefinitions.attrib["coreCount"])
		sorted_my_dict = sorted(my_dict.items(), key=lambda kv: kv[1])
		# Iterate item in sorted dictionary (dict sorted by coreCount/server size)
		for item in sorted_my_dict:
			# Iterate over possible servers, only returning the first match of the server type that can run the job
			for server in servers:
				if(server.get_name() == item[0] and server.can_run(job)):
					return server
		# If none capable of running job, just return the first server
		return servers[0]
