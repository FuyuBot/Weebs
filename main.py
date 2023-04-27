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

@bot.command()
async def sync(ctx) -> None:
    if ctx.author.id == 920797181034778655 or ctx.author.id == 155580061888675840:
        try:
            fmt = await ctx.bot.tree.sync()
            print(f"Synced {len(fmt)} commands.")
            return
        except Exception as e:
            print(e)
    else:
        print("Failed: not sean or jacob.")

@bot.command()
async def syncweebs(ctx) -> None:
    if ctx.author.id == 920797181034778655 or ctx.author.id == 155580061888675840:
        try:
            fmt = await ctx.bot.tree.sync(guild=ctx.guild)
            print(f"Synced {len(fmt)} commands.")
            return
        except Exception as e:
            print(e)
    else:
        print("Failed: not sean or jacob.")


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