import discord
from discord import app_commands
from discord.ext import commands
from dadjokes import Dadjoke


class dadJokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `dadJokes.py`")
    
    @app_commands.command(name="dadjoke", description="Sends a dad joke.")
    async def dadjoke(self, interaction: discord.Interaction):

        dj = Dadjoke()
        await interaction.response.send_message(f'Here is your dad joke {interaction.user.mention}\n`{dj.joke}`')

async def setup(bot):
    await bot.add_cog(dadJokes(bot))
