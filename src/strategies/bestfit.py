from strategies import strategy

class BestFit(strategy.Strategy):
        def calculate(self, servers, job):
                bestFit = 9999999
                minAvail = 9999999
                found = False
                daServer = servers[0]
                for server in servers:
                        if(int(server[2])!=4):
                                if((int(server[4]) - int(job[3]) >= 0 and int(server[4]) - int(job[3]) < bestFit) or
                                        (int(server[4]) - int(job[3]) == bestFit and int(server[3]) < minAvail)):
                                                bestFit = int(server[4]) - int(job[3])
                                                minAvail = int(server[3])
                                                found = True
                                                daServer = server
                if(found):
                        return daServer
                else:
                        for server in servers:
                                if(int(server[2])!=4 and int(server[3])!=-1):
                                        return server
                        return daServer
