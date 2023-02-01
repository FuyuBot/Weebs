import discord
from discord.ext import commands
from discord import app_commands
import config
import requests


class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `twitch.py`")
    
    @app_commands.command(name="twitch", description="Send an embed in the streams channel with your channel link.")
    @app_commands.checks.has_any_role("Management Team", "Senior Staff", "Staff Team")
    async def twitch(self, interaction: discord.Interaction, channel_name: str, message: str, channel_url: str):
        embed = discord.Embed(color=config.color, description=message)
        embed.set_author(name=channel_name, url=channel_url)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    bot.add_cog(twitch(bot), guilds=[discord.Object(id=860752406551461909)])