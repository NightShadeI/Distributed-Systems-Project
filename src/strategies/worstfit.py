from strategies import strategy

class WorstFit(strategy.Strategy):

    def calculate(self, servers, job):
        	
        worstFit = -9999999
        altFit = -9999999
        worst_server = servers[0]
        alt_server = servers[0]
        system = self.tree.getroot()
        for serverType in system[0]:
            for server in servers: 
                if server.cores_left(job) >= 0:
                    if (server.cores_left(job) > worstFit) and (2 <= server.get_state() <= 3):
                        worstFit = server.cores_left(job)
                        worst_server = server
                    elif server.cores_left(job) > altFit and (server.get_available_time() != -1):
                        altFit = server.cores_left(job)
                        alt_server = server
            if worstFit >= 0:
                return worst_server
            if altFit >= 0:
                return alt_server
       
        return worst_server
