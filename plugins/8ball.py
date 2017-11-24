

import random
import asyncio

import hangups

class Ball:

	def __init__(self, client):
		self.client = client

	@asyncio.coroutine
	def handle(self, pearl, args, event):
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Error: 404 not found", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "0% chance"]
    ball = random.choice(responses)

		
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
					hangups.ChatMessageSegment(ball).serialize()
				],
			),
		)
		yield from self.client.send_chat_message(request)

def initialize(client):
	return Ball(client)
