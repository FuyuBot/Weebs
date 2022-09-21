import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button,View
import random


rockButton = Button(label="", style=discord.ButtonStyle.secondary, emoji="🪨")
paperButton = Button(label="", style=discord.ButtonStyle.secondary, emoji="📰")
scissorsButton = Button(label="", style=discord.ButtonStyle.secondary, emoji="✂️")
replayButton = Button(label="", style=discord.ButtonStyle.secondary, emoji="🔃")

async def rockButton_callback(interaction):
    x = random.randrange(1,4)
    if x == 1: #1 rock, 2 paper, 3 scissors
        embed = discord.Embed(
            title="Tie.",
            description=":robot:>  :rock: | :rock:  <:neutral_face:\n\nChoose your choice with one of the button.",
            color=0x2699C6
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(rockButton)
        view.add_item(paperButton)
        view.add_item(scissorsButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback
    elif x == 2:
        embed = discord.Embed(
            title="You lost.",
            description=":robot:>  :newspaper: | :rock:  <:sob:\n\nTo replay click or tap the replay button.",
            color=discord.Color.red()
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(replayButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback
    elif x == 3:
        embed = discord.Embed(
            title="You won!",
            description=":robot:>  :scissors: | :rock:  <:grin:\n\nTo replay click or tap the replay button.",
            color=discord.Color.green()
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(replayButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback

async def paperButton_callback(interaction):
    x = random.randrange(1,4)
    if x == 1: #1 rock, 2 paper, 3 scissors
        embed = discord.Embed(
            title="You won!",
            description=":robot:>  :rock: | :newspaper:  <:grin:\n\nTo replay click or tap the replay button.",
            color=discord.Color.green()
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(replayButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback
    elif x == 2:
        embed = discord.Embed(
            title="Tie.",
            description=":robot:>  :newspaper: | :newspaper:  <:neutral_face:\n\nChoose your choice with one of the button.",
            color=0x2699C6
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(rockButton)
        view.add_item(paperButton)
        view.add_item(scissorsButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback
    elif x == 3:
        embed = discord.Embed(
            title="You lost.",
            description=":robot:>  :scissors: | :newspaper:  <:sob:\n\nTo replay click or tap the replay button.",
            color=discord.Color.red()
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(replayButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback

async def scissorsButton_callback(interaction):
    x = random.randrange(1,4)
    if x == 1: #1 rock, 2 paper, 3 scissors
        embed = discord.Embed(
            title="You lost.",
            description=":robot:>  :rock: | :scissors:  <:sob:\n\nTo replay click or tap the replay button.",
            color=discord.Color.red()
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(replayButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback
    elif x == 2:
        embed = discord.Embed(
            title="You won!",
            description=":robot:>  :newspaper: | :scissors:  <:grin:\n\nTo replay click or tap the replay button.",
            color=discord.Color.green()
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(replayButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback
    elif x == 3:
        embed = discord.Embed(
            title="Tie.",
            description=":robot:>  :scissors: | :scissors:  <:neutral_face:\n\nChoose your choice with one of the button.",
            color=0x2699C6
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(rockButton)
        view.add_item(paperButton)
        view.add_item(scissorsButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        replayButton.callback = replayButton_callback

async def replayButton_callback(interaction):
    embed = discord.Embed(
            title="Rock-Paper-Scissors",
            description="Choose your choice with one of the buttons.",
            color=0x2699C6
        )
    embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
    view = View()
    view.add_item(rockButton)
    view.add_item(paperButton)
    view.add_item(scissorsButton)
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    rockButton.callback = rockButton_callback
    paperButton.callback = paperButton_callback
    scissorsButton.callback = scissorsButton_callback

class rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `rps.py`")

    @app_commands.command(name='rps', description="Rock Paper or Scissors")
    async def rps(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Rock-Paper-Scissors",
            description="Choose your choice with one of the buttons.",
            color=0x2699C6
        )
        embed.set_footer(text='Bot created by Jzcob#2842 and Sezn#6554.')
        view = View()
        view.add_item(rockButton)
        view.add_item(paperButton)
        view.add_item(scissorsButton)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        rockButton.callback = rockButton_callback
        paperButton.callback = paperButton_callback
        scissorsButton.callback = scissorsButton_callback

async def setup(bot):
    await bot.add_cog(rps(bot))