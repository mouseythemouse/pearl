import asyncio
import hangups
import os

from interactive import Interactive

class Dog(Interactive):

	def __init__(self, pearl):
		self.pearl = pearl

	def handle(self, args, event):
		dog = os.path.join('plugins','220px-Shiba_inu_taiki.jpg')
		asyncio.run_coroutine_threadsafe(self.sendImage(self.conversation(event=event),dog), self.pearl.loop)
def initialize(pearl):
	return Dog(pearl)
