import discord
from discord import app_commands
from discord.ext import commands
import config
import pymongo
import random

"""styleList = ['Rustic', 'Modern', "Japanese", "Coastal", "Western", "Cyberpunk", 'Antique', "Minimalist", "Medevial", "90's", "80's", "70's", "60's"]
colorList = ['Blue', 'Green', "Red", "Purple", "Neon **ANY**", "Orage", "Yellow"]"""

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["InternationalGang"]
mycol = mydb["bot_info"]

class houseflipper(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"LOADED: `houseflipper.py`")
    
    @app_commands.command(name="houseflipper")
    @app_commands.describe(hf="What would you like to get randomized?")
    @app_commands.choices(hf=[
        discord.app_commands.Choice(name='style', value="style"),
        discord.app_commands.Choice(name='color', value="colors")
    ])
    async def houseflipper(self, interaction: discord.Interaction, hf: discord.app_commands.Choice[str]):
        try:
            if hf.name == "style":
                server = interaction.guild.id
                serverdB = mycol.find_one({"_id": server})
                styleList = serverdB['styleList']
                randomStyle = random.choice(styleList)
                embed = discord.Embed(title=f"Style chosen was `{randomStyle}`!", color=discord.Color.teal())
                return await interaction.response.send_message(embed=embed)
            if hf.name == "color":
                server = interaction.guild.id
                serverdB = mycol.find_one({"_id": server})
                colorList = serverdB['colorList']
                randomColor = random.choice(colorList)
                embed = discord.Embed(title=f"Color chosen was `{randomColor}`!", color=discord.Color.teal())
                return await interaction.response.send_message(embed=embed)
        except Exception as e:
            return await interaction.response.send_message(f"> Error: `{e}`")
    
    @app_commands.command(name="stylelist", description="List all of the styles that are in the bot")
    async def stylelist(self, interaction : discord.Interaction):
        try:
            server = interaction.guild.id
            serverdB = mycol.find_one({"_id": server})
            styleList = serverdB['styleList']
            return await interaction.response.send_message(f"`{styleList}`")
        except Exception as e:
            return await interaction.response.send_message(f"> Error: `{e}`")
    
    @app_commands.command(name="colorlist", description="List all of the colors that are in the bot")
    async def colorlist(self, interaction : discord.Interaction):
        try:
            server = interaction.guild.id
            serverdB = mycol.find_one({"_id": server})
            colorList = serverdB['colorList']
            return await interaction.response.send_message(f"`{colorList}`")
        except Exception as e:
            return await interaction.response.send_message(f"> Error: `{e}`")
    
    @app_commands.command(name="add-style", description="Update the list that is for the houseflipper part of the bot")
    async def addToList(self, interaction: discord.Interaction, adding: str):
        try:
            server = interaction.guild.id
            serverdB = mycol.find_one({"_id": server})
            styleList = list(serverdB['styleList'])
            styleList.append(adding)
            mycol.update_one({'_id': server}, {"$set": {"styleList": styleList}})
            await interaction.response.send_message(":thumbsup:")
            print("Added to the list successfully!")
        except Exception as e:
            return await interaction.response.send_message(f"> Error: `{e}`")
    
    @app_commands.command(name="remove-style", description="Update the list that is for the houseflipper part of the bot")
    async def removeFromList(self, interaction: discord.Interaction, removing: str):
        server = interaction.guild.id
        serverdB = mycol.find_one({"_id": server})
        styleList = list(serverdB['styleList'])
        try:
            styleList.remove(removing)
            mycol.update_one({'_id': server}, {"$set": {"styleList": styleList}})
            await interaction.response.send_message(":thumbsup:")
            print("Removed from the list successfully!")
        except Exception as e:
            return await interaction.response.send_message(f"> Error: `{e}`\n\nPlease note if error message is `list.remove(x): x not in list`, the command is case-sensitive.")
    
    @app_commands.command(name="add-color", description="Update the list that is for the houseflipper part of the bot")
    async def addColorToList(self, interaction: discord.Interaction, adding: str):
        server = interaction.guild.id
        serverdB = mycol.find_one({"_id": server})
        colorList = list(serverdB['colorList'])
        colorList.append(adding)
        mycol.update_one({'_id': server}, {"$set": {"styleList": colorList}})
        await interaction.response.send_message(":thumbsup:")
        print("Added to the list successfully!")
    
    @app_commands.command(name="remove-color", description="Update the list that is for the houseflipper part of the bot")
    async def removeColorFromList(self, interaction: discord.Interaction, removing: str):
        server = interaction.guild.id
        serverdB = mycol.find_one({"_id": server})
        colorList = list(serverdB['colorList'])
        try:
            colorList.remove(removing)
            mycol.update_one({'_id': server}, {"$set": {"colorList": colorList}})
            await interaction.response.send_message(":thumbsup:")
            print("Removed from the list successfully!")
        except Exception as e:
            return await interaction.response.send_message(f"> Error: `{e}`\n\nPlease note if error message is: `list.remove(x): x not in list`, the command is case-sensitive.")

    
    """@app_commands.command(name="setup-db", description="Allows the admins to setup the database.")
    @app_commands.checks.has_permissions(administrator=True)
    async def dbSetup(self, interaction: discord.Interaction):
        mydict = {
            "_id": 920801858967191573,
            "name": interaction.guild.name,
            "ownerID": interaction.guild.owner.name,
            "ownerName": interaction.guild.owner_id,
            "styleList": styleList,
            "colorList": colorList
        }
        try:
            mycol.insert_one(mydict)
            await interaction.response.send_message(":thumbsup:")
            print("Added to the database successfully!")
        except Exception as e:
            print(e)"""

async def setup(bot):
    await bot.add_cog(houseflipper(bot), guilds=[discord.Object(id=config.internationalGang)])
