import discord
import asyncio
import config
from discord.ext import commands
from discord import app_commands
import os



intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.auto_moderation_configuration = True
intents.reactions = True
bot = commands.Bot(command_prefix='.', intents=intents)
status = discord.Status.online



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
    game = discord.Game("A Weeb's Hangout")
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="A Weeb's Hangout"))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="A Weeb's Hangout"))
    await bot.start(config.token)

asyncio.run(main())