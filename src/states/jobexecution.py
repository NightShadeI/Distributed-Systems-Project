from states import state
from job import Job
from server import Server

class JobExecutionState(state.State):

	def __init__(self, client):
		super().__init__(client)


	def receive_ok(self):
		self.client.s.send("REDY".encode())


	def receive_none(self):
		self.client.s.send("QUIT".encode())
		self.client.setState(self.client.getQuitState())


	def request_servers(self):
		servers = []
		self.client.s.send(' '.join(["RESC", "Capable", required_cores, required_memory, required_disk]).encode())
		data = self.client.s.recv(1024).decode()
		while data != ".":
			if(data != "DATA"):
				servers.append(Server(data))
			self.client.s.send("OK".encode())
			data = self.client.s.recv(1024).decode()
		return servers


	def handle_job_request(self, job):

		# Get job information
		current_job = Job(job)
		job_id = current_job.get_id()
		required_cores = current_job.get_cores()
		required_memory = current_job.get_memory()
		required_disk = current_job.get_disk()
		
		# Get server to run job on
		servers = self.request_servers()
		executing_server = self.client.getServer(servers, current_job)

		# send this server
		dataSend = " ".join(["SCHD", job_id, executing_server.get_name(), executing_server.get_id()])
		self.client.s.send(dataSend.encode())

