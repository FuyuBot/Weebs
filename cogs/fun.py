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
    
    @app_commands.command(name="bot-info", description="Displays information about the bot.")
    async def botInfo(self, interaction: discord.Interaction):
        try:
            client = interaction.client
            embed = discord.Embed(color=config.color, title=f"{client.user}'s Information", description=f"\
                Bot's Creators: Jzcob#2842, Sezn#6554, and SpaceZ#4346\n\
                Questions Commands: https://docs.truthordarebot.xyz/api-docs\n\
                Cat Command: https://developers.thecatapi.com/\n\
                Dog Command: https://dog.ceo/dog-api/\n\
                Duck Command: https://random-d.uk/api\n\
                Fox Command: https://randomfox.ca/\n\
                Lucifer Command: https://lucifer-quotes.vercel.app/\n\
                Anime Commands: https://otakugifs.xyz/api\n\
                Weather Command: https://openweathermap.org/\n\n\
                Bot is coded in `Python` v3.11 and using `discord.py` v2.1.0")
            embed.set_thumbnail(url=client.user.avatar)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)
    
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
