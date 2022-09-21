import discord
from discord import app_commands
from discord.ext import commands


class joinleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `joinleave.py`")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #welcomeChannel = self.bot.get_channel(865681786877378630)
        logsChannel = self.bot.get_channel(865073673668526080)
        embed = discord.Embed(
            title=f'Welcome {member} to the server.',
            color=discord.Color.green(),
            description=":loudspeaker: Please follow all the rules and have a great time here.\nIn order to get DM's from our bot <@926163269503299695> please allow DM's on this server."
        )
        logsEmbed = discord.Embed(
            title=f'{member} joined the server',
            color=discord.Color.green()
        )
        unverified = self.bot.guild.get_role(1022172788460625951)
        await member.add_roles(unverified)
        #await welcomeChannel.send(embed=embed)
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