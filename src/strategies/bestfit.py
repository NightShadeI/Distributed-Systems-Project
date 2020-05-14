from strategies import strategy

class BestFit(strategy.Strategy):
    def calculate(self, servers, job):
        system = self.tree.getroot()
        bestFit = 9999999
        minAvail = 9999999
        bfServer = servers[0]
        for serverType in system[0]:
            for server in servers:
                if(serverType.attrib["type"] == server.get_name()):
                    if((server.cores_left(job) >= 0 and server.cores_left(job) < bestFit) or
                        (server.cores_left(job) == bestFit and server.get_available_time() < minAvail)):
                        bestFit = server.cores_left(job)
                        minAvail = server.get_available_time()
                        bfServer = server  

        return bfServer
