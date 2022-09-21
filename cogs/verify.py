import discord
from discord import app_commands
from discord.ext import commands

class VerifyModal(discord.ui.Modal, title="Verify"):
    verification = discord.ui.TextInput(label="Name", placeholder="Enter your Name and Tag here...")
    async def on_submit(self, interaction: discord.Interaction):
        user = interaction.user
        print(f"`{self.verification}`")
        print(f"`{interaction.user.name}`")
        if interaction.user.name in self.verification:
            verified = discord.utils.get(user.guild.roles, name="Member")
            unverified = discord.utils.get(user.guild.roles, name="unverified")
            logsChannel = self.bot.get_channel(865073673668526080)
            logsEmbed = discord.Embed(
                title=f'{user} Verified.',
                color=discord.Color.green()
            )
            await user.add_roles(verified)
            await user.remove_roles(unverified)
            await logsChannel.send(embed=logsEmbed)


class verfiy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `verify.py`")

    @app_commands.command(name='verify', description='Verify that you are a human.')
    async def verify(self, interaction:discord.Interaction):
        await interaction.response.send_modal(VerifyModal())

async def setup(bot):
    await bot.add_cog(verfiy(bot), guilds=[discord.Object(id=860752406551461909)])

