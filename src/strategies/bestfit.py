from strategies import strategy


class BestFit(strategy.Strategy):
    def calculate(self, servers, job):

        found = False
        best_fit = servers[0]

        # Iterate over servers
        for server in servers:

            server_available = server.is_available()
            # If an available server has been found, non-availables don't matter
            if found and not server_available:
                pass

            # If this is the first available server, set it to the current best
            if not found and server_available:
                found = True
                best_fit = server
                pass

            # Get the current and best core counts
            current_difference = server.cores_left(job)
            best_difference = best_fit.cores_left(job)

            # If this core count is better than the best
            if ((core_difference < best_difference) or 
            (core_difference == best_difference and server.get_available_time() < best_fit.get_available_time())):
                best_fit = server

        return best_fit
