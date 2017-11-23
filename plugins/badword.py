import asyncio

import hangups

class BadWord:

	def __init__(self, client):
		self.client = client

	@asyncio.coroutine
	def handle(self, pearl, args, event):
		badword = 'No thanks'
		
		request = hangups.hangouts_pb2.SendChatMessageRequest(
			request_header=self.client.get_request_header(),
			event_request_header=hangups.hangouts_pb2.EventRequestHeader(
				conversation_id=hangups.hangouts_pb2.ConversationId(
					id=event.conversation_id.id
				),
				client_generated_id=self.client.get_client_generated_id(),
			),
			message_content=hangups.hangouts_pb2.MessageContent(
				segment=[
					hangups.ChatMessageSegment(badword).serialize()
				],
			),
		)
		yield from self.client.send_chat_message(request)

def initialize(client):
	return BadWord(client)
