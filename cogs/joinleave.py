import discord
from discord.ext import commands
from discord import app_commands
import config
import pymongo

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient['WeebsHangout']
mycol = mydb['user_info']

class joinleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `joinleave.py`")
    
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        try:
            mycol.delete_one({"_id": member.id})
            logsChannel = self.bot.get_channel(865073673668526080)
            logsEmbed = discord.Embed(
                title=f'{member} left the server',
                color=discord.Color.red()
            )
            logsEmbed.set_footer(text=f"ID: {member.id}")
            await logsChannel.send(embed=logsEmbed)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logsChannel = self.bot.get_channel(865073673668526080)
        logsEmbed = discord.Embed(
            title=f'{member} joined the server',
            color=discord.Color.green()
        )
        
        logsEmbed.set_footer(text=f"ID: {member.id}")
        unverified = discord.utils.get(member.guild.roles, name="unverified")
        await member.add_roles(unverified)
        await logsChannel.send(embed=logsEmbed)
   
    @app_commands.command(name="test-join", description="Sends a test join to test the database.")
    @app_commands.checks.has_any_role("Management Team")
    async def test_join(self, interaction: discord.Interaction, member: discord.Member):
        try:
            mydict = { 
                "_id": member.id,
                "info": {
                    "name": member.name,
                    "tag": member.discriminator,
                    "joined": member.joined_at,
                    "applied": False,
                    "currently_banned": False
                },
                "levels": {
                    "level": 0,
                    "xp": 0
                },
                "economy": {
                    "wallet": 0,
                    "bank": 0
                },
                "punishments": {
                    "bans": [],
                    "timeouts": [],
                    "warns": [],
                    "notes": []
                },
                "roles": {
                    "green" : False,
                    "red": False,
                    "blue": False,
                    "yellow": False,
                    "ninja": False,
                    "orange": False,
                    "teal": False,
                    "purple": False,
                    "white": False
                }
            }
        
            mycol.insert_one(mydict)

            await interaction.response.send_message("Success!", ephemeral=True)
        except Exception as e:
            print(e)



async def setup(bot):
    await bot.add_cog(joinleave(bot), guilds=[discord.Object(id=860752406551461909)])