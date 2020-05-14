from strategies import strategy

class FirstFit(strategy.Strategy):
	def calculate(self, servers, job):
    	return servers[0]
