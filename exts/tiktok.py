import re

from interactions import AllowedMentions, Extension, Message, listen
from interactions.api.events import MessageCreate

from utils.quickvids_api import create_short_url


class Tiktok(Extension):
	def __init__(self, bot) -> None:
		self.tiktok_regex = re.compile(
			r'https?://(?:\w{1,3}\.)?tiktok\.com/[^\/]+\/?\S*',
			re.IGNORECASE,
		)

	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		match = re.search(self.tiktok_regex, event.message.content)

		if match:
			api_response = create_short_url(match.group(), detailed=True)

			quickvids_url = api_response['quickvids_url']
			author_username = api_response['details']['author']['username']
			bot_response = f'[@{author_username} via TikTok]({quickvids_url})'

			await event.message.add_reaction('<:Sanitized:1206376642042138724>')
			await event.message.reply(
				bot_response, allowed_mentions=AllowedMentions.none()
			)
			await event.message.suppress_embeds()
