import discord
from discord import app_commands
from discord.ext import commands
import random
import config

class coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `coinflip.py`")

    @app_commands.command(name='coinflip', description='Flip a coin')
    async def coinflip(self, interaction: discord.Interaction):
        x = random.randrange(1, 3)
        if x == 1:
            embed = discord.Embed(
                color=0x2699C6
            )
            embed.set_image(url="https://c.tenor.com/nEu74vu_sT4AAAAC/heads-coinflip.gif")
            embed.set_footer(text=config.footer)
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                color=0x2699C6
            )
            embed.set_image(url='https://c.tenor.com/kK8D7hQXX5wAAAAC/coins-tails.gif')
            embed.set_footer(text=config.footer)
            await interaction.response.send_message(embed=embed)
async def setup(bot):
    await bot.add_cog(coinflip(bot))