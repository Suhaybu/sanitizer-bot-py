from discord.ext import commands


class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.hybrid_command(name='credits', description='Roll the credits!')
	async def credits(self, ctx):
		if ctx.author == self.bot.user:
			return

		with open('credits.md', 'r', encoding='utf-8') as file:
			bot_response = file.read()

		await ctx.reply(bot_response, ephemeral=True)


async def setup(bot):
	await bot.add_cog(General(bot))
