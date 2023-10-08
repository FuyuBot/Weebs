import discord
from discord import app_commands
from discord.ext import commands
import config
import pymongo
from datetime import datetime
import TOKEN

myclient = pymongo.MongoClient(TOKEN.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]

seniorstaff = 865054271857885225
managementTeam = 860758013731274762
staffTeam = 860758014386896926
member = 860757567566774322

class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `members.py`")

    @app_commands.command(name='member', description="Check someone's information")
    async def member(self, interaction: discord.Interaction, user: discord.Member):
        player = user.id
        playerDB = mycol.find_one({"_id": player})
        msgNum = playerDB['info']['messages']
        embed = discord.Embed(color=config.color)
        
        embed.set_author(name=f"{user}", icon_url=user.avatar)
        embed.add_field(name="Joined:", value=user.joined_at, inline=False)
        embed.add_field(name="Account Created:", value=user.created_at, inline=False)
        embed.add_field(name="Server Nickname", value=user.nick)
        embed.add_field(name="Messages Sent:", value=msgNum)
        embed.add_field(name="ID:", value=user.id)
        embed.set_footer(text=config.footer)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='avatar', description="Get a users avatar.")
    async def avatar(self, interaction: discord.Interaction, user: discord.Member):
        avatar = user.avatar
        
        embed=discord.Embed(color=config.color)
        embed.set_image(url=avatar)
        await interaction.response.send_message(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        player = message.author.id
        member = message.author
        playerDB = mycol.find_one({"_id": player})
        mycol.update_one({"_id": player}, {"$inc": {"info.messages": 1}})
        msgNum = playerDB['info']['messages']
        roleReq = [10000, 50000, 100000, 500000, 1000000]

        role1 = discord.utils.get(member.guild.roles, id=865727060861386792)
        role2 = discord.utils.get(member.guild.roles, id=865727060172603433)
        role3 = discord.utils.get(member.guild.roles, id=865430631944290334)
        role4 = discord.utils.get(member.guild.roles, id=1034276120876548126)
        role5 = discord.utils.get(member.guild.roles, id=1034276484556275742)
        
        if msgNum in roleReq:
            if msgNum == roleReq[0]:
                await member.add_roles(role1)
                return await member.send(f"{member} congradulations, you have received the first message reward role.")
            elif msgNum == roleReq[1]:
                await member.add_roles(role2)
                return await member.send(f"{member} congradulations, you have received the second message reward role.")
            elif msgNum == roleReq[2]:
                await member.add_roles(role3)
                return await member.send(f"{member} congradulations, you have received the third message reward role.")
            elif msgNum == roleReq[3]:
                await member.add_roles(role4)
                return await member.send(f"{member} congradulations, you have received the fourth message reward role.")
            elif msgNum == roleReq[4]:
                await member.add_roles(role5)
                return await member.send(f"{member} congradulations, you have received the fifth and final message reward role.")
        else:
            return
    
    @app_commands.command(name="messages", description="Show how many messages you have sent in the server.")
    async def messages(self, interaction: discord.Interaction, user: discord.Member=None):
        member = interaction.user
        roleReq = [10000, 50000, 100000, 500000, 1000000]

        role1 = discord.utils.get(member.guild.roles, id=865727060861386792)
        role2 = discord.utils.get(member.guild.roles, id=865727060172603433)
        role3 = discord.utils.get(member.guild.roles, id=865430631944290334)
        role4 = discord.utils.get(member.guild.roles, id=1034276120876548126)
        role5 = discord.utils.get(member.guild.roles, id=1034276484556275742)
        if user == None:
            player = interaction.user.id
            playerDB = mycol.find_one({"_id": player})
            msgNum = playerDB['info']['messages']
        
            if msgNum < roleReq[0]:
                msgLeft = roleReq[0] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"You currently have **{msgNum}** messages.\n\nYou need `{msgLeft} more messages to get {role1.mention}")
            elif msgNum > roleReq[0] and msgNum < roleReq[1]:
                msgLeft = roleReq[1] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"You currently have **{msgNum}** messages.\n\nYou need `{msgLeft} more messages to get {role2.mention}")
            elif msgNum > roleReq[1] and msgNum < roleReq[2]:
                msgLeft = roleReq[2] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"You currently have **{msgNum}** messages.\n\nYou need `{msgLeft} more messages to get {role3.mention}")
            elif msgNum > roleReq[2] and msgNum < roleReq[3]:
                msgLeft = roleReq[3] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"You currently have **{msgNum}** messages.\n\nYou need `{msgLeft} more messages to get {role4.mention}")
            elif msgNum > roleReq[3] and msgNum < roleReq[4]:
                msgLeft = roleReq[4] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"You currently have **{msgNum}** messages.\n\nYou need `{msgLeft} more messages to get {role5.mention}")

            return await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            player = user.id
            member = user
            playerDB = mycol.find_one({"_id": player})
            msgNum = playerDB['info']['messages']
        
            if msgNum < roleReq[0]:
                msgLeft = roleReq[0] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"They currently have **{msgNum}** messages.")
            elif msgNum > roleReq[0] and msgNum < roleReq[1]:
                msgLeft = roleReq[1] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"They currently have **{msgNum}** messages.")
            elif msgNum > roleReq[1] and msgNum < roleReq[2]:
                msgLeft = roleReq[2] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"They currently have **{msgNum}** messages.")
            elif msgNum > roleReq[2] and msgNum < roleReq[3]:
                msgLeft = roleReq[3] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"They currently have **{msgNum}** messages.")
            elif msgNum > roleReq[3] and msgNum < roleReq[4]:
                msgLeft = roleReq[4] - msgNum
                embed = discord.Embed(color=config.color, title=f"{member}'s messages", description=f"They currently have **{msgNum}** messages.")

            return await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(name="message-leaderboard", description="Displays the message leaderboard for everyone in the server.")
    async def msgLeaderboard(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(title="Message Leaderboard", color=config.color)
            playerDB = mycol.find().sort([("info.messages", -1),]).limit(10)
            count = 0
            for x in playerDB:
                count += 1
                user = self.bot.get_user(int(x['_id']))
                msgs = x['info']['messages']
                embed.add_field(name=f"{count}. {user.name}", value=f"**{msgs}** messages", inline=False) 
            return await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(members(bot), guilds=[discord.Object(id=860752406551461909)])