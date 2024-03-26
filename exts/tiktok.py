import re
from interactions import AllowedMentions, Extension, listen, Message
from interactions.api.events import MessageCreate

from utils.quickvids_api import create_short_url


class Tiktok(Extension):
	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		tiktok_regex = re.compile(
			r'https?:\/\/.*tiktok\.com\/.*',
			re.IGNORECASE | re.MULTILINE,
		)
		match = re.search(tiktok_regex, event.message.content)

		if match:
			api_response = create_short_url(match.group().lower(), detailed=True)

			quickvids_url = api_response['quickvids_url']
			author_username = api_response['details']['author']['username']
			bot_response = f'[@{author_username} via TikTok]({quickvids_url})'

			await event.message.add_reaction('<:Sanitized:1206376642042138724>')
			await event.message.reply(
				bot_response, allowed_mentions=AllowedMentions.none()
			)
			await event.message.suppress_embeds()
