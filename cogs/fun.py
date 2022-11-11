import discord
from discord import app_commands
from discord.ext import commands
import requests
import json
import config

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `fun.py`')
    
    @app_commands.command(name="lucifer-quote", description="Sends a quote from the show Lucifer.")
    async def lucifer(self, interaction: discord.Interaction):
        url = "https://lucifer-quotes.vercel.app/api/quotes"
        response = requests.get(url)
        json_data = json.loads(response.text)
        for x in json_data:
            quote = x['quote']
            author = x['author']
        
        embed = discord.Embed(title=author,description=quote,color=config.color)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(fun(bot))
