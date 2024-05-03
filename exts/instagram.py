import re
from typing import Optional

from interactions import AllowedMentions, Extension, Member, listen
from interactions.api.events import MessageCreate


class Instagram(Extension):
	def __init__(self, bot) -> None:
		self.instagram_regex = re.compile(
			r'https?:\/\/(?:www\.)?instagram\.com/(reel|p)/([^/\s?]+)',
			re.IGNORECASE | re.MULTILINE,
		)

	def get_instagram_response(self, user_input: str) -> Optional[str]:
		try:
			match = re.search(self.instagram_regex, user_input)
			if match:
				type, url_data = match.groups()
				if type == 'reel':
					type_printed = 'Reel'
				elif type == 'p':
					type_printed = 'Post'
				else:
					raise ValueError('Invalid link type')

				return f'[{type_printed} via Instagram](https://g.ddinstagram.com/{type}/{url_data}/)'
		except ValueError as e:
			print(f'ValueError in Instagrams bot response: {e}')
		except Exception as e:
			print(f'Unexpected Error in Instagrams bot response: {e}')

	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		try:
			bot_response = self.get_instagram_response(event.message.content)

			if not bot_response:
				return

			await event.message.add_reaction('<:Sanitized:1206376642042138724>')
			await event.message.reply(
				bot_response, allowed_mentions=AllowedMentions.none()
			)
			if isinstance(event.message.author, Member):
				await event.message.suppress_embeds()

		except Exception:
			return
