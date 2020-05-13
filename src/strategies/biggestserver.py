from strategies import strategy

class BiggestServer(strategy.Strategy):

	def calculate(self, servers, job):
		servers = self.tree.getroot().find("servers")
		biggest_server = servers[0]
		for server in servers:
		    if int(server.attrib['coreCount']) > int(biggest_server.attrib['coreCount']):
		        biggest_server = server        
		return biggest_server.attrib['type']