class Server:

	def __init__(self, server_params):

		server_params = server_params.split()
		self.server_name = server_params[0]
		self.server_id = server_params[1]
		self.server_state = server_params[2]
		self.available_time = server_params[3]
		self.cores = server_params[4]
		self.memory = server_params[5]
		self.disk = server_params[6]


	def get_server_name(self):
		return self.server_name


	def get_server_id(self):
		return self.server_id


	def get_server_state(self):
		return self.server_state


	def get_available_time(self):
		return self.available_time


	def get_cores(self):
		return self.cores


	def get_memory(self):
		return self.memory


	def get_disk(self):
		return self.disk