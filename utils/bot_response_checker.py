from typing import List

from interactions import Embed

from models.enums.service import Service


class BotResponseChecker:
	@staticmethod
	def is_response_valid(message_embed: List[Embed] | None, service: Service) -> bool:
		if service == Service.TWITTER:
			if not message_embed:
				return False
			if message_embed[0].title == "FxTwitter / FixupX":
				return False
		elif service == Service.INSTAGRAM:
			if not message_embed:
				return False
			if message_embed[0].title == "InstaFix":
				return False

		return True
