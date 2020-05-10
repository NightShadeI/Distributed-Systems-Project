from strategies import strategy

class BestFit(strategy.Strategy):
	def calculate_(self, jobParams):
		return jobParams[0][0]
