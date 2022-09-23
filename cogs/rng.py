import discord
from discord import app_commands
from discord.ext import commands
from random import randint


class rng(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"LOADED: `rng.py`")
    

    @app_commands.command(name='rng', description="Random anime game.")
    @app_commands.describe(animelist='Which list do you want to pick from?')
    @app_commands.choices(animelist=[
        discord.app_commands.Choice(name='ja', value=24 + 140),
        discord.app_commands.Choice(name='ji', value=21 + 212),
        discord.app_commands.Choice(name='k', value=36 + 664)
    ])
    async def rng(self, interaction: discord.Interaction, animelist: discord.app_commands.Choice[int]):
        if animelist.name == "ja":
            await interaction.response.send_message(f"Jacob's List: {randint(1, animelist.value)}")
        elif animelist.name == "ji":
            await interaction.response.send_message(f"Jillian's List: {randint(1, animelist.value)}")
        elif animelist.name == "k":
            await interaction.response.send_message(f"Kyle's List: {randint(1, animelist.value)}")
        else:
            await interaction.response.send_message(f"{interaction.user.mention} It didn't work!")


async def setup(bot):
    await bot.add_cog(rng(bot), guilds=[discord.Object(id=860752406551461909)])