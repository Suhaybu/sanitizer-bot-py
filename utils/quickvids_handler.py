from re import Match

import aiohttp

from main import get_quick_vids_token
from models.enums.service import Service
from models.errors import APIError, NoAPIResponseError


class QuickvidsHandler:
	def __init__(self) -> None:
		self.token = get_quick_vids_token()

	async def _call_api(self, input_text: str, detailed: bool = False) -> dict | None:
		url = "https://api.quickvids.app/v2/quickvids/shorturl"
		headers = {
			"Content-Type": "application/json",
			"Authorization": f"Bearer {self.token}",
		}
		data = {"input_text": input_text, "detailed": detailed}

		async with aiohttp.ClientSession() as session:
			async with session.post(url, json=data, headers=headers) as response:
				if response.status != 200:
					data["detailed"] = False
					async with session.post(
						url, json=data, headers=headers
					) as retry_response:
						response = retry_response

				if response.status == 200:
					return await response.json()

				response_text = await response.text()
				raise APIError(response.status, response_text)

	async def get_response(
		self, matched_input: Match[str], service_type: Service
	) -> str | None:
		api_response = await self._call_api(matched_input.group(), detailed=True)
		if api_response is None:
			raise NoAPIResponseError("No API response")

		quickvids_url = api_response["quickvids_url"]
		if api_response["details"] is not None:
			author_username = api_response["details"]["author"]["username"]
			return f"[@{author_username} via {service_type.value}]({quickvids_url})"
		else:
			return f"[via {service_type.value}]({quickvids_url})"
