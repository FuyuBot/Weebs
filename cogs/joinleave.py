import discord
from discord.ext import commands


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
        logsEmbed.set_footer(text=f"ID: {member.id}")
        logsEmbed.set_footer(text=f"ID: {member.id}")
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
        embed.set_footer(text=f"ID: {member.id}")
        embed.set_footer(text=f"ID: {member.id}")
        await logsChannel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(joinleave(bot), guilds=[discord.Object(id=860752406551461909)])