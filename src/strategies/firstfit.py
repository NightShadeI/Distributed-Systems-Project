from strategies import strategy

class FirstFit(strategy.Strategy):
	def calculate_(self, jobParams):
		return jobParams[0][0]
