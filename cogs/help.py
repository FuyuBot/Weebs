import discord
from discord import app_commands
from discord.ext import commands
import config

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `help.py`")
    
    @app_commands.command(name="help", )
    async def help(self, interaction: discord.Interaction, category: str):
        return

async def setup(bot):
    await bot.add_cog(help(bot), guilds=[discord.Object(id=config.weebsHangout)])