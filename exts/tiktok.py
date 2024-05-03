import re
from typing import Optional

import requests
from interactions import AllowedMentions, Extension, Member, SlashContext, listen
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

	def get_tiktok_response(self, user_input: str) -> Optional[str]:
		try:
			match = re.search(self.tiktok_regex, user_input)
			if match:
				api_response = self.create_short_url(match.group(), detailed=True)
				if api_response is None:
					raise RuntimeError('No API response')
				quickvids_url = api_response['quickvids_url']
				if api_response['details'] is not None:
					author_username = api_response['details']['author']['username']
					return f'[@{author_username} via TikTok]({quickvids_url})'
				else:
					return f'[via TikTok]({quickvids_url})'
		except RuntimeError as e:
			print(f'RuntimeError in TikTok API bot response: {e}')
		except Exception as e:
			print(f'Unexpected Error in TikTok bot response: {e}')

	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		try:
			bot_response = self.get_tiktok_response(event.message.content)
		except Exception:
			return

		if not bot_response:
			return

		await event.message.add_reaction('<:Sanitized:1206376642042138724>')
		await event.message.reply(bot_response, allowed_mentions=AllowedMentions.none())
		if isinstance(event.message.author, Member):
			await event.message.suppress_embeds()
