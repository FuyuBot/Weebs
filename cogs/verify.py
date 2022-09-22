import discord
from discord import app_commands
from discord.ext import commands

class verfiy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `verify.py`")

    @app_commands.command(name='verify', description='Verify that you are a human.')
    @app_commands.checks.has_any_role("unverified")
    async def verify(self, interaction:discord.Interaction):
        await interaction.response.send_modal(VerifyModal())
        
class VerifyModal(discord.ui.Modal, title="Verify"):
    verification = discord.ui.TextInput(label="Verification", placeholder="Enter your Name and Tag here. e.g. Name#1234", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        user = interaction.user
        userName = self.verification
        verified = discord.utils.get(user.guild.roles, name="Member")
        unverified = discord.utils.get(user.guild.roles, name="unverified")
        welcomeChannel = interaction.client.get_channel(865056995295625256)
        logsChannel = interaction.client.get_channel(865073673668526080)
        
        logsEmbed = discord.Embed(
            title=f'{user} Verified.',
            color=discord.Color.green()
        )
        embed = discord.Embed(
            title=f'Welcome {user} to the server.',
            color=discord.Color.green(),
            description=":loudspeaker: Please follow all the rules and have a great time here.\nIn order to get DM's from our bot <@926163269503299695> please allow DM's on this server."
        )
        
        if str(user) == str(userName):
            await interaction.response.send_message("Success, Welcome to A Weeb's Hangout!", ephemeral= True)
            await user.add_roles(verified)
            await user.remove_roles(unverified)
            await logsChannel.send(embed=logsEmbed)
            await welcomeChannel.send(embed=embed)
        else:
            await interaction.response.send_message("'/verify' and enter your discord name and tag. e.g. Name#1234", ephemeral= True)
            
async def setup(bot):
    await bot.add_cog(verfiy(bot), guilds=[discord.Object(id=860752406551461909)])