from states import state

class JobExecutionState(state.State):

	def __init__(self, client):
		super().__init__(client)


	def receive_ok(self):
		self.client.s.send("REDY".encode())


	def receive_none(self):
		self.client.s.send("QUIT".encode())
		self.client.setState(self.client.getQuitState())


	def handle_job_request(self, job):
		self.client.s.send(' '.join(["RESC", "Capable", job[3], job[4], job[5]]).encode())
		servers = []
		data = self.client.s.recv(1024).decode()
		while data != ".":
			if(data != "DATA"):
				data_split = data.split()
				servers.append(data.split())
			self.client.s.send("OK".encode())
			data = self.client.s.recv(1024).decode()

		executing_server = self.client.getServer(servers, job)
		dataSend = " ".join(["SCHD", job[1], executing_server[0], executing_server[1]])
		self.client.s.send(dataSend.encode())

