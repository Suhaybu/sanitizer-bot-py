import re

from discord.ext import commands


class Instagram(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		instagram_regex = r'https?:\/\/(?:www\.)?instagram\.com/(reel|p)/([^?]+)'
		match = re.search(instagram_regex, message.content)

		if match:
			type, url_data = match.groups()
			if type == 'reel':
				type_printed = 'Reel'
			elif type == 'p':
				type_printed = 'Post'

			response = f'[{type_printed} via Instagram](https://www.instagramez.com/{type}/{url_data})'

			await message.reply(response, mention_author=False)
			await message.edit(suppress=True)


async def setup(bot):
	await bot.add_cog(Instagram(bot))
