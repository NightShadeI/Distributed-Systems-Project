from strategies import strategy

class WorstFit(strategy.Strategy):
	def calculate(self, servers, job):
		return servers[0]
