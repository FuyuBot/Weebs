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
            embed.set_footer(text=f"User's ID: {message.author.id}, Created at: {message.created_at}")
            messageLogsChannel = self.bot.get_channel(messageLogs)
            await messageLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
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
            embed=discord.Embed(title=f"Thread Updated `{before.name}`", color=0x2699C6, description=f"Name before: {before.name}\n\
                Name after: {after.name}\n\nThread ID: {before.id}")
            embed.set_author(name=before.owner, icon_url=before.owner.avatar)
            embed.add_field(name="Owner before", value=before.owner)
            embed.add_field(name="Owner after", value=after.owner)
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
            embed=discord.Embed(title=f"Stage created", color=0x2699C6, description=f"The topic of the stage is {stage_instance.topic}")
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.add_field(name="Privacy level", value=stage_instance.privacy_level)
            embed.set_footer(text=f"Channel ID: {stage_instance.id}")

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_stage_instance_delete(self, stage_instance):
        try:
            embed=discord.Embed(title=f"Stage deleted", color=0x2699C6, description=f"The topic of the stage was {stage_instance.topic}")
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.add_field(name="Privacy level", value=stage_instance.privacy_level)
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
        hexURL = f'https://www.thecolorapi.com/id?hex={role.color}'
        hexGET = requests.get(hexURL)
        hexIMAGE = hexGET.json()['image']['name']
        try:
            embed=discord.Embed(title="Role created", color=0x2699C6, description=f"Name: {role.name}")
            embed.set_thumbnail(url=hexIMAGE)
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.set_footer(text=f"Role ID: {role.id} | Created at: {role.created_at}")
            if role.hoist == True:
                embed.add_field(name="Hoisted?", value="✅")
            else:
                embed.add_field(name="Hoisted?", value="❎")
            if role.managed == True:
                embed.add_field(name="Managed by an Integration?", value="✅")
            else:
                embed.add_field(name="Managed by an Integration?", value="❎")
            if role.mentionable == True:
                embed.add_field(name="Mentionable?", value="✅")
            else:
                embed.add_field(name="Mentionable?", value="❎")
            
            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        try:
            embed=discord.Embed(title="Role deleted", color=0x2699C6, description=f"Name: {role.name}")
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.set_footer(text=f"Role ID: {role.id} | Created at: {role.created_at}")
            if role.hoist == True:
                embed.add_field(name="Hoisted?", value="✅")
            else:
                embed.add_field(name="Hoisted?", value="❎")
            if role.managed == True:
                embed.add_field(name="Managed by an Integration?", value="✅")
            else:
                embed.add_field(name="Managed by an Integration?", value="❎")
            if role.mentionable == True:
                embed.add_field(name="Mentionable?", value="✅")
            else:
                embed.add_field(name="Mentionable?", value="❎")
            
            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        hexURL = f'https://www.thecolorapi.com/id?hex={after.color}'
        hexGET = requests.get(hexURL)
        hexIMAGE = hexGET.json()['image']['name']
        try:
            embed=discord.Embed(title="Role created", color=0x2699C6, description=f"Name before: {before.name}\nName after: {after.name}")
            embed.set_thumbnail(url=hexIMAGE)
            embed.set_author(name=self.bot, icon_url=self.bot.avatar)
            embed.set_footer(text=f"Role ID: {before.id} | Created at: {before.created_at}")
            if before.hoist == True:
                embed.add_field(name="Hoisted?", value="✅")
            else:
                embed.add_field(name="Hoisted?", value="❎")
            if after.hoist == True:
                embed.add_field(name="Hoisted?", value="✅")
            else:
                embed.add_field(name="Hoisted?", value="❎")
            if before.managed == True:
                embed.add_field(name="Managed by an Integration?", value="✅")
            else:
                embed.add_field(name="Managed by an Integration?", value="❎")
            if after.managed == True:
                embed.add_field(name="Managed by an Integration?", value="✅")
            else:
                embed.add_field(name="Managed by an Integration?", value="❎")
            if before.mentionable == True:
                embed.add_field(name="Mentionable?", value="✅")
            else:
                embed.add_field(name="Mentionable?", value="❎")
            if after.mentionable == True:
                embed.add_field(name="Mentionable?", value="✅")
            else:
                embed.add_field(name="Mentionable?", value="❎")
            
            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
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
    @commands.Cog.listener()
    async def on_scheduled_event_create(self, event):
        try:
            embed=discord.Embed(title="Event created", color=0x2699C6, description=f"Name of the event: {event.name}\n\
                Description of the event: {event.description}")
            embed.set_author(name=event.creator, icon_url=event.creator.avatar)
            if event.cover_image is not None:
                embed.set_image(url=event.cover_image)
            else:
                pass
            embed.add_field(name="Privacy level", value=event.privacy_level)
            embed.add_field(name="Start time", value=event.start_time)
            embed.add_field(name="End time", value=event.end_time)
            embed.url(url=event.url)
            
            eventsLogsChannel = self.bot.get_channel(eventLogs)
            await eventsLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_scheduled_event_delete(self, event):
        try:
            embed=discord.Embed(title="Event deleted", color=0x2699C6, description=f"Name of the event: {event.name}\n\
                Description of the event: {event.description}")
            embed.set_author(name=event.creator, icon_url=event.creator.avatar)
            if event.cover_image is not None:
                embed.set_image(url=event.cover_image)
            else:
                pass
            embed.add_field(name="Privacy level", value=event.privacy_level)
            embed.add_field(name="Start time", value=event.start_time)
            embed.add_field(name="End time", value=event.end_time)
            embed.url(url=event.url)
            
            eventsLogsChannel = self.bot.get_channel(eventLogs)
            await eventsLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_scheduled_event_update(self, before, after):
        try:
            embed=discord.Embed(title="Event deleted", color=0x2699C6, description=f"Name of the event before: {before.name}\nName of the event after:\
                {after.name}\nDescription of the event before:{before.description}\nDescription of the event after:\
                    {after.description}")
            embed.set_author(name=after.creator, icon_url=after.creator.avatar)
            if after.cover_image is not None:
                embed.set_image(url=after.cover_image)
            else:
                pass
            embed.add_field(name="Privacy level before", value=before.privacy_level)
            embed.add_field(name="Privacy level after", value=after.privacy_level)
            embed.add_field(name="Start time before", value=before.start_time)
            embed.add_field(name="End time before", value=before.end_time)
            embed.add_field(name="Start time after", value=after.start_time)
            embed.add_field(name="End time after", value=after.end_time)
            embed.url(url=after.url)

            eventsLogsChannel = self.bot.get_channel(eventLogs)
            await eventsLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_scheduled_event_user_add(self, event, user):
        try:
            embed=discord.Embed(title="User added to an event", color=0x2699C6, description=f"Name of the event: {event.name}\n\
                Description of the event: {event.description}")
            embed.set_author(name=user, icon_url=user.avatar)
            if event.cover_image is not None:
                embed.set_image(url=event.cover_image)
            else:
                pass
            embed.add_field(name="Privacy level", value=event.privacy_level)
            embed.add_field(name="Start time", value=event.start_time)
            embed.add_field(name="End time", value=event.end_time)
            embed.url(url=event.url)
            
            eventsLogsChannel = self.bot.get_channel(eventLogs)
            await eventsLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_scheduled_event_user_remove(self, event, user):
        try:
            embed=discord.Embed(title="User removed from an event", color=0x2699C6, description=f"Name of the event: {event.name}\n\
                Description of the event: {event.description}")
            embed.set_author(name=user, icon_url=user.avatar)
            if event.cover_image is not None:
                embed.set_image(url=event.cover_image)
            else:
                pass
            embed.add_field(name="Privacy level", value=event.privacy_level)
            embed.add_field(name="Start time", value=event.start_time)
            embed.add_field(name="End time", value=event.end_time)
            embed.url(url=event.url)

            eventsLogsChannel = self.bot.get_channel(eventLogs)
            await eventsLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

##############################
######## GUILD EVENTS ########
##############################
# update
# emoji update
# stickers update
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        try:
            embed=discord.Embed(title="Server name changed", color=0x2699C6, description=f"Name before: {before.name}\nName after: {after.name}")

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, before, after):
        try:
            embed=discord.Embed(title="Emoji's updated", color=0x2699C6)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_guild_stickers_update(self, before, after):
        try:
            embed=discord.Embed(title="Stickers updated", color=0x2699C6)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

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
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        try:
            embed=discord.Embed(title="Server profile updated", color=0x2699C6, description=f"Nickname before: {before.nick}\nNickname after: {after.nick}")
            embed.thumbnail(url=after.guild_avatar)
            embed.set_author(name=before.name, icon_url=before.guild_avatar)
            embed.add_field(name="Roles before", value=before.roles)
            embed.add_field(name="Roles after", value=after.roles)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        try:
            embed=discord.Embed(title="User updated", color=0x2699C6, description=f"Name before: {before.name}#{before.discriminator}\nName after: {after.name}#{after.discriminator}")
            embed.thumbnail(url=after.avatar)
            embed.set_author(name=before.name, icon_url=before.avatar)
            embed.add_field(name="Roles before", value=before.roles)
            embed.add_field(name="Roles after", value=after.roles)

            serverLogsChannel = self.bot.get_channel(serverLogs)
            await serverLogsChannel.send(embed=embed)
        except Exception as e:
            print(e)

##################################
######## EXTRA MOD EVENTS ########
##################################
# automod rule create
# automod rule update
# automod rule delete
# automod action
    @commands.Cog.listener()
    async def on_automod_rule_create(self, rule):
        # name
        # creator
        # id
        # enabled
        # trigger
        try:
            embed=discord.Embed(title="Automod rule created", color=0x2699C6, description=f"The ID of the rule is: {rule.id}")
            embed.set_author(name=rule.creator, icon_url=rule.creator.avatar)
            embed.add_field(name="Is it enabled", value=rule.enabled)
            embed.set_footer(text=f"User ID: {rule.creator_id}")
        except Exception as e:
            print(e)

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