from strategies import strategy

class BestFit(strategy.Strategy):
	def calculate_(self,jobParams,resourceInfo):
	    
            return resourceInfo[0][0]
