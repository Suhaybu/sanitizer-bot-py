import re

from discord.ext import commands


class Twitter(commands.Cog):
	def __init__(self, bot: commands.bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		twitter_regex = r'https?:\/\/(?:www\.)?twitter\.com\/(\w+)(\/status\/\S*)'
		x_regex = r'https?:\/\/(?:www\.)?x\.com\/(\w+)(\/status\/\S*)'

		match = re.search(twitter_regex, message.content)
		service = 'Twitter'
		fixup_url = 'https://fxtwitter.com'

		if not match:
			match = re.search(x_regex, message.content)
			service = 'X (Twitter)'
			fixup_url = 'https://fixupx.com'

		if match:
			tweet_author, link_data = match.groups()
			response = f'[@{tweet_author}, via {service}]({fixup_url}{link_data})'

			await message.reply(response, mention_author=False)
			await message.edit(suppress=True)


async def setup(bot):
	await bot.add_cog(Twitter(bot))
