from strategies import strategy

class WorstFit(strategy.Strategy):
	def calculate_(self, jobParams):
		return jobParams[0][0]
