from strategies import strategy


class BestFit(strategy.Strategy):
    def calculate(self, servers, job):

        bestFit = 9999999
        minAvail = 9999999
        found = False
        bfServer = servers[0]

        for server in servers:

            # For the sake of readability
            serverState = int(server[2])
            unavailable = 4
            serverCores = int(server[4])
            coresRequired = int(job[3])
            serverAvailTime = int(server[3])
            immediatelyAvail = -1

            if(serverState != unavailable):
                if((serverCores - coresRequired >= 0 and serverCores - coresRequired < bestFit) or
                        (serverCores - coresRequired == bestFit and serverAvailTime < minAvail)):
                    bestFit = serverCores - coresRequired
                    minAvail = serverAvailTime
                    found = True
                    bfServer = server
        if(found):
            return bfServer
        else:
            for server in servers:
                if(serverState != unavailable and serverAvailTime != immediatelyAvail):
                    return server
            return bfServer
