from states import state
import sys

class QuitState(state.State):

	def __init__(self, client):
		super().__init__(client)


	def receive_quit(self):
		self.client.closeSocket()
		sys.exit(0)