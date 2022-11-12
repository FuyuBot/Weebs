import discord
from discord import app_commands
from discord.ext import commands
import requests
import json
import config

#https://some-random-api.ml/endpoints


class animals(commands.Cog):
    def __init__(self, bot: commands.Bot): 
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"LOADED: `animals.py`")

    @app_commands.command(name='cat', description="Send a random picture of a cat.")
    async def cat(self, interaction: discord.Interaction):
        catUrl = 'https://api.thecatapi.com/v1/images/search'
        catGet = requests.get(catUrl)
        json_data = json.loads(catGet.text)
        for x in json_data:
            catPicture = x['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=catPicture)
        embed.set_footer(text=config.footer)
        print(interaction.user.get_role(860758013731274762))
        await interaction.response.send_message(f"{interaction.user.mention} here is your cat picture.", embed=embed)

    @app_commands.command(name='dog', description="Send a random picture of a dog.")
    async def dog(self, interaction: discord.Interaction):
        dogUrl = 'https://dog.ceo/api/breeds/image/random'
        dogGet = requests.get(dogUrl)
        dogPicture = dogGet.json()['message']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=dogPicture)
        embed.set_footer(text=config.footer)
        await interaction.response.send_message(f"{interaction.user.mention} here is your dog picture.", embed=embed)


async def setup(bot):
    await bot.add_cog(animals(bot))