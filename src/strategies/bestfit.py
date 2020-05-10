from strategies import strategy

class BestFit(strategy.Strategy):
	def calculate(self, servers, job):
		return servers[0]
