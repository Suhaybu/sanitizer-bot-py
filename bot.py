import asyncio
import os

import discord
from discord.ext import commands

from settings import BOT_TOKEN

intents = discord.Intents.default()
discord.Intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), intents=intents
)


async def load_cogs():
    for cog_name in os.listdir('./cogs'):
        if cog_name.endswith('.py'):
            await bot.load_extension()


async def main():
    async with bot:
        await bot.start(BOT_TOKEN)


@bot.event
async def on_ready():
    print('Sanitizer Bot is Online!')
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"!help",
        )
    )
    print(discord.__version__)


asyncio.run(main())
