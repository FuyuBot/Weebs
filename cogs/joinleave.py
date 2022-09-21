import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get


class joinleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `joinleave.py`")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logsChannel = self.bot.get_channel(865073673668526080)
        logsEmbed = discord.Embed(
            title=f'{member} joined the server',
            color=discord.Color.green()
        )
        unverified = discord.utils.get(member.guild.roles, name="unverified")
        await member.add_roles(unverified)
        await logsChannel.send(embed=logsEmbed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logsChannel = self.bot.get_channel(865073673668526080)
        embed = discord.Embed(
            title=f'{member} has left the server.',
            color=discord.Color.green()
        )
        await logsChannel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(joinleave(bot))