import re

from models.enums.service import Service
from utils.quickvids_handler import QuickvidsHandler


class Tiktok:
	def __init__(self) -> None:
		self.tiktok_regex = re.compile(
			r"https?://(?:\w{1,3}\.)?tiktok\.com/[^\/]+\/?\S*",
			re.IGNORECASE,
		)
		self.api = QuickvidsHandler()

	async def get_response(self, user_input: str) -> str | None:
		try:
			match = re.search(self.tiktok_regex, user_input)
			if match:
				return await self.api.get_response(match, Service.TIKTOK)
		except RuntimeError as e:
			print(f"RuntimeError in TikTok API bot response: {e}")
		except Exception as e:
			print(f"Unexpected Error in TikTok bot response: {e}")
