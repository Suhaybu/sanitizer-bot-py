# import re
# from typing import Optional, Tuple

# from interactions import AllowedMentions, Extension, Member, listen
# from interactions.api.events import MessageCreate


# class Youtube(Extension):
# 	def __init__(self, bot) -> None:
# 		self.youtube_regex = re.compile(
# 			r"https?://(?:www\.)?youtu(?:be.com|\.be)/((?:watch\?v=)?(?:[a-zA-Z0-9_-]+))(?:(?:\S+)?\&t=(\d+))?",
# 			re.IGNORECASE,
# 		)
# 		self.youtube_music_regex = re.compile(
# 			r"https?://music\.youtube\.com/((?:watch\?v=)?(?:[a-zA-Z0-9_-]+))(?:(?:\S+)?\&t=(\d+))?",
# 			re.IGNORECASE,
# 		)

# 	def get_youtube_response(self, user_input: str) -> Optional[Tuple[str, bool]]:
# 		try:
# 			match = re.search(self.youtube_regex, user_input)

# 			if match:
# 				service: str = "Video via YouTube"
# 			else:
# 				match = re.search(self.youtube_music_regex, user_input)
# 				if match:
# 					service: str = "Music via YouTube"
# 				else:
# 					return  # End the program, no match
# 			link_data = match.group(1)
# 			if link_data.lower() == "shorts":
# 				return  # End the program, shorts are currently not supported

# 			try:
# 				has_time_stamp = bool(match.group(2))
# 			except IndexError:
# 				has_time_stamp = False

# 			return (
# 				f"[{service}](https://yt.cdn.13373333.one/{link_data})",
# 				has_time_stamp,
# 			)

# 		except Exception as e:
# 			print(f"Unexpected Error in YouTube bot response: {e}")

# 	@listen(event_name=MessageCreate)
# 	async def on_message(self, event: MessageCreate):
# 		try:
# 			response = self.get_youtube_response(event.message.content)

# 			if not response:
# 				return

# 			bot_response, has_time_stamp = response

# 			await event.message.add_reaction("<:Sanitized:1206376642042138724>")
# 			await event.message.reply(
# 				bot_response, allowed_mentions=AllowedMentions.none()
# 			)
# 			# if not has_time_stamp and isinstance(event.message.author, Member):
# 			# 	await event.message.suppress_embeds()

# 		except Exception:
# 			return
