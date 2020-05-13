class Server:

	def __init__(self, server_params):

		server_params = server_params.split()
		self.name = server_params[0]
		self.id = server_params[1]
		self.state = int(server_params[2])
		self.available_time = int(server_params[3])
		self.cores = int(server_params[4])
		self.memory = int(server_params[5])
		self.disk = int(server_params[6])


	def get_name(self):
		return self.server_name


	def get_id(self):
		return self.id


	def get_state(self):
		return self.server_state


	def get_available_time(self):
		return self.available_time


	def get_cores(self):
		return self.cores


	def get_memory(self):
		return self.memory


	def get_disk(self):
		return self.disk


	def is_available(self):
		return not (self.get_state() < 4 or self.available_time() < 0)


	def can_run(self, job):
		core_check = self.get_cores() >= job.get_cores()
		memory_check = self.get_memory() >= job.get_memory()
		disk_check = self.get_disk() >= job.get_disk()
		return core_check and memory_check and disk_check


	def cores_left(self, job):
		return self.get_cores() - job.get_cores()