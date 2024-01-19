import asyncio
import os

import discord
from discord.ext import commands

from settings import BOT_TOKEN
from utils.cogs_loader import print_cog_status

intents = discord.Intents.default()
discord.Intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), intents=intents
)


async def load_cogs():
    loaded_cogs = []
    faulty_cogs = []

    for cog_name in os.listdir('./cogs'):
        if cog_name.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{cog_name[:-3]}')
                loaded_cogs.append(cog_name[-3])
            except Exception as e:
                faulty_cogs.append(cog_name[:-3])

    print_cog_status(loaded_cogs, faulty_cogs)


async def main():
    async with bot:
        print('(1/2) Starting the bot and loading cogs')
        await load_cogs()
        await bot.start(BOT_TOKEN)


@bot.event
async def on_ready():
    print(
        f'(2/2) Sanitizer Bot is Online! Discord version: {discord.__version__}'
    )
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=f"to !help",
        )
    )


asyncio.run(main())
