import discord
from discord import app_commands
from discord.ext import commands


class reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: 'reactions.py'")
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        try:
            if payload.message_id == 1036298274434453514:
                member = payload.member
                print("1")
                guild = member.guild
                print("1")
                emoji = payload.emoji.id
                print("1")
                if emoji == 1036298274434453514:
                    print("1")
                    role = discord.utils.get(guild.roles, name="He/Him")
                    print("1")
                    await member.add_roles(role)
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(reactions(bot), guilds=[discord.Object(id=860752406551461909)])