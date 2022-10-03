import discord
import asyncio
import config
from cogs.rng import rng
from discord.ext import commands
from discord import app_commands
import os
#color=0x2699C6


intents = discord.Intents.all()
intents.message_content = True
intents.auto_moderation_configuration = True
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}")
    

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'FOUND: `{filename}`')
            
async def main():
    await load()
    await bot.start(config.token)

asyncio.run(main())