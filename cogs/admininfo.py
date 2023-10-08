import discord
from discord import app_commands
from discord.ext import commands
import pymongo
import config
import TOKEN


myclient = pymongo.MongoClient(TOKEN.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]

class admininfo(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot

    
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"LOADED: `broadcast.py`")


    @app_commands.command(name='get-info', description="As a Management Member you can check someone's database status.")
    @app_commands.checks.has_any_role('Management Team', "Hidden Manager")
    async def broadcast(self, interaction: discord.Interaction, user: discord.Member):
        embed = discord.Embed(
            title=f"{user}'s database information",
            color=0x2699C6
        )
        player = user.id
        playerDB = mycol.find_one({"_id": player})
        name = playerDB['info']['name']
        tag = playerDB['info']['tag']
        messages = playerDB['info']['messages']
        wallet = playerDB['economy']['wallet']
        bank = playerDB['economy']['bank']
        level = playerDB['levels']['level']
        xp = playerDB['levels']['xp']
        embed.add_field(name="Name", value=name)
        embed.add_field(name="Tag", value=tag)
        embed.add_field(name="Messages", value=messages)
        embed.add_field(name="Wallet", value=wallet)
        embed.add_field(name="Bank", value=bank)
        embed.add_field(name=f"‎ ", value=f"‎ ")
        embed.add_field(name="Level", value=level)
        embed.add_field(name="XP", value=xp)
        await interaction.response.send_message(embed=embed)
        #await interaction.response.send_message(f"Message sent to {channel}.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(admininfo(bot), guilds=[discord.Object(id=860752406551461909)])