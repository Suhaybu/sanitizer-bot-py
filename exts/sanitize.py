import asyncio

from interactions import (AllowedMentions, ContextMenuContext, Embed,
                          Extension, Message, OptionType, SlashContext,
                          integration_types, listen, message_context_menu,
                          slash_command, slash_option)
from interactions.api.events import MessageCreate

from models.enums.service import Service, ServiceResponse
from socialmedia_handlers.instagram import Instagram
from socialmedia_handlers.tiktok import Tiktok
from socialmedia_handlers.twitter import Twitter
from utils.bot_response_checker import BotResponseChecker


class Sanitize(Extension):
	def __init__(self, bot) -> None:
		self.instagram = Instagram()
		self.tiktok = Tiktok()
		self.twitter = Twitter()
		self.response_checker = BotResponseChecker()

	async def sanitize(self, user_input: str) -> ServiceResponse | None:
		instagram_response = self.instagram.get_response(user_input)
		tiktok_response = self.tiktok.get_response(user_input)
		twitter_response = self.twitter.get_response(user_input)

		instagram_result, tiktok_result, twitter_result = await asyncio.gather(
			instagram_response, tiktok_response, twitter_response
		)

		if instagram_result:
			return ServiceResponse(Service.INSTAGRAM, instagram_result)
		elif tiktok_result:
			return ServiceResponse(Service.TIKTOK, tiktok_result)
		elif twitter_result:
			return ServiceResponse(Service.TWITTER, twitter_result)
		else:
			return None

	# Listener for automatically responding to valid messages
	@listen(event_name=MessageCreate)
	async def on_message(self, event: MessageCreate):
		try:
			response = await self.sanitize(user_input=event.message.content)

			if not response:
				return

			await event.message.add_reaction("<:Sanitized:1206376642042138724>")
			bot_message = await event.message.reply(
				response.content, allowed_mentions={"parse": []}
			)

			await self.response_checker.handle(
				event, bot_message, response.service, True
			)

		except Exception:
			return

	# Slash command
	@slash_command(name="sanitize", description="Fix the embed of your link! 🫧")
	@slash_option(
		name="link",
		description="Your link that you want to Sanitize",
		opt_type=OptionType.STRING,
		required=True,
	)
	@integration_types(guild=True, user=True)
	async def slash_sanitize(self, ctx: SlashContext, link: str):
		try:
			response = await self.sanitize(user_input=link)

			if not response:
				response = (
					"I couldn't find a supported URL in the message you asked me to sanitize.\n"
					"To learn more about me and what I can do, try `/credits`! "
				)
				await ctx.send(
					embed=Embed(
						title="Sorry :c", description=response, color="#d1001f"
					),
					ephemeral=True,
				)
				return

			bot_message = await ctx.send(
				response.content, allowed_mentions=AllowedMentions.none()
			)

			await self.response_checker.handle(ctx, bot_message, response.service)

		except Exception:
			return

	# Context Menu command
	@message_context_menu(name="Sanitize")
	@integration_types(guild=True, user=True)
	async def context_sanitize(self, ctx: ContextMenuContext):
		message = ctx.target
		if not isinstance(message, Message):
			return

		try:
			response = await self.sanitize(user_input=message.content)

			if not response:
				response = (
					"I couldn't find a supported URL in the message you asked me to sanitize.\n"
					"To learn more about me and what I can do, try `/credits`! "
				)
				await ctx.send(
					embed=Embed(
						title="Sorry :c", description=response, color="#d1001f"
					),
					ephemeral=True,
				)
				return

			bot_message = await ctx.send(
				response.content, allowed_mentions=AllowedMentions.none()
			)

			await self.response_checker.handle(ctx, bot_message, response.service)

		except Exception:
			return
