import discord
from discord import app_commands
from discord.ext import commands

class reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `reactions.py`")

    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.Member):
        if reaction.message.id == 1053328668283379783:
            player = user.id
            playerDB = ({"_id": player})
            genshin = playerDB['roles']['genshin']
            if reaction.emoji.name == "video_game" and genshin == True:
                return
            else:
                return





async def setup(bot):
    await bot.add_cog(reactions(bot), guilds=[discord.Object(id=860752406551461909)])