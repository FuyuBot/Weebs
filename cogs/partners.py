import discord
from discord import app_commands
from discord.ext import commands

class partners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `partners.py`')

async def setup(bot):
    await bot.add_cog(partners(bot))