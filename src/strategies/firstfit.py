from strategies import strategy

class FirstFit(strategy.Strategy):
	def calculate(self, servers, job):
            for server in servers:
                if(servers[server][3]!=-1):
                    return servers[server]
            return servers[0]
