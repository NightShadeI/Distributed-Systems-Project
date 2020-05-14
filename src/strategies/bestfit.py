from strategies import strategy


class BestFit(strategy.Strategy):
    def calculate(self, servers, job):

        bestFit = 9999999
        minAvail = 9999999
        bfServer = servers[0]

        for server in servers:
            # if the difference between server cores and required job cores is greater than 0 
            # and less than best fit
            # OR
            # 
            if((server.cores_left(job) >= 0 and server.cores_left(job) < bestFit) or
                    (server.cores_left(job) == bestFit and server.get_available_time() < minAvail)):
                bestFit = server.cores_left(job)
                minAvail = server.get_available_time()
                bfServer = server  

        return bfServer

         
