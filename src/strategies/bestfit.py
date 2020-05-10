from strategies import strategy

class BestFit(strategy.Strategy):
<<<<<<< HEAD
	def calculate(self, servers, job):
		return servers[0][0]
=======
	def calculate_(self,jobParams,resourceInfo):
	    
            return resourceInfo[0][0]
>>>>>>> a601353810db32cef6bccb340a4630e7765a2a7f
