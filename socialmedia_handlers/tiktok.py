import os
import re

import aiohttp
import requests

from main import get_quick_vids_token


class Tiktok:
	def __init__(self) -> None:
		self.tiktok_regex = re.compile(
			r"https?://(?:\w{1,3}\.)?tiktok\.com/[^\/]+\/?\S*",
			re.IGNORECASE,
		)
		self.token = get_quick_vids_token()

	async def get_api_response(
		self, input_text: str, detailed: bool = False
	) -> dict | None:
		url = "https://api.quickvids.app/v2/quickvids/shorturl"
		headers = {
			"Content-Type": "application/json",
			"Authorization": f"Bearer {self.token}",
		}
		data = {"input_text": input_text, "detailed": detailed}

		async with aiohttp.ClientSession() as session:
			async with session.post(url, json=data, headers=headers) as response:
				if response.status == 500:
					data["detailed"] = False
					async with session.post(
						url, json=data, headers=headers
					) as retry_response:
						response = retry_response

				if response.status == 200:
					return await response.json()

				print(f"Error creating short URL: {response.text}")
				return None

	async def get_response(self, user_input: str) -> str | None:
		try:
			match = re.search(self.tiktok_regex, user_input)
			if match:
				api_response = await self.get_api_response(match.group(), detailed=True)
				if api_response is None:
					raise RuntimeError("No API response")
				quickvids_url = api_response["quickvids_url"]
				if api_response["details"] is not None:
					author_username = api_response["details"]["author"]["username"]
					return f"[@{author_username} via TikTok]({quickvids_url})"
				else:
					return f"[via TikTok]({quickvids_url})"
		except RuntimeError as e:
			print(f"RuntimeError in TikTok API bot response: {e}")
		except Exception as e:
			print(f"Unexpected Error in TikTok bot response: {e}")
