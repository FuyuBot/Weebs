import discord
import config
from discord import app_commands
from discord.ext import commands
import pymongo
import TOKEN

myclient = pymongo.MongoClient(TOKEN.mongoDB)
mydb = myclient['WeebsHangout']
mycol = mydb['user_info']

class verfiy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `verify.py`")

    @app_commands.command(name='verify', description='Verify that you are a human.')
    @app_commands.checks.has_any_role("unverified")
    async def verify(self, interaction:discord.Interaction):
        try:
            await interaction.response.send_modal(VerifyModal())
        except Exception as e:
            print(e)

    @app_commands.command(name='force-verify', description='Allows Administrators to forcibly verify someone.')
    @app_commands.checks.has_any_role("Administrator", "Management Team")
    async def forceverify(self, interaction:discord.Interaction, user: discord.Member):
        try:
            unverified = discord.utils.get(user.guild.roles, name="unverified")
            if unverified  in user.roles:
                verified = discord.utils.get(user.guild.roles, name="Member")
                logsChannel = interaction.client.get_channel(865073673668526080)
                welcomeChannel = interaction.client.get_channel(865056995295625256)

                logsEmbed = discord.Embed(
                    title=f'{user} Verified.',
                    color=config.color
                )
                logsEmbed.set_footer(text=f"ID: {user.id}")
                DMembed = discord.Embed(
                    title=f'You were forcibly verified by an Administrator of the server. Welcome to the server.',
                    color=config.color,
                    description=":loudspeaker: Please follow all the rules and have a great time here.\n\
                    In order to get DM's from our bot <@926163269503299695> please allow DM's on this server.\n\n\
                    Do `/roles` to get as many roles as you would want.\n\
                    <#915078396990603296> has a lot of the information for the server."
                )
                embed = discord.Embed(
                title=f'Welcome {user} to the server.',
                color=config.color,
                description=":loudspeaker: Please follow all the rules and have a great time here.\n\
                    In order to get DM's from our bot <@926163269503299695> please allow DM's on this server.\n\n\
                    Do `/roles` to get as many roles as you would want.\n\
                    <#915078396990603296> has a lot of the information for the server."
                )
                mydict = { 
                    "_id": user.id,
                    "info": {
                        "name": user.name,
                        "tag": user.discriminator,
                        "joined": user.joined_at,
                        "applied": False,
                        "currently_banned": False,
                        "messages": 0,
                        "mal": "none"
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

                await user.add_roles(verified)
                await user.remove_roles(unverified)
                await logsChannel.send(embed=logsEmbed)
                await user.send(embed=DMembed)
                await welcomeChannel.send(embed=embed)
                await interaction.response.send_message(f"{user} was verified successfully.")
            else:
                await interaction.response.send_message(f"That user is already verified.")
        except Exception as e:
            print(e)        

class VerifyModal(discord.ui.Modal, title="Verify"):
    verification = discord.ui.TextInput(label="Verification", placeholder="Enter your Name and Tag here. e.g. Name#1234", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        try:
            user = interaction.user
            userName = self.verification
            verified = discord.utils.get(user.guild.roles, name="Member")
            unverified = discord.utils.get(user.guild.roles, name="unverified")
            welcomeChannel = interaction.client.get_channel(865056995295625256)
            logsChannel = interaction.client.get_channel(865073673668526080)

            logsEmbed = discord.Embed(
                title=f'{user} Verified.',
                color=config.color
            )
            logsEmbed.set_footer(text=f"ID: {user.id}")
            embed = discord.Embed(
                title=f'Welcome {user} to the server.',
                color=config.color,
                description=":loudspeaker: Please follow all the rules and have a great time here.\n\
                    In order to get DM's from our bot <@926163269503299695> please allow DM's on this server.\n\n\
                    Do `/roles` to get as many roles as you would want.\n\
                    <#915078396990603296> has a lot of the information for the server."
                )

            if str(user) == str(userName):
                mydict = { 
                    "_id": interaction.user.id,
                    "info": {
                        "name": interaction.user.name,
                        "tag": interaction.user.discriminator,
                        "joined": interaction.user.joined_at,
                        "applied": False,
                        "currently_banned": False,
                        "mal": "none"
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

                await interaction.response.send_message("Success, Welcome to A Weeb's Hangout!", ephemeral= True)
                await user.add_roles(verified)
                await user.remove_roles(unverified)
                await logsChannel.send(embed=logsEmbed)
                await welcomeChannel.send(embed=embed)

            else:
                await interaction.response.send_message("'/verify' and enter your discord name and tag. e.g. Name#1234", ephemeral= True)
        except Exception as e:
            print("Error in verify modal: " + e)
            
            
async def setup(bot):
    await bot.add_cog(verfiy(bot), guilds=[discord.Object(id=config.weebsHangout)])