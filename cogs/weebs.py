import discord
from discord import app_commands
from discord.ext import commands
import config
import pymongo
import TOKEN

myclient = pymongo.MongoClient(TOKEN.mongoDB)
mydb = myclient['WeebsHangout']
mycol = mydb["user_info"]


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
        staffEmbed = discord.Embed(title=f"Staff Team Roles",color=config.color, description="\
            <@&860758013731274762> - This role is given to all of the people managing the server keeping it updated and running smoothly.\n\
            <@&860757939618316298> - This role is given to the Owner of the server.\n\
            <@&860757995171610628> - This role is given to the Managers on the server managing the area they have been assigned to.\n\
            <@&865727062374744064> - This role is given to the Developers on the server in charge of creating and managing our server's bot.\n\
            <@&860758015011586069> - This role is given to the Administrators who are the highest level of moderation with extra responsibilities.\n\
            <@&860758015585812480> - This role is given to our Senior Moderators who are the second highest level of moderation and primarily help\
            with dealing with tickets and other issues that might come up.\n\
            <@&860758015959498763> - This role is given to our Moderators who deal with most of the moderating on the server.\n\
            <@&860758016618266624><@&860758016764936193> - These roles are given to our Trial Helpers and Helpers who help with\
                managing the chats on the server.\n\
            <@&895490315174178857> - Users with this role are extremely close with the management team and help test new features for the server.\n\
            <@&1041796871892516874> - Stream/channel moderators of <@920797181034778655>'s channels.")
        twitchEmbed = discord.Embed(title=f"Twitch Roles", color=config.color, description="\
            <@&1041791871913046137> - This role is given to those who subscribe to <@920797181034778655> on twitch. This role doesn't give any extra perks just a channel.")
        generalEmbed = discord.Embed(title=f"General Roles",color=config.color, description="\
            <@&865727063327768618> - People wanted a role saying they are not a weeb.\n\
            <@&910929581605789718> - Gives you access to all of the Genshin Impact channels here on the server.\n\
            <@&865050483189219338> - You can get this role to be pinged when we have announcements on the server.\n\
            <@&865050484506886164> - You can get this role to be pinged when we are adding new things to the server.\n\
            <@&1053016537994362890> - You can get this role to be pinged when we are doing events on the server.\n\
            <@&927774106554884156> - You can get this role to gain access to <#1020393781117341716> which posts updates everyday about new anime episodes for that day.\n\
            <@&865430630987857921> - <@920797181034778655> does stream from time to time, if you want to be notifed when he is live feel free to get this role.\n\
            <@&1022724072792129547> - This role is given to the users that boost the server.")
        generalEmbed.set_footer(text="Obtain by doing /roles in any channel.")
        levelsEmbed = discord.Embed(color=config.color, description="These are the message requirement roles on the server:\n\
            <@&1034276484556275742> - 1,000,000+ Messages\n\
            <@&1034276120876548126> - 500,000 Messages\n\
            <@&865430631944290334> - 100,00 Messages\n\
            <@&865727060172603433> - 50,000 Messages\n\
            <@&865727060861386792> - 10,000 Messages\n")
        faqEmbed = discord.Embed(color=config.color, description="Frequently Asked Questions:\n\
            Q: How can I apply to become a staff member?\n\
            A: `/apply` in any channel.\n\n\
            Q: Who can see my application?\n\
            A: Only members of the Management Team.\n\n\
            Q: If I have a question about the application/application process what do I do?\n\
            A: Make a staff app ticket with `/ticket` in any channel.\n\n\
            Q: How can I get more roles on the server?\n\
            A: Use the command `/roles` in any channel.\n\n\
            Q: How do I report someone?\n\
            A: Make a report ticket with `/ticket` in any channel.\n\n\
            Q: How can I contact staff?\n\
            A: Make a ticket with `/ticket` in any channel.\n\n\
            Q: How can I fund/start a giveaway?\n\
            A: Make a giveaway ticket with `/ticket` in any channel.")
            
        try:
            await sendChannel.send(embed=initialEmbed)
            await sendChannel.send(embed=staffEmbed)
            await sendChannel.send(embed=twitchEmbed)
            await sendChannel.send(embed=generalEmbed)
            await sendChannel.send(embed=levelsEmbed)
            await sendChannel.send(embed=faqEmbed)
            await interaction.response.send_message("Sent successfully!", ephemeral=True)
        except Exception as e:
            print(e)
    @app_commands.command(name="genshin-information", description="This command sends the Genshin information into a specified channel.")
    @app_commands.checks.has_any_role("Management Team")
    async def genshinInformation(self, interaction: discord.Interaction, channel: discord.TextChannel):
        sendChannel = interaction.client.get_channel(channel.id)
        initialEmbed = discord.Embed(color=config.color, description="\
            Hello and welcome Genshin community to A Weeb's hangout.\n\n\
                I hope you like our Genshin Impact area of the server! We have lots of things that\
                you can use here as well as lots of announcements from the official Genshin Impact server. If you have any questions regarding things related\
            feel free to make a ticket using `/ticket` or ask a staff member and they should be able to help you. Although if your question is related\
                to Genshin I would probably ask someone that has the Genshin Impact role. If you are requesting the AR 60 roles please make a General ticket. with `/ticket`.")
        genshinEmbed = discord.Embed(color=config.color, description="World levels and Adventure Rank 60:\n\
            <@&1036071298272604291> - Users who are Adventurer Rank 60\n\
            <@&1036071227376271390> - Users who have world level 8\n\
            <@&1036071267444461641> - Users who have world level 7\n\
            <@&1036071270858620938> - Users who have world level 6\n\
            <@&1036071272477642782> - Users who have world level 5\n\
            <@&1036071279737982996> - Users who have world level 4\n\
            <@&1036071285404487720> - Users who have world level 3\n\
            <@&1036071289925931008> - Users who have world level 2\n")
        genshinEmbed.set_footer(text="Obtain by doing /genshin-roles. ")
        
        await sendChannel.send(embed=initialEmbed)
        await sendChannel.send(embed=genshinEmbed)
        await interaction.response.send_message("Sent successfully!", ephemeral=True)

    @app_commands.command(name="rtj-information", description="Sends the information regarding RTJ in the channel specified.")
    @app_commands.checks.has_any_role("Management Team")
    async def rtjinformation(self, interaction: discord.Interaction, channel: discord.TextChannel):
        sendChannel = interaction.client.get_channel(channel.id)
        embed=discord.Embed(color=config.color,description=f'`/request-to-join` to get started.\n\n\
            This command will prompt you to put your Genshin name, world level, and finally why you are requesting to join.\n\
            The reasons to request to join could be things like "Nahida\'s flowers", "Shimenawa Domain", etc just please make it clear of\
            what you are requesting.')
        
        await sendChannel.send(embed=embed)
        await interaction.response.send_message(f"Sent successfully", ephemeral=True)
async def setup(bot):
    await bot.add_cog(weebs(bot), guilds=[discord.Object(id=config.weebsHangout)])