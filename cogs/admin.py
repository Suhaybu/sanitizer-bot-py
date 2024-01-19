import discord
from discord import app_commands
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # $sync: sync slash commands (Prefix)
    @commands.command(
        name='sync',
        aliases=['Sync'],
        description='Requests all slash commands to sync.',
    )
    @commands.is_owner()
    async def sync(self, ctx):
        print(
            f'User {ctx.author.name} ({ctx.author.id}) used Prefix Sync command'
        )
        synced = await self.bot.tree.sync()

        if not synced:
            print(
                'No commands were synced. Please make sure the cogs are loaded.'
            )
        else:
            print(f'Successfully synced {synced} command(s)')

    # /sync: sync slash commands
    # @app_commands.command(
    #     name='sync', description='Requests all slash commands to sync.'
    # )
    # @app_commands.checks.is_owner()
    # async def ssync(self, interaction: discord.Interaction):
    #     ...


async def setup(bot):
    await bot.add_cog(Admin(bot))
