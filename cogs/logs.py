import discord
from discord.ext import commands
import config
import pymongo
from datetime import datetime

moderatorLogs = 865078390109634590
otherLogs = 865073269811052621
memberLogs = 1058040014912634880
serverLogs = 865073601832157214
voiceLogs = 865073623073292369
messageLogs = 865073643553423360
imageLogs = 1023932277442490458
joinLeaveLogs = 865073673668526080
ticketLogs = 1022980124909518898
eventLogs = 1024365047633424404

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]

class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `logs.py`")
################################
######## MESSAGE EVENTS ########
################################
# delete
# edit
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.id == 865058528913784852:
            return
        try:
            embed = discord.Embed(color=config.color, timestamp=datetime.now())
            embed.set_author(name=message.author, icon_url=message.author.avatar)
            embed.add_field(name=f'Messaged Deleted in #{message.channel.name}', value=message.content)
            embed.set_footer(text=f"ID: {message.author.id}")
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print("Error in on_message_delete")
            print(e)
    
    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        try:
            embed = discord.Embed(color=config.color, timestamp=datetime.now())
            embed.add_field(name=f'Messaged Deleted', value=len(messages))
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print("Error in on_bulk_message_delete")
            print(e)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        ########## WEEBS BOT ########## MUDAE BOT ######## GALAXY.BOT ######## KATHERYNE ######## BUMP REMINDER BOT ## DISBOARD BOT ##### GIVEAWAY BOT ####### POKETWO BOT ####### QOTD BOT ######### SEASONAL ANIME BOT ### TOP.GG BOT ####
        botIDs = [926163269503299695, 432610292342587392, 820031583419367425, 774806286051049504, 735147814878969968, 302050872383242240, 294882584201003009, 716390085896962058, 713586207119900693, 614495694769618944, 422087909634736160]
        ############## MANAGEMENT TEAM ###### MESSAGE LOGS
        channelIDs = [865058528913784852, 865073643553423360]
        if before.author.id in botIDs:
            return
        if before.channel.id in channelIDs:
            return
        
        try:
            embed = discord.Embed(title=f'Messaged edited in #{before.channel.name}',color=config.color, description=f"**Before:** {before.content}\n**+After:** {after.content}", timestamp=datetime.now())
            embed.set_author(name=before.author, icon_url=before.author.avatar)
            embed.set_footer(text=f"ID: {before.author.id}")
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print("Error in on_message_edit")
            print(e)
    
#### UPDATE DB
    @commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User):
        player = before.id
        nameAfter = after.name
        tagAfter = after.discriminator
        playerDB = mycol.find_one({"_id": player})
        tag = playerDB['info']['tag']
        if tag != tagAfter:
            mycol.update_one({'_id': player}, {"$set": {"info.name": nameAfter}})
            mycol.update_one({'_id': player}, {"$set": {"info.tag": tagAfter}})
        else:
            mycol.update_one({'_id': player}, {"$set": {"info.name": nameAfter}})

#### User upadte
    @commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User):
        memberLog = self.bot.get_channel(memberLogs)
        try:
            if after.name != before.name:
                embed = discord.Embed(color=config.color, title="Username has changed", description=before.mention, timestamp=datetime.now())
                embed.add_field(name="Before", value=before.name, inline=True)
                embed.add_field(name="After", value=after.name, inline=True)
                embed.set_author(name=before, icon_url=before.avatar)
                embed.set_footer(text=f"ID: {before.id}")
                await memberLog.send(embed=embed)
            if after.discriminator != before.discriminator:
                embed = discord.Embed(color=config.color, title="Discriminator has changed", description=before.mention, timestamp=datetime.now())
                embed.add_field(name="Before", value=before.discriminator, inline=True)
                embed.add_field(name="After", value=after.discriminator, inline=True)
                embed.set_author(name=before, icon_url=before.avatar)
                embed.set_footer(text=f"ID: {before.id}")
                await memberLog.send(embed=embed)
            if after.avatar != before.avatar:
                embed = discord.Embed(color=config.color, title="Avatar has changed", description=before.mention, timestamp=datetime.now())
                embed.set_thumbnail(url=after.avatar)
                embed.set_author(name=before, icon_url=before.avatar)
                embed.set_footer(text=f"ID: {before.id}")
                await memberLog.send(embed=embed)
        except Exception as e:
            print(e)
            print("Error in on_user_update")

#### Member Update
    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        memberLog = self.bot.get_channel(memberLogs)
        try:
            if after.nick != before.nick:
                embed = discord.Embed(color=config.color, title="Username has changed", description=before.mention, timestamp=datetime.now())
                embed.add_field(name="Before", value=before.nick, inline=True)
                embed.add_field(name="After", value=after.nick, inline=True)
                embed.set_author(name=before, icon_url=before.avatar)
                embed.set_footer(text=f"ID: {before.id}")
            if after.guild_avatar != before.guild_avatar:
                embed = discord.Embed(color=config.color, title="Guild Avatar has changed", description=before.mention, timestamp=datetime.now())
                embed.set_thumbnail(url=after.guild_avatar)
                embed.set_author(name=before, icon_url=before.guild_avatar)
                embed.set_footer(text=f"ID: {before.id}")
                await memberLog.send(embed=embed)
            #print(before.roles)
            if len(before.roles) < len(after.roles):
                newRole = next(role for role in after.roles if role not in before.roles)
                embed = discord.Embed(color=config.color, title="Role Added", description=newRole.mention, timestamp=datetime.now())
                embed.set_author(name=before, icon_url=before.avatar)
                embed.set_footer(text=f"ID: {before.id}")
                await memberLog.send(embed=embed)
            if len(before.roles) > len(after.roles):
                oldRole = next(role for role in before.roles if role not in after.roles)
                embed = discord.Embed(color=config.color, title="Role Removed", description=oldRole.mention, timestamp=datetime.now())
                embed.set_author(name=before, icon_url=before.avatar)
                embed.set_footer(text=f"ID: {before.id}")
                await memberLog.send(embed=embed)
        except Exception as e:    
            print(e)
            print("Error in on_member_update")
async def setup(bot):
    await bot.add_cog(logs(bot), guilds=[discord.Object(id=860752406551461909)])