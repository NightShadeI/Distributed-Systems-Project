from strategies import strategy

class FirstFit(strategy.Strategy):
	def calculate(self, servers, job):
            print("test")
            return servers[0]
