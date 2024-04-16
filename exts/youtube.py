import re

from interactions import AllowedMentions, Extension, Member, listen
from interactions.api.events import MessageCreate


class Youtube(Extension):
	def __init__(self, bot) -> None:
		self.youtube_regex = re.compile(
			r'https?://(?:www\.)?youtu(?:be.com|\.be)/((?:watch\?v=)?(?:[a-zA-Z0-9_-]+))(?:(?:\S+)?\&t=(\d+))?',
			re.IGNORECASE,
		)
		youtube_music_regex = re.compile(
			r'https?://music\.youtube\.com/((?:watch\?v=)?(?:[a-zA-Z0-9_-]+))(?:(?:\S+)?\&t=(\d+))?',
			re.IGNORECASE,
		)
		self.youtube_music_regex = re.compile(
			r'https?://music\.youtube\.com/((?:watch\?v=)?(?:[a-zA-Z0-9_-]+))(?:(?:\S+)?\&t=(\d+))?',
			re.IGNORECASE,
		)

	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		match = re.search(self.youtube_regex, event.message.content)

		if match:
			service: str = 'Video via YouTube'
		else:
			match = re.search(self.youtube_music_regex, event.message.content)
			if match:
				service: str = 'Music via YouTube'
			else:
				return  # End the program, no match
		link_data = match.group(1)
		if link_data.lower() == 'shorts':
			return  # End the program, shorts are currently not supported

		try:
			has_time_stamp = bool(match.group(2))
		except IndexError:
			has_time_stamp = False

		bot_response = f'[{service}](https://yt.cdn.13373333.one/{link_data})'

		await event.message.add_reaction('<:Sanitized:1206376642042138724>')
		await event.message.reply(bot_response, allowed_mentions=AllowedMentions.none())
		if has_time_stamp is False & isinstance(event.message.author, Member):
			await event.message.suppress_embeds()
