import re

import aiohttp

from models.enums.service import Service
from models.errors import APIError, NoAPIResponseError
from utils.quickvids_handler import QuickvidsHandler


class Instagram:
	def __init__(self) -> None:
		self.instagram_regex = re.compile(
			r"https?:\/\/(?:www\.)?instagram\.com/(reel|p)/([^/\s?]+)",
			re.IGNORECASE | re.MULTILINE,
		)
		self.api = QuickvidsHandler()

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

				try:
					return await self.api.get_response(match, Service.INSTAGRAM)
				except (NoAPIResponseError, APIError, aiohttp.ClientError):
					return f"[{type_printed} via Instagram](https://g.ddinstagram.com/{type}/{url_data}/)"
		except ValueError as e:
			print(f"ValueError in Instagram bot response: {e}")
		except Exception as e:
			print(f"Unexpected Error in Instagram bot response: {e}")
