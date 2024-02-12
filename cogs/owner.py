from discord.ext import commands


class Owner(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	# Prefix: sync slash commands (Prefix)
	@commands.command(
		name='sync',
		aliases=['Sync'],
		description='Requests all slash commands to sync.',
	)
	@commands.is_owner()
	async def sync(self, ctx):
		print(f'User {ctx.author.name} ({ctx.author.id}) used Prefix Sync command')
		synced = await self.bot.tree.sync()

		if not synced:
			message = 'No commands were synced. Please make sure the cogs were correctly loaded.'
		else:
			message = f"Successfully synced {len(synced)} command's."
			if len(synced) == 1:
				message = message[:-3] + '.'

		await ctx.message.reply(message)
		print(message)


async def setup(bot):
	await bot.add_cog(Owner(bot))
