import re


class Twitter:
	def __init__(self) -> None:
		self.twitter_regex = re.compile(
			r"https?:\/\/(?:www\.)?twitter\.com\/(\w+)(\/status\/\S*)",
			re.IGNORECASE | re.MULTILINE,
		)
		self.x_regex = re.compile(
			r"https?:\/\/(?:www\.)?x\.com\/(\w+)(\/status\/\S*)",
			re.IGNORECASE | re.MULTILINE,
		)

	async def get_response(self, user_input: str) -> str | None:
		try:
			match = re.search(self.x_regex, user_input)
			service = "X (Twitter)"
			fixup_url = "https://fixupx.com"

			if not match:
				match = re.search(self.twitter_regex, user_input)
				service = "Twitter"
				fixup_url = "https://fxtwitter.com"

			if match:
				tweet_author, link_data = match.groups()
				return f"[@{tweet_author} via {service}]({fixup_url}{link_data})"

		except Exception as e:
			print(f"Unexpected Error in Twitter bot response: {e}")
