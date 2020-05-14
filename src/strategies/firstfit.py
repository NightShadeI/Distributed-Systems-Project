from strategies import strategy


class FirstFit(strategy.Strategy):
    def calculate(self, servers, job):
        system = self.tree.getroot()
        for serverType in system[0]:
            for server in servers:
                if(serverType.attrib["type"] == server.get_name()):
                    if(server.cores_left(job) >= 0):
            	        return server
        
        return servers[0]
