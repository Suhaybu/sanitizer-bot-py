import re

from interactions import AllowedMentions, Extension, Message, listen
from interactions.api.events import MessageCreate


class Instagram(Extension):
	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		# instagram_regex = r'https?:\/\/(?:www\.)?instagram\.com/(reel|p)/([^?]+)'
		instagram_regex = re.compile(
			r'https?:\/\/(?:www\.)?instagram\.com/(reel|p)/([^/\s?]+)',
			re.IGNORECASE | re.MULTILINE,
		)

		match = re.search(instagram_regex, event.message.content)

		if match:
			type, url_data = match.groups()
			if type == 'reel':
				type_printed = 'Reel'
			elif type == 'p':
				type_printed = 'Post'

			bot_response = f'[{type_printed} via Instagram](https://www.ddinstagram.com/{type}/{url_data}/)'
			# no_reply = AllowedMentions.none()
			await event.message.add_reaction('<:Sanitized:1206376642042138724>')
			await event.message.reply(
				bot_response, allowed_mentions=AllowedMentions.none()
			)
			await event.message.suppress_embeds()
