"""
Distributed Systems group project
Authors: Thomas Tapne
Student ID: 45387168
Practical session: Friday 10:00am
"""

from strategies import strategy


class FirstFit(strategy.Strategy):
	def calculate(self, servers, job):
		# get the root element
		system = self.tree.getroot()
		# Iterate over each of the server types
		for serverType in system[0]:
			# Iterate over possible servers, only returning the first match of the server type that can run the job
			for server in servers:
				if(serverType.attrib["type"] == server.get_name() and server.can_run(job)):
					return server
		# If none capable of running job, just return the first server
		return servers[0]
