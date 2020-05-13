from strategies import strategy

class FirstFit(strategy.Strategy):
	def calculate(self, servers, job):
            for server in servers:
                if(int(server[3])!=-1):
                    return server
            return servers[0]
