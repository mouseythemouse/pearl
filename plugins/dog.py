import asyncio
import hangups

from command import Command

class Dog(Command):

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client

	def handle(self, args, event):
		dog = self.client.upload_image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Shiba_inu_taiki.jpg/220px-Shiba_inu_taiki.jpg")
		
		asyncio.run_coroutine_threadsafe(self.send(dog, event.conversation_id.id), self.pearl.loop)

def initialize(pearl):
	return Dog(pearl)
