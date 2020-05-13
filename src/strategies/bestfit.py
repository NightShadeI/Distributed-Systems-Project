from strategies import strategy


class BestFit(strategy.Strategy):
    def calculate(self, servers, job):

        found = False
        best_fit = servers[0]

        for server in servers:
            if server.is_available():
                if server.can_run(job):
                    current_difference = server.cores_left(job)
                    best_difference = best_fit.cores_left(job)
                    if ((core_difference < best_difference) or 
                    (core_difference == best_difference and server.get_available_time() < best_fit.get_available_time())):
                        best_fit = server
                        found = True
                elif not found:
                    best_fit = server
        return best_fit
