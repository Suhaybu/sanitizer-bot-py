import re

import requests
from interactions import (AllowedMentions, Extension, Member, SlashContext,
                          listen)
from interactions.api.events import MessageCreate


class Tiktok(Extension):
	def __init__(self, bot) -> None:
		self.tiktok_regex = re.compile(
			r'https?://(?:\w{1,3}\.)?tiktok\.com/[^\/]+\/?\S*',
			re.IGNORECASE,
		)

	@staticmethod
	def create_short_url(input_text: str, detailed: bool = False):
		url = 'https://api.quickvids.win/v1/shorturl/create'
		headers = {'Content-Type': 'application/json'}
		data = {'input_text': input_text, 'detailed': detailed}
		response = requests.post(url, json=data, headers=headers)

		if response.status_code == 500:
			data = {'input_text': input_text, 'detailed': False}
			response = requests.post(url, json=data, headers=headers)

		if response.status_code == 200:
			return response.json()  # Includes quickvids_url and possibly details

		print(f'Error creating short URL: {response.text}')
		return None

	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		match = re.search(self.tiktok_regex, event.message.content)

		if match:
			try:
				api_response = self.create_short_url(match.group(), detailed=True)
				if api_response is None:
					raise Exception('No API response')
				quickvids_url = api_response['quickvids_url']
				if api_response['details'] is not None:
					author_username = api_response['details']['author']['username']
					bot_response = f'[@{author_username} via TikTok]({quickvids_url})'
				else:
					bot_response = f'[via TikTok]({quickvids_url})'

				await event.message.add_reaction('<:Sanitized:1206376642042138724>')
				await event.message.reply(
					bot_response, allowed_mentions=AllowedMentions.none()
				)
				if isinstance(event.message.author, Member):
					await event.message.suppress_embeds()
			except Exception as e:
				print(f'Error processing TikTok URL: {e}')
