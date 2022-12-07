import discord
from discord.ext import commands
import requests
import config
import pymongo

moderatorLogs = 865078390109634590
otherLogs = 865073269811052621
memberLogs = 865073582908768266
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
# create
# delete
# edit
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if self.bot.guild.id != 860752406551461909:
            return 
        try:
            embed = discord.Embed(color=0x2699C6)
            embed.set_author(name=message.author, icon_url=message.author.avatar)
            embed.add_field(name=f'Messaged Deleted in #{message.channel.name}', value=message.content)
            embed.set_footer(text=f"User's ID: {message.author.id}, Created at: {message.created_at}")
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        if self.bot.guild.id != 860752406551461909:
            return
        try:
            for msg in messages:
                embed = discord.Embed(color=0x2699C6)
                embed.set_author(name=messages.author, icon_url=messages.author.avatar)
                embed.add_field(name=f'Messaged Deleted in #{messages.channel.name}', value=msg.content)
                embed.set_footer(text=f"User's ID: {messages.author.id}, Created at:{messages.created_at}")
                messageLogsChannel = self.bot.get_channel(messageLogs)
                await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if self.bot.guild.id != 860752406551461909:
            return
        try:
            embed = discord.Embed(title=f'Messaged edited in #{before.channel.name}',color=0x2699C6, description=f"**Before:** {before.content}\n**+After:** {after.content}")
            embed.set_author(name=before.author, icon_url=before.author.avatar)
            embed.set_footer(text=f"User's ID: {before.author.id}")
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
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



async def setup(bot):
    await bot.add_cog(logs(bot), guilds=[discord.Object(id=860752406551461909)])