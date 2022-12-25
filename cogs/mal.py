import discord
from discord import app_commands
from discord.ext import commands
import config
import pymongo
import requests

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]

class mal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `mal.py`")

    @app_commands.command(name="mal", description="Set or view a MAL account.")
    @app_commands.checks.has_any_role("Member")
    @app_commands.choices(option=[
        discord.app_commands.Choice(name='Me', value="me"),
        discord.app_commands.Choice(name='Member', value="member"),
        discord.app_commands.Choice(name='Set', value="set")
        
    ])
    async def mal(self, interaction: discord.Interaction, option: discord.app_commands.Choice[str], who: discord.Member=None):
        try:
            
            if option.value == "me":
                member = interaction.user
                playerDB = mycol.find_one({"_id": member.id})
                if playerDB['info']['mal'] == "none":
                    return await interaction.response.send_message("You do not have a link set. Set one with `/mal Set` with the link.", ephemeral=True)
                else:
                    link = playerDB['info']['mal']
                    embed = discord.Embed(color=config.color, title=f"{member.name}'s MyAnimeList",url=link)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            elif option.value == "member":
                member = who
                playerDB = mycol.find_one({"_id": member.id})
                if playerDB['info']['mal'] == "none":
                    return await interaction.response.send_message("They do not have their MAL set.", ephemeral=True)
                else:
                    link = playerDB['info']['mal']
                    embed = discord.Embed(color=config.color, title=f"{member.name}'s MyAnimeList",url=link)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            elif option.value == "set":
                await interaction.response.send_modal(LinkModal())

        except Exception as e:
            print(e)

class LinkModal(discord.ui.Modal, title= "Set your My Anime List link"):
    link = discord.ui.TextInput(label="What is your MAL link?", required=True, placeholder="https://myanimelist.net/profile/Jzcob")
    async def on_submit(self, interaction: discord.Interaction):
        try:
            player = interaction.user
            if "https://myanimelist.net/profile/" in str(self.link):
                url = self.link
                get = requests.get(url)
                if str(get) == "<Response [200]>":
                    mycol.update_one({"_id": player.id}, {"$set": {"info.mal": str(url)}})
                    await interaction.response.send_message("Successfully set your MAL.", ephemeral=True)
                else:
                    await interaction.response.send_message("Not a valid user", ephemeral=True)
            else:
                await interaction.response.send_message("Your link must be a MAL link.", ephemeral=True)
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(mal(bot), guilds=[discord.Object(id=860752406551461909)])