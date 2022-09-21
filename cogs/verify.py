import discord
from discord import app_commands
from discord.ext import commands

class verfiy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `verify.py`")

    @app_commands.command(name='verify', description='Verify that you are a human.')
    async def verify(self, interaction:discord.Interaction):
        return

async def setup(bot):
    await bot.add_cog(verfiy(bot))