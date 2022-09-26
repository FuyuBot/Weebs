import discord
from discord import app_commands
from discord.ext import commands
import requests

class rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `rules.py`')

async def setup(bot):
    await bot.add_cog(rules(bot), guilds=[discord.Object(id=860752406551461909)])