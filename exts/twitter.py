import re

from interactions import AllowedMentions, Extension, Member, listen
from interactions.api.events import MessageCreate


class Twitter(Extension):
	def __init__(self, bot) -> None:
		self.twitter_regex = re.compile(
			r'https?:\/\/(?:www\.)?twitter\.com\/(\w+)(\/status\/\S*)',
			re.IGNORECASE | re.MULTILINE,
		)
		self.x_regex = re.compile(
			r'https?:\/\/(?:www\.)?x\.com\/(\w+)(\/status\/\S*)',
			re.IGNORECASE | re.MULTILINE,
		)

	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		match = re.search(self.twitter_regex, event.message.content)
		service = 'Twitter'
		fixup_url = 'https://fxtwitter.com'

		if not match:
			match = re.search(self.x_regex, event.message.content)
			service = 'X (Twitter)'
			fixup_url = 'https://fixupx.com'

		if match:
			tweet_author, link_data = match.groups()
			bot_response = f'[@{tweet_author} via {service}]({fixup_url}{link_data})'

			await event.message.add_reaction('<:Sanitized:1206376642042138724>')
			await event.message.reply(
				bot_response, allowed_mentions=AllowedMentions.none()
			)
			if isinstance(event.message.author, Member):
				await event.message.suppress_embeds()
