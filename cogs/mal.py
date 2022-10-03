import discord
from discord import app_commands
from discord.ext import commands
import json
import requests
from jikanpy import Jikan
jikan = Jikan()


class mal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `mal.py`")
    
#    @app_commands.command(name='anime', description='Search an anime from MAL.')
#    async def anime(self, interaction: discord.Interaction, anime: str):
#        try:
#            search_result = jikan.search('anime', f'{anime}')
#            result = json.loads(f'{search_result}')
#            print(result)
#            await interaction.response.send_message("Check the terminal")
#       except Exception as e:
#           print(e)

async def setup(bot):
    await bot.add_cog(mal(bot), guilds=[discord.Object(id=860752406551461909)])