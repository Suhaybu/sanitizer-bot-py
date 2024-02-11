from discord.ext import commands


class Tiktok(commands.Cogs):
	def __init__(self, bot):
		self.bot = bot


async def setup(bot):
	await bot.add_cog(Tiktok(bot))
