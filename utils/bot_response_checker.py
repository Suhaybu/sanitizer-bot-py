from typing import List

from interactions import Embed

from models.enums.service import Service


class BotResponseChecker:
	def is_twitter_valid(self, message_embed: List[Embed] | None) -> bool:
		if not message_embed:
			return False
		if message_embed[0].title == "FxTwitter / FixupX":
			return False
		return True

	def is_instagram_valid(self, message_embed: List[Embed] | None) -> bool:
		if not message_embed:
			return False
		if message_embed[0].title == "InstaFix":
			return False
		return True

	def is_response_valid(
		self, message_embed: List[Embed] | None, service: Service
	) -> bool:
		if service == Service.TWITTER:
			return self.is_twitter_valid(message_embed)
		elif service == Service.INSTAGRAM:
			return self.is_instagram_valid(message_embed)

		return True
