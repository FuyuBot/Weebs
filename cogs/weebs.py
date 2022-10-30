import discord
from discord import app_commands
from discord.ext import commands
import config

class weebs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Welcome
    # Staff Roles
    # General Roles
    # Leveling Roles
    # Staff Team

    @app_commands.command(name="information", description="This will send the Information embeds to the information channel.")
    @app_commands.checks.has_any_role("Management Team")
    async def information(self, interaction: discord.Interaction, channel: discord.TextChannel):
        sendChannel = interaction.client.get_channel(channel.id)
        initialEmbed = discord.Embed(title='Information', color=config.color,description="Hello and welcome to A Weeb's Hangout!\n\n\
            Hey, Jacob here would like to personally welcome everyone to this server and I really hope you enjoy being in the server. I want this to\
                be a place where everyone can talk about their anime interests and whatever else they want to talk about.")
        staffEmbed = discord.Embed(color=config.color, description="\
            <@&860758013731274762> - This role is given to all of the people managing the server keeping it updated and running smoothly.\n\
            <@&860757939618316298> - This role is given to the Owner of the server.\n\
            <@&860757995171610628> - This role is given to the Managers on the server managing the area they have been assigned to.\n\
            <@&865727062374744064> - This role is given to the Developers on the in charge of creating and managing our server's bot.\n\
            <@&860758015011586069> - This role is given to the Administrators who are the highest level of moderation with extra responsibilities.\n\
            <@&860758015585812480> - This role is given to our Senior Moderators and they are the second highest level of moderation and primarily help\
            with dealing with tickets and other issues that might come up.\n\
            <@&860758015959498763> - This role is given to our Moderators and they deal with most of the moderating on the server.\n\
            <@&860758016618266624><@&860758016764936193> - These roles are given to our Trial Helpers and Helpers and they help with\
                managing the chats on the server.\n\
            <@&895490315174178857> - Users with this role are extremely close with the Management team and help with testing new features for the server.")
        generalEmbed = discord.Embed(color=config.color, description="\
            <@&860757567566774322> - This the role everyone will have.\n\
            <@&865727063327768618> - People wanted a role saying they are not a weeb.\n\
            <@&910929581605789718> - Gives you access to all of the Genshin Impact channels here on the server.\n\
            <@&865430630987857921> - <@920797181034778655> does stream from time to time, if you want to be notifed when he is life feel free to get this role.\n\
            <@&1022724072792129547> - This role is given to the users that boost the server.")
        levelsEmbed = discord.Embed(color=config.color, description="These are the message requirement roles on the server:\n\
            <@&1034276484556275742> - 1,000,000+ Messages\n\
            <@&1034276120876548126> - 500,000 Messages\n\
            <@&865430631944290334> - 100,00 Messages\n\
            <@&865722681139527681> - 50,000 Messages\n\
            <@&865727060172603433> - 10,000 Messages\n")
        genshinEmbed = discord.Embed(color=config.color, description="Our roles related to Genshin Impact:\n\
            <@&1036071298272604291> - Users who are Adventurer Rank 60\n\
            <@&1036071227376271390> - Users who have world level 8\n\
            <@&1036071267444461641> - Users who have world level 7\n\
            <@&1036071270858620938> - Users who have world level 6\n\
            <@&1036071272477642782> - Users who have world level 5\n\
            <@&1036071279737982996> - Users who have world level 4\n\
            <@&1036071285404487720> - Users who have world level 3\n\
            <@&1036071289925931008> - Users who have world level 2\n")
            

        await sendChannel.send(embed=initialEmbed)
        await sendChannel.send(embed=staffEmbed)
        await sendChannel.send(embed=generalEmbed)
        await sendChannel.send(embed=levelsEmbed)
        #await sendChannel.send(embed=genshinEmbed)

async def setup(bot):
    await bot.add_cog(weebs(bot), guilds=[discord.Object(id=config.weebsHangout)])