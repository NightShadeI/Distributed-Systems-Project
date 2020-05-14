from strategies import strategy


class FirstFit(strategy.Strategy):
    def calculate(self, servers, job):
        for server in servers:
            if(server.get_state() != 4 and server.get_available_time() != -1):
            	return server
        return servers[0]
