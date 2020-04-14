from states import state

class JobExecutionState(state.State):

	def __init__(self, client):
		super().__init__(client)


	def receive_ok(self):
		self.client.s.send("REDY".encode())


	def receive_none(self):
		self.client.s.send("QUIT".encode())
		self.client.setState(self.client.getQuitState())


	def receive_job_request(self, params):
		executing_server = self.client.getServer()
		dataSend = " ".join(["SCHD", params[1], executing_server, "0"])
		self.client.s.send(dataSend.encode())
		