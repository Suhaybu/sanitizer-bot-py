from discord.ext import commands


class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


async def setup(bot):
	await bot.add_cog(General(bot))
