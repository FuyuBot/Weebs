import discord
from discord import app_commands
from discord.ui import Button,View
from discord.ext import commands
import requests
import random
import config
from config import truth,dare,wyr,nhie,paranoia

Turl = truth
Durl = dare
Wurl = wyr
Nurl = nhie
Purl = paranoia


Tget = requests.get(Turl)
Tquestion = Tget.json()['question']
Trating = Tget.json()['rating']
Dget = requests.get(Durl)
Dquestion = Dget.json()['question']
Drating = Dget.json()['rating']
Wget = requests.get(Wurl)
Wquestion = Wget.json()['question']
Wrating = Wget.json()['rating']
Nget = requests.get(Nurl)
Nquestion = Nget.json()['question']
Nrating = Nget.json()['rating']
Pget = requests.get(Purl)
Pquestion = Pget.json()['question']
Prating = Pget.json()['rating']


truthButton = Button(label="Truth", style=discord.ButtonStyle.success)
dareButton = Button(label="Dare", style=discord.ButtonStyle.danger)
wyrButton = Button(label="Would you Rather", style=discord.ButtonStyle.primary)
nhieButton = Button(label="Never have I ever", style=discord.ButtonStyle.primary)
paranoiaButton = Button(label="Paranoia", style=discord.ButtonStyle.primary)
randomButton = Button(label="Random", style=discord.ButtonStyle.secondary)


async def dareButton_callback(interaction):
    Dget = requests.get(Durl)
    Dquestion = Dget.json()['question']
    Drating = Dget.json()['rating']

    embed = discord.Embed(
        title=Dquestion,
        description=f"Type: Dare | Rated: {Drating}",
        color=discord.Color.red()
    )
    embed.set_footer(text=config.footer)
    view = View()
    view.add_item(truthButton)
    view.add_item(dareButton)
    view.add_item(wyrButton)
    view.add_item(nhieButton)
    view.add_item(paranoiaButton)
    await interaction.response.send_message(embed=embed,view=view)

async def truthButton_callback(interaction):
    Tget = requests.get(Turl)
    Tquestion = Tget.json()['question']
    Trating = Tget.json()['rating']

    embed = discord.Embed(
        title=Tquestion,
        description=f"Type: Truth | Rated: {Trating}",
        color=discord.Color.green()
    )
    embed.set_footer(text=config.footer)
    view = View()
    view.add_item(truthButton)
    view.add_item(dareButton)
    view.add_item(wyrButton)
    view.add_item(nhieButton)
    view.add_item(paranoiaButton)
    await interaction.response.send_message(embed=embed,view=view)


async def wyrButton_callback(interaction):
    Wget = requests.get(Wurl)
    Wquestion = Wget.json()['question']
    Wrating = Wget.json()['rating']
    embed = discord.Embed(
        title=Wquestion,
        description=f"Type: Would You Rather | Rated: {Wrating}",
        color=discord.Color.blue()
    )
    embed.set_footer(text=config.footer)
    view = View()
    view.add_item(truthButton)
    view.add_item(dareButton)
    view.add_item(wyrButton)
    view.add_item(nhieButton)
    view.add_item(paranoiaButton)
    await interaction.response.send_message(embed=embed,view=view)

async def nhieButton_callback(interaction):
    Nget = requests.get(Nurl)
    Nquestion = Nget.json()['question']
    Nrating = Nget.json()['rating']
    embed = discord.Embed(
        title=Nquestion,
        description=f"Type: Never Have I Ever | Rated: {Nrating}",
        color=discord.Color.orange()
    )
    embed.set_footer(text=config.footer)
    view = View()
    view.add_item(truthButton)
    view.add_item(dareButton)
    view.add_item(wyrButton)
    view.add_item(nhieButton)
    view.add_item(paranoiaButton)
    await interaction.response.send_message(embed=embed,view=view)
async def paranoiaButton_callback(interaction):
    Pget = requests.get(Purl)
    Pquestion = Pget.json()['question']
    Prating = Pget.json()['rating']
    embed = discord.Embed(
        title=Pquestion,
        description=f"Type: Paranoia | Rated: {Prating}",
        color=discord.Color.purple()
    )
    embed.set_footer(text=config.footer)
    view = View()
    view.add_item(truthButton)
    view.add_item(dareButton)
    view.add_item(wyrButton)
    view.add_item(nhieButton)
    view.add_item(paranoiaButton)
    await interaction.response.send_message(embed=embed,view=view)

class questions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `questions.py`")
    
    @app_commands.command(name='truth', description="Truth")
    async def truth(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=Tquestion,
            description=f"Type: Truth | Rated: {Trating}",
            color=discord.Color.green()
        )
        embed.set_footer(text=config.footer)
        view = View()
        view.add_item(truthButton)
        view.add_item(dareButton)
        view.add_item(wyrButton)
        view.add_item(nhieButton)
        view.add_item(paranoiaButton)
        await interaction.response.send_message(embed=embed, view=view)
        truthButton.callback = truthButton_callback
        dareButton.callback = dareButton_callback
        wyrButton.callback = wyrButton_callback
        nhieButton.callback = nhieButton_callback
        paranoiaButton.callback = paranoiaButton_callback

    @app_commands.command(name='dare', description="Dare")
    async def dare(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=Dquestion,
            description=f"Type: Dare | Rated: {Drating}",
            color=discord.Color.red()
        )
        embed.set_footer(text=config.footer)
        view = View()
        view.add_item(truthButton)
        view.add_item(dareButton)
        view.add_item(wyrButton)
        view.add_item(nhieButton)
        view.add_item(paranoiaButton)
        await interaction.response.send_message(embed=embed, view=view)
        truthButton.callback = truthButton_callback
        dareButton.callback = dareButton_callback
        wyrButton.callback = wyrButton_callback
        nhieButton.callback = nhieButton_callback
        paranoiaButton.callback = paranoiaButton_callback

    @app_commands.command(name='wyr', description="Would you rather")
    async def wyr(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=Wquestion,
            description=f"Type: Would You Rather | Rated: {Wrating}",
            color=discord.Color.blue()
        )
        embed.set_footer(text=config.footer)
        view = View()
        view.add_item(truthButton)
        view.add_item(dareButton)
        view.add_item(wyrButton)
        view.add_item(nhieButton)
        view.add_item(paranoiaButton)
        await interaction.response.send_message(embed=embed, view=view)
        truthButton.callback = truthButton_callback
        dareButton.callback = dareButton_callback
        wyrButton.callback = wyrButton_callback
        nhieButton.callback = nhieButton_callback
        paranoiaButton.callback = paranoiaButton_callback
    
    @app_commands.command(name='nhie', description="Never have I ever")
    async def nhie(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=Nquestion,
            description=f"Type: Never Have I Ever | Rated: {Nrating}",
            color=discord.Color.orange()
        )
        embed.set_footer(text=config.footer)
        view = View()
        view.add_item(truthButton)
        view.add_item(dareButton)
        view.add_item(wyrButton)
        view.add_item(nhieButton)
        view.add_item(paranoiaButton)
        await interaction.response.send_message(embed=embed, view=view)
        truthButton.callback = truthButton_callback
        dareButton.callback = dareButton_callback
        wyrButton.callback = wyrButton_callback
        nhieButton.callback = nhieButton_callback
        paranoiaButton.callback = paranoiaButton_callback
    @app_commands.command(name='paranoia', description="Paranoia")
    async def paranoia(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=Pquestion,
            description=f"Type: Paranoia | Rated: {Prating}",
            color=discord.Color.purple()
        )
        embed.set_footer(text=config.footer)
        view = View()
        view.add_item(truthButton)
        view.add_item(dareButton)
        view.add_item(wyrButton)
        view.add_item(nhieButton)
        view.add_item(paranoiaButton)
        await interaction.response.send_message(embed=embed, view=view)
        truthButton.callback = truthButton_callback
        dareButton.callback = dareButton_callback
        wyrButton.callback = wyrButton_callback
        nhieButton.callback = nhieButton_callback
        paranoiaButton.callback = paranoiaButton_callback
    @app_commands.command(name='random', description="Random")
    async def random(self, interaction: discord.Interaction):
        randnum = random.randrange(1,6)
        if randnum == 1:
            embed = discord.Embed(
            title=Tquestion,
            description=f"Type: TRUTH and Rating: {Trating}",
            color=discord.Color.green()
            )
            embed.set_footer(text=config.footer)
            view = View()
            view.add_item(truthButton)
            view.add_item(dareButton)
            view.add_item(wyrButton)
            view.add_item(nhieButton)
            view.add_item(paranoiaButton)
            await interaction.response.send_message(embed=embed, view=view)
            truthButton.callback = truthButton_callback
            dareButton.callback = dareButton_callback
            wyrButton.callback = wyrButton_callback
            nhieButton.callback = nhieButton_callback
            paranoiaButton.callback = paranoiaButton_callback
        elif randnum == 2:
            embed = discord.Embed(
            title=Dquestion,
            description=f"Type: Dare | Rated: {Drating}",
            color=discord.Color.red()
            )
            embed.set_footer(text=config.footer)
            view = View()
            view.add_item(truthButton)
            view.add_item(dareButton)
            view.add_item(wyrButton)
            view.add_item(nhieButton)
            view.add_item(paranoiaButton)
            await interaction.response.send_message(embed=embed,view=view)
            truthButton.callback = truthButton_callback
            dareButton.callback = dareButton_callback
            wyrButton.callback = wyrButton_callback
            nhieButton.callback = nhieButton_callback
            paranoiaButton.callback = paranoiaButton_callback
        elif randnum == 3:
            embed = discord.Embed(
            title=Wquestion,
            description=f"Type: Would You Rather | Rated: {Wrating}",
            color=discord.Color.blue()
            )
            embed.set_footer(text=config.footer)
            view = View()
            view.add_item(truthButton)
            view.add_item(dareButton)
            view.add_item(wyrButton)
            view.add_item(nhieButton)
            view.add_item(paranoiaButton)
            await interaction.response.send_message(embed=embed,view=view)
            truthButton.callback = truthButton_callback
            dareButton.callback = dareButton_callback
            wyrButton.callback = wyrButton_callback
            nhieButton.callback = nhieButton_callback
            paranoiaButton.callback = paranoiaButton_callback
        elif randnum == 4:
            embed = discord.Embed(
            title=Nquestion,
            description=f"Type: Never Have I Ever | Rated: {Nrating}",
            color=discord.Color.orange()
            )
            embed.set_footer(text=config.footer)
            view = View()
            view.add_item(truthButton)
            view.add_item(dareButton)
            view.add_item(wyrButton)
            view.add_item(nhieButton)
            view.add_item(paranoiaButton)
            await interaction.response.send_message(embed=embed,view=view)
            truthButton.callback = truthButton_callback
            dareButton.callback = dareButton_callback
            wyrButton.callback = wyrButton_callback
            nhieButton.callback = nhieButton_callback
            paranoiaButton.callback = paranoiaButton_callback
        elif randnum == 5:
            embed = discord.Embed(
            title=Pquestion,
            description=f"Type: Paranoia | Rated: {Prating}",
            color=discord.Color.purple()
            )
            embed.set_footer(text=config.footer)
            view = View()
            view.add_item(truthButton)
            view.add_item(dareButton)
            view.add_item(wyrButton)
            view.add_item(nhieButton)
            view.add_item(paranoiaButton)
            await interaction.response.send_message(embed=embed,view=view)
            truthButton.callback = truthButton_callback
            dareButton.callback = dareButton_callback
            wyrButton.callback = wyrButton_callback
            nhieButton.callback = nhieButton_callback
            paranoiaButton.callback = paranoiaButton_callback
        else:
            await interaction.response.send_message("Failed!")
            print(randnum)

async def setup(bot):
    await bot.add_cog(questions(bot))