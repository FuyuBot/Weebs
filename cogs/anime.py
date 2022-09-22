import discord
from discord.ext import commands
from discord import app_commands
import requests

#API https://otakugifs.xyz/api


class anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `anime.py`')

    @app_commands.command(name='airkiss', description="Blow an airkiss to someone")
    async def airkiss(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=airkiss"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} blew a kiss at {user.mention}', embed=embed)

    @app_commands.command(name='angrystare', description="Stare Angerly at someone")
    async def angrystare(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=angrystare"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} angerly stared at {user.mention}', embed=embed)

    @app_commands.command(name='bite', description='Bite someone')
    async def bite(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=bite"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} Bit {user.mention}', embed=embed)

    @app_commands.command(name='blush', description='Blush')
    async def blush(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=blush"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} is blushing', embed=embed)

    @app_commands.command(name='brofist', description='Bro Fist')
    async def brofist(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=brofist"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} bro fisted {user.mention}', embed=embed)

    @app_commands.command(name='celebrate')
    async def celebrate(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=celebrate"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} is celebrating', embed=embed)

    @app_commands.command(name='cheers', description='Cheers')
    async def cheers(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=cheers"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} is cheering', embed=embed)

    @app_commands.command(name='clap', description='Clap')
    async def clap(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=clap"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} is clapping', embed=embed)

    @app_commands.command(name='confused', description='Confused')
    async def confused(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=confused"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is confused", embed=embed)

    @app_commands.command(name='cool', description='Cool')
    async def cool(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=cool"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} thinks its cool", embed=embed)

    @app_commands.command(name='cry', description='Cry')
    async def cry(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=cry"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is crying", embed=embed)

    @app_commands.command(name='cuddle', description='Cuddle with someone')
    async def cuddle(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=cuddle"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} wants to cuddle with {user.mention}', embed=embed)

    @app_commands.command(name='dance', description='Dance')
    async def dance(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=dance"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is dancing", embed=embed)

    @app_commands.command(name='drool', description='Drool')
    async def drool(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=drool"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is drooling", embed=embed)

    @app_commands.command(name='evillaugh', description='Evil Laugh')
    async def evillaugh(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=evillaugh"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} laughed evilly", embed=embed)

    @app_commands.command(name='facepalm', description='Facepalm')
    async def facepalm(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=facepalm"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} facepalmed", embed=embed)

    @app_commands.command(name='handhold', description="Hold someone's hand")
    async def handhold(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=handhold"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} held {user.mention} hand", embed=embed)

    @app_commands.command(name='happy', description='Happy')
    async def happy(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=happy"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is happy", embed=embed)

    @app_commands.command(name='headbang', description='Headbang')
    async def headbang(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=happy"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is happy", embed=embed)

    @app_commands.command(name='hug', description='Hug someone')
    async def hug(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=hug"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} gave {user.mention} a hug", embed=embed)

    @app_commands.command(name='kiss', description='Kiss someone')
    async def kiss(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=kiss"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} kissed {user.mention}", embed=embed)

    @app_commands.command(name='laugh', description='Laugh')
    async def laugh(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=laugh"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} starting to laugh", embed=embed)

    @app_commands.command(name='lick', description='Lick someone')
    async def lick(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=lick"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} kissed {user.mention}", embed=embed)

    @app_commands.command(name='love', description='Love someone')
    async def love(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=love"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is inlove with {user.mention}", embed=embed)

    @app_commands.command(name='mad', description='Mad')
    async def mad(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=mad"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is angry", embed=embed)

    @app_commands.command(name='nervous', description='Nervous')
    async def nervous(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=nervous"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} is nervous', embed=embed)

    @app_commands.command(name='no', description='No')
    async def no(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=no"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} said no', embed=embed)

    @app_commands.command(name='nom', description='Nom')
    async def nom(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=nom"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} nommed", embed=embed)

    @app_commands.command(name='nosebleed', description='Nosebleed')
    async def nosebleed(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=nosebleed"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} got a nosebleed", embed=embed)

    @app_commands.command(name='nuzzle', description='Nuzzle')
    async def nuzzle(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=nuzzle"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} nuzzled {user.mention}", embed=embed)

    @app_commands.command(name='nyah', description='Nyah')
    async def nyah(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=nyah"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f'{interaction.user.mention} nyah {user.mention}', embed=embed)

    @app_commands.command(name='pat', description='Pat someone')
    async def pat(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=pat"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} pat {user.mention}", embed=embed)

    @app_commands.command(name='peek', description='Peek at someone')
    async def peek(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=peek"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} peeked at {user.mention}", embed=embed)

    @app_commands.command(name='pinch', description='Pinch someone')
    async def pinch(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=pinch"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} pinched {user.mention}", embed=embed)

    @app_commands.command(name='poke', description='Poke someone')
    async def poke(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=poke"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} poked {user.mention}", embed=embed)

    @app_commands.command(name='pout', description='Pout')
    async def pout(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=pout"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is pouting", embed=embed)

    @app_commands.command(name='punch', description='Punch someone')
    async def punch(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=punch"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} punched {user.mention}", embed=embed)

    @app_commands.command(name='roll', description='Roll')
    async def roll(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=roll"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} rolled", embed=embed)

    @app_commands.command(name='run', description='Run away')
    async def run(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=run"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} ran away from {user.mention}", embed=embed)

    @app_commands.command(name='sad', description='Sad')
    async def sad(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=sad"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is sad", embed=embed)

    @app_commands.command(name='scared', description='Scared')
    async def scared(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=scared"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is scared", embed=embed)

    @app_commands.command(name='shrug', description='¯\_(ツ)_/¯')
    async def shrug(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=shrug"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} shrugged", embed=embed)

    @app_commands.command(name='shy', description='Be Shy')
    async def shy(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=shy"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is shy", embed=embed)

    @app_commands.command(name='sigh', description='Sigh')
    async def sigh(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=sigh"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} sighed", embed=embed)

    @app_commands.command(name='sip', description='Sip')
    async def sip(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=sip"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} took a sipped", embed=embed)

    @app_commands.command(name='slap', description='Slap someone')
    async def slap(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=slap"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} slapped {user.mention}", embed=embed)

    @app_commands.command(name='sleep', description='Fall asleep')
    async def sleep(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=sleep"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} fell asleep", embed=embed)

    @app_commands.command(name='slowclap', description='Slowclap')
    async def slowclap(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=slowclap"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} clapped slowly", embed=embed)

    @app_commands.command(name='smack', description='Smack someone')
    async def smack(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=smack"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} smack {user.mention}", embed=embed)

    @app_commands.command(name='smile', description='Smile')
    async def smile(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=smile"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_money(f"{interaction.user.mention} smiled", embed=embed)

    @app_commands.command(name='smug', description='Smug')
    async def smug(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=smug"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} smugged", embed=embed)

    @app_commands.command(name='sneeze', description='Sneeze')
    async def sneeze(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=sneeze"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} Sneezed", embed=embed)

    @app_commands.command(name='sorry', description='Sorry')
    async def sorry(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=sorry"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is sorry", embed=embed)

    @app_commands.command(name='stare', description='Stare')
    async def stare(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=stare"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} stared at {user.mention}", embed=embed)

    @app_commands.command(name='stop', description='Stop')
    async def stop(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=stop"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} STOP", embed=embed)

    @app_commands.command(name='surprise', description='Surprise')
    async def surprise(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=surprised"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is surprised", embed=embed)

    @app_commands.command(name='sweat', description='Sweat')
    async def sweat(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=sweat"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is sweating", embed=embed)

    @app_commands.command(name='thumbsup', description='Put your thumb up')
    async def thumbsup(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=thumbsup"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} put their thumb up", embed=embed)

    @app_commands.command(name='tickle', description='Tickle someone')
    async def tickle(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=tickle"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} tickled {user.mention}", embed=embed)

    @app_commands.command(name='tired', description='Tired')
    async def tired(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=tired"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} is tired", embed=embed)

    @app_commands.command(name='wave', description='Wave to someone')
    async def wave(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=wave"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        embed.set_footer(text=f"Bot created by Jzcob#2842 and Sezn#6554")
        await interaction.response.send_message(f"{interaction.user.mention} waved at {user.mention}", embed=embed)

    @app_commands.command(name='wink', description='Wink at someone')
    async def wink(self, interaction: discord.Interaction, user: discord.Member):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=wink"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} winked at {user.mention}", embed=embed)

    @app_commands.command(name='woah', description=':o')
    async def woah(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=woah"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} woahed", embed=embed)

    @app_commands.command(name='yawn', description='Yawn')
    async def yawn(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=yawn"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)

        await interaction.response.send_message(f"{interaction.user.mention} Yawned", embed=embed)

    @app_commands.command(name='yay', description='Yay')
    async def yay(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=yay"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} Yayed", embed=embed)

    @app_commands.command(name='yes', description='Yes')
    async def yes(self, interaction: discord.Interaction):
        animeUrl = "https://api.otakugifs.xyz/gif?reaction=yes"
        animeGet = requests.get(animeUrl)
        animeGif = animeGet.json()['url']
        embed = discord.Embed(
            color=0x2699C6
        )
        embed.set_image(url=animeGif)
        await interaction.response.send_message(f"{interaction.user.mention} is happy", embed=embed)


async def setup(bot):
    await bot.add_cog(anime(bot))