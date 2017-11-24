import asyncio
import hangups

from command import Command

class Dog(Command):

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client

	def handle(self, args, event):
		dog = "pearl/plugins/220px-Shiba_inu_taiki.jpg"
		
		asyncio.run_coroutine_threadsafe(self.sendImage(dog, event.conversation_id.id), self.pearl.loop)

def initialize(pearl):
	return Dog(pearl)
