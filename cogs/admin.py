import discord
from discord import app_commands
from discord.ext import commands


class Admin(commands.Cog):
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

	# TODO: Need to convert both sync commands into a hybrid command
	# /sync: sync slash commands
	@app_commands.command(
		name='sync', description='Requests all slash commands to sync.'
	)
	# TODO: Make it exclusive for the Owner
	# @app_commands.is_owner()
	async def ssync(self, interaction: discord.Interaction):
		print(
			f'User {interaction.user.name} ({interaction.user.id}) used /sync command'
		)
		synced = await self.bot.tree.sync()

		if not synced:
			message = 'No commands were synced. Please make sure the cogs were correctly loaded.'
		else:
			message = f"Successfully synced {len(synced)} command's."
			if len(synced) == 1:
				message = message[:-3] + '.'

		await interaction.response.send_message(message, ephemeral=True)
		print(message)


async def setup(bot):
	await bot.add_cog(Admin(bot))
