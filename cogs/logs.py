import discord
from discord.ext import commands
import requests



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
        try:
            embed = discord.Embed(color=0x2699C6)
            embed.set_author(name=message.author, icon_url=message.author.avatar)
            embed.add_field(name=f'Messaged Deleted in #{message.channel.name}', value=message.content)
            embed.set_footer(text=f"User's ID: {message.author.id} {message.created_at}")
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            embed = discord.Embed(title=f'Messaged edited in #{before.channel.name}',color=0x2699C6, description=f"**Before:** {before.content}\n**+After:** {after.content}")
            embed.set_author(name=before.author, icon_url=before.author.avatar)
            embed.set_footer(text=f"User's ID: {before.author.id}")
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
################################
######## CHANNEL EVENTS ########
################################
# create
# delete
# update
# thread create
# thread delete
# thread update
# stage create
# stage delete
# state update
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        try:
            embed=discord.Embed(title="Channel created", color=0x2699C6)
            embed.add_field(name="Channel name", value=channel.name)
            embed.add_field(name="Created at", value=channel.created_at)
            embed.add_field(name="Permissions", value=channel.overwrites)
            embed.add_field(name="Permissions Synced", value=channel.permissions_synced)
            embed.url(url=channel.jump_url)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        try:
            embed=discord.Embed(title="Channel deleted", color=0x2699C6)
            embed.add_field(name="Channel name", value=channel.name)
            embed.add_field(name="Created at", value=channel.created_at)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        try:
            embed=discord.Embed(title="Channel deleted", color=0x2699C6)
            embed.add_field(name="Channel name before", value=before.name, inline=True)
            embed.add_field(name="Channel name after", value=before.name, inline=True)
            embed.add_field(name="Permissions", value=before.overwrites)
            embed.add_field(name="Permissions", value=after.overwrites)
            embed.add_field(name="Created at", value=before.created_at, inline=False)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        try:
            embed=discord.Embed(title=f"Thread created `{thread.name}`", color=0x2699C6, description=f"Thread ID: {thread.id}")
            embed.set_author(name=thread.owner, icon_url=thread.owner.avatar)
            embed.add_field(name="Parent channel", value=f"{thread.parent}\n{thread.parent_id}")
            embed.add_field(name="Flags", value=thread.flags)
            embed.set_footer(text=f"Owner ID: {thread.owner_id}")
            embed.url(url=thread.jump_url)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_thread_delete(self, thread):
        try:
            embed=discord.Embed(title=f"Thread deleted `{thread.name}`", color=0x2699C6, description=f"Thread ID: {thread.id}")
            embed.set_author(name=thread.owner, icon_url=thread.owner.avatar)
            embed.add_field(name="Parent channel", value=f"{thread.parent}\n{thread.parent_id}")
            embed.set_footer(text=f"Owner ID: {thread.owner_id}")
            embed.url(url=thread.jump_url)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_thread_update(self, before, after):
        try:
            embed=discord.Embed(title=f"Thread Updated `{before.name}`", color=0x2699C6, description=f"Name Before: {before.name}\n\
                Name After: {after.name}\n\nThread ID: {before.id}")
            embed.set_author(name=before.owner, icon_url=before.owner.avatar)
            embed.add_field(name="Owner Before", value=before.owner)
            embed.add_field(name="Owner After", value=after.owner)
            embed.add_field(name="Parent channel", value=f"{before.parent}\n{before.parent_id}")
            embed.set_footer(text=f"Owner ID: {before.owner_id}")
            embed.url(url=before.jump_url)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_stage_instance_create(self, stage_instance):
        try:
            embed=discord.Embed(title=f"Stage created", color=0x2699C6, description=f"The topic of the Stage is {stage_instance.topic}")
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.add_field(name="Privacy Level", value=stage_instance.privacy_level)
            embed.set_footer(text=f"Channel ID: {stage_instance.id}")

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_stage_instance_delete(self, stage_instance):
        try:
            embed=discord.Embed(title=f"Stage deleted", color=0x2699C6, description=f"The topic of the Stage was {stage_instance.topic}")
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.add_field(name="Privacy Level", value=stage_instance.privacy_level)
            embed.set_footer(text=f"Channel ID: {stage_instance.id}")

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_stage_instance_update(self, before, after):
        try:
            embed=discord.Embed(title=f"Stage updated", color=0x2699C6, description=f"Topic before: {before.topic}\nTopic after: {after.topic}")
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.add_field(name="Privacy Level Before", value=before.privacy_level)
            embed.add_field(name="Privacy Level After", value=after.privacy_level)
            embed.set_footer(text=f"Channel ID: {before.id}")

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

#############################
######## ROLE EVENTS ########
#############################
# create
# delete
# update
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=event#roles
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        # color
        # created_at
        # hoist * bool
        # id
        # managed * bool
        # mentionable
        # name
        # 
        hexURL = f'https://www.thecolorapi.com/id?hex={role.color}'
        hexGET = requests.get(hexURL)
        try:
            return
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        try:
            return
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        try:
            return
        except Exception as e:
            print(e)

##################################
######## SCHEDULED EVENTS ########
##################################
# create
# delete
# update
# user add
# user remove

##############################
######## GUILD EVENTS ########
##############################
# update
# emoji update
# stickers update

###############################
######## MEMBER EVENTS ########
###############################
# member update
# - nickname
# - roles
# - guild avatar
# user update
# - avatar
# - username
# - discriminator

##################################
######## EXTRA MOD EVENTS ########
##################################
# automod rule create
# automod rule update
# automod rule delete
# automod action

##################################
######## INTEGRATION EVENTS ########
##################################
# create
# update
# delete
# webhook update

async def setup(bot):
    await bot.add_cog(logs(bot))


#@commands.Cog.listener()
#    async def on_invite_create(self, invite):
#        try:
#            if invite.temporary == True:
#                embed = discord.Embed(title='Temporary Invite Created', color=0x2699C6)
#                embed.set_author(name=invite.inviter, icon_url=invite.inviter.avatar)
#                embed.add_field(name="Created at", value=invite.created_at)
#                embed.add_field(name="Expires at", value=invite.expires_at)
#                embed.add_field(name="Max Uses", value=invite.max_uses)
#                embed.add_field(name="Current Uses", value=invite.uses)
#                embed.set_footer(text=f"User ID: {invite.inviter.id}, URL: {invite.url}")
#                messageLogsChannel = self.bot.get_channel(865073643553423360)
#                await messageLogsChannel.send(embed=embed)
#            else:
#                embed = discord.Embed(title='Permanent Invite Created', color=0x2699C6)
#                embed.set_author(name=invite.inviter, icon_url=invite.inviter.avatar)
#                embed.add_field(name="Created at", value=invite.created_at)
#                embed.add_field(name="Max Uses", value=invite.max_uses)
#                embed.add_field(name="Current Uses", value=invite.uses)
#                embed.set_footer(text=f"User ID: {invite.inviter.id}, URL: {invite.url}")
#                messageLogsChannel = self.bot.get_channel(865073643553423360)
#                await messageLogsChannel.send(embed=embed)
#        
#        except Exception as e:
#            print(e)