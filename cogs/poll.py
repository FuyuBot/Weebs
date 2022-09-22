import discord
from discord import app_commands
from discord.ext import commands

import config
from config import embedFooter


class poll(commands.Cog):
    def __int__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `poll.py`')

    @app_commands.command(name='poll', description='Start a Poll.')
    async def poll(self, interaction: discord.Interaction,channel: discord.TextChannel , title: str, option1: str, option2: str, option3: str=None, option4: str=None):
        user = interaction.user

        embed = discord.Embed(
            title=f'{title}'
        )
        embed.add_field(name=':one:', value=option1)
        embed.add_field(name=':two;', value=option2)
        if option3 is not None:
            embed.add_field(name=':three:', value=option3)

        if option4 is not None:
            embed.add_field(name=':four:', value=option4)
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')

        await interaction.response.send_message(embed=embed)
        #await channel.send(embed=embed)
        await interaction.message.add_reaction(self, ":one:")
        await interaction.message.add_reaction(self, ":two:")
        await interaction.message.add_reaction(self, ":three:")
        await interaction.message.add_reaction(self, ":four:")



async def setup(bot):
    await bot.add_cog(poll(bot), guilds=[discord.Object(id=860752406551461909)])