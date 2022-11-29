import discord
import pymongo
import requests
import config
from discord.ext import commands
from discord import app_commands


myclient = config.mongoDB

class punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED `punishments.py`")
    
    






async def setup(bot):
    await bot.add_cog(punishments(bot), guilds=[discord.Object(id=860752406551461909)])