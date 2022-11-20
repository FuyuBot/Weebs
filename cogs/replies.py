import discord
from discord.ext import commands
import config

seniorstaff = 865054271857885225
managementTeam = 860758013731274762
staffTeam = 860758014386896926
member = 860757567566774322

class replies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `replies.py`")

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.channel.id == 865755491303817216 and message.author.id is not 926163269503299695:
                await discord.Message.delete(message)
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(replies(bot), guilds=[discord.Object(id=config.weebsHangout)])