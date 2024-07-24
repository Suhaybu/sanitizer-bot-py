import re


class Instagram:
	def __init__(self) -> None:
		self.instagram_regex = re.compile(
			r"https?:\/\/(?:www\.)?instagram\.com/(reel|p)/([^/\s?]+)",
			re.IGNORECASE | re.MULTILINE,
		)

	async def get_response(self, user_input: str) -> str | None:
		try:
			match = re.search(self.instagram_regex, user_input)
			if match:
				type, url_data = match.groups()
				if type == "reel":
					type_printed = "Reel"
				elif type == "p":
					type_printed = "Post"
				else:
					raise ValueError("Invalid link type")

				return f"[{type_printed} via Instagram](https://g.ddinstagram.com/{type}/{url_data}/)"
		except ValueError as e:
			print(f"ValueError in Instagrams bot response: {e}")
		except Exception as e:
			print(f"Unexpected Error in Instagrams bot response: {e}")
