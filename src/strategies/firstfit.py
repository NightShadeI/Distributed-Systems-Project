from strategies import strategy

class FirstFit(strategy.Strategy):
	def calculate(self, servers, job):
            for server in servers:
                #if server.is_available():
                return server
            return servers[0]
