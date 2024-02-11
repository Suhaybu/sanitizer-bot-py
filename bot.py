"""
This is the main file where the bot starts from.
"""

import asyncio
import os

import discord
from discord.ext import commands

from settings import BOT_TOKEN
from utils.print_cog_status import print_cog_status
from utils.setup_logger import setup_logger

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!!'), intents=intents)

logger = setup_logger()


async def load_cogs():
	loaded_cogs = []
	faulty_cogs = []

	for cog_name in os.listdir('./cogs'):
		if cog_name.endswith('.py'):
			try:
				await bot.load_extension(f'cogs.{cog_name[:-3]}')
				loaded_cogs.append(cog_name[:-3])
			except Exception:
				faulty_cogs.append(cog_name[:-3])

	print_cog_status(loaded_cogs, faulty_cogs)


async def main():
	async with bot:
		print('#--------  Bot is starting up and loading cogs...  ----------#')
		await load_cogs()
		await bot.start(BOT_TOKEN)


@bot.event
async def on_ready():
	await bot.change_presence(
		activity=discord.Activity(
			type=discord.ActivityType.listening,
			name='!!help',
		)
	)

	print('#----------        Sanitizer Bot is Online!        ----------#')


asyncio.run(main())
