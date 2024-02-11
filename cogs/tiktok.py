import re

from discord.ext import commands

from utils.quickvids_api import create_short_url


class Tiktok(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		tiktok_regex = r'https?:\/\/.*tiktok\.com\/.*'
		match = re.search(tiktok_regex, message.content)

		if match:
			api_response = create_short_url(match.group(), detailed=True)

			quickvids_url = api_response['quickvids_url']
			author_username = api_response['details']['author']['username']
			bot_response = f'[@{author_username} via TikTok]({quickvids_url})'

			await message.reply(bot_response, mention_author=False)
			await message.edit(suppress=True)


async def setup(bot):
	await bot.add_cog(Tiktok(bot))
