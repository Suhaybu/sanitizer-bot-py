import asyncio

from interactions import (
	AllowedMentions,
	Embed,
	Extension,
	Member,
	OptionType,
	SlashContext,
	integration_types,
	listen,
	slash_command,
	slash_option,
)
from interactions.api.events import MessageCreate

from socialmedia_handlers.instagram import Instagram
from socialmedia_handlers.tiktok import Tiktok
from socialmedia_handlers.twitter import Twitter


class Sanitize(Extension):
	def __init__(self, bot) -> None:
		self.instagram = Instagram()
		self.tiktok = Tiktok()
		self.twitter = Twitter()

	async def sanitize(self, user_input: str) -> str | None:
		instagram_response = self.instagram.get_response(user_input)
		tiktok_response = self.tiktok.get_response(user_input)
		twitter_response = self.twitter.get_response(user_input)

		instagram_result, tiktok_result, twitter_result = await asyncio.gather(
			instagram_response, tiktok_response, twitter_response
		)
		return instagram_result or tiktok_result or twitter_result

	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		try:
			bot_response = await self.sanitize(user_input=event.message.content)

			if not bot_response:
				return

			await event.message.add_reaction("<:Sanitized:1206376642042138724>")
			await event.message.reply(bot_response, allowed_mentions={"parse": []})
			if isinstance(event.message.author, Member):
				await event.message.suppress_embeds()

		except Exception:
			return

	@slash_command(name="sanitize", description="Fix the embed of your link! 🫧")
	@slash_option(
		name="link",
		description="Your link that you want to Sanitize",
		opt_type=OptionType.STRING,
		required=True,
	)
	@integration_types(guild=True, user=True)
	async def slashSanitize(self, ctx: SlashContext, link: str):
		try:
			bot_response = await self.sanitize(user_input=link)

			if not bot_response:
				bot_response = (
					"I couldn't find a supported URL in the message you asked me to sanitize.\n"
					"To learn more about me and what I can do, try `/credits`! "
				)
				await ctx.send(
					embed=Embed(
						title="Sorry :c", description=bot_response, color="#d1001f"
					),
					ephemeral=True,
				)
				return

			await ctx.send(bot_response, allowed_mentions=AllowedMentions.none())

		except Exception:
			return
