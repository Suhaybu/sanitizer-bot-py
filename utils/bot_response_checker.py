import asyncio
from typing import List

from interactions import Embed, Message

from models.enums.service import Service


class BotResponseChecker:
	@staticmethod
	def _check_response(message_embed: List[Embed] | None, service: Service) -> bool:
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

	async def handle(
		self, ctx, bot_message: Message, service_enum: Service, is_reply: bool = False
	):
		for _ in range(10):
			await asyncio.sleep(1)
			if bot_message.embeds:
				break

		is_valid_response = self._check_response(bot_message.embeds, service_enum)

		if is_valid_response and is_reply:
			await ctx.message.suppress_embeds()

		if not is_valid_response:
			await bot_message.delete()
			response_body = (
				"Something went wrong. The service I rely on for fixing \n"
				f"{service_enum.value} links was not able to fix your link."
			)
			response_embed = Embed(
				title="Sorry   ꒰ ꒡⌓꒡꒱", description=response_body, color="#d1001f"
			)

			if is_reply:
				await ctx.message.remove_reaction("<:Sanitized:1206376642042138724>")
				error_message = await ctx.message.reply(
					embed=response_embed, allowed_mentions={"parse": []}
				)
				await asyncio.sleep(10)
				await error_message.delete()
			else:
				await ctx.send(embed=response_embed, ephemeral=True)
