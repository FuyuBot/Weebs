import discord
from discord import app_commands
from discord.ext import commands

#### Colors
trialColor = 0x429ebd
helperColor = 0x20b38f
modColor = 0xffda71
srModColor = 0xe0176b
adminColor = 0x88ec56
managerColor = 0xe7b158
exampleColor = discord.Color.red()
#### Roles
trialhelper = 860758016764936193
helper = 860758016618266624
moderator = 860758015959498763
seniormoderator = 860758015585812480
seniorstaff = 865054271857885225
managementTeam = 860758013731274762
################

exampleEmbed=discord.Embed(
            title="Example",
            color=exampleColor,
            description="Possible durationTypes:\n'minute, minutes, min, hour, hours, h, day, days, d, week, weeks, w, month, m'\n\n\n/timeout Jzcob#2842 1 d Breaking rule #2"
        )

class staffhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `staffhelp.py`')

#Trial Helper Commands and Permissions
# warn
# close
# view general tickets
# delete messages from other members

    @app_commands.command(name='trial-help', description="Explains how to use all of the commands and permissions that are given to trial helpers.")
    @app_commands.checks.has_any_role(trialhelper, managementTeam)
    async def trialhelp(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Trial Helper | Help System",color=trialColor,description="This system shows you how to use all the commands and\
            permissions you have access to. If you have any other questions about these commands please message anyone on the management team!")
        warnEmbed=discord.Embed(title="/warn (user) (reason)", color=trialColor)
        warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules. Our server\
            rules can be found here <#860762802703695913>")
        closeEmbed=discord.Embed(title='/close',color=trialColor)
        closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
        ticketsEmbed=discord.Embed(title='Permission', color=trialColor)
        ticketsEmbed.add_field(name="View General Tickets", value="As a trial helper, you have access to view and respond to general tickets.")
        messagesEmbed=discord.Embed(title='Permission', color=trialColor)
        messagesEmbed.add_field(name="Delete Messages", value="As a trial helper, you have access to delete messages from other members, only delete a\
            message if it should be deleted. Use common sense.")
        
        await interaction.response.send_message("Help message sent to DM's!", ephemeral=True)
        await interaction.user.send(embed=embed)
        await interaction.user.send(embed=warnEmbed)
        await interaction.user.send(embed=closeEmbed)
        await interaction.user.send(embed=ticketsEmbed)
        await interaction.user.send(embed=messagesEmbed)
        

#Helper Commands and Permissions
# warn
# timeout
# close
# view and respond to general tickets
# delete messages from other members 
# manage nicknames
    @app_commands.command(name='helper-help', description="Explains how to use all of the commands and permissions that are given to helpers.")
    @app_commands.checks.has_any_role(helper, managementTeam)
    async def helperhelp(self, interaction: discord.Interaction):
        try:
            embed=discord.Embed(title="Helper | Help System",color=helperColor,description="This system shows you how to use all of the commands and\
                permissions you have access to. If you have any other questions about these commands please message anyone on the management team!")
            warnEmbed=discord.Embed(title="/warn (user) (reason)",color=helperColor)
            warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
                Our server rules can be found here <#860762802703695913>")
            timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=helperColor)
            timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
            closeEmbed=discord.Embed(title='/close',color=helperColor)
            closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
            ticketsEmbed=discord.Embed(title='Permission', color=helperColor)
            ticketsEmbed.add_field(name="View General Tickets", value="As a helper, you have access to view and respond to general tickets.")
            messagesEmbed=discord.Embed(title='Permission', color=helperColor)
            messagesEmbed.add_field(name="Delete Messages", value="As a helper, you have access to delete messages from other members,\
                only delete a message if it should be deleted. Use common sense.")
            nicknameEmbed=discord.Embed(title='Permission', color=helperColor)
            nicknameEmbed.add_field(name="Manage Nicknames", value="As a helper, you have access to manage other user's nicknames to make sure they fit\
                within our server rules.")
            
            await interaction.response.send_message("Help message sent to DM's!", ephemeral=True)
            await interaction.user.send(embed=embed)
            await interaction.user.send(embed=warnEmbed)
            await interaction.user.send(embed=timeoutEmbed)
            await interaction.user.send(embed=closeEmbed)
            await interaction.user.send(embed=ticketsEmbed)
            await interaction.user.send(embed=messagesEmbed)
            await interaction.user.send(embed=nicknameEmbed)
            await interaction.user.send(embed=exampleEmbed)
        except Exception as e:
            print(e)
        

#Moderator Commands and Permissions
# warn
# timeout
# ban
# unban
# close
# polls
# view and respond to general tickets
# view and respond to report tickets
# delete messages from other members
# manage nicknames
# manage threads
    @app_commands.command(name='moderator-help', description= "Explains how to use all of the commands and permissions that are given to moderators.")
    @app_commands.checks.has_any_role(moderator, managementTeam)
    async def moderatorhelp(self, interaction: discord.Interaction):
        try:
            embed=discord.Embed(title="Moderator | Help System", color=modColor, description= "This system shows you how to use all of the commands and\
                permissions you have access to. If you have any other questions about these commands please message anyone on the management team!")
            warnEmbed=discord.Embed(title="/warn (user) (reason)",color=modColor)
            warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
                Our server rules can be found here <#860762802703695913>")
            timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=modColor)
            timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
            banEmbed=discord.Embed(title="/ban (user) (reason)", color=modColor)
            banEmbed.add_field(name='Usage', value="Use this command to ban users from the server.")
            unbanEmbed=discord.Embed(title='/unban (user)', color=modColor)
            unbanEmbed.add_field(name='Usage', value="Use this command to unban users from the server.")
            closeEmbed=discord.Embed(title='/close',color=modColor)
            closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
            pollsEmbed=discord.Embed(title='/poll (title) (option1) (option2) <option3> <option4>', color=modColor, description="() =  Required | <> = Not Required")
            pollsEmbed.add_field(name='Usage', value='Use this command to create a poll in chat. Use this reasonably but you can use it whenever, if someone asks to make a poll go ahead.')
            GticketsEmbed=discord.Embed(title='Permission', color=modColor)
            GticketsEmbed.add_field(name="View General Tickets", value="As a moderator, you have access to view and respond to general tickets.")
            RticketsEmbed=discord.Embed(title='Permission', color=modColor)
            RticketsEmbed.add_field(name="View Report Tickets", value="As a moderator, you have access to view and respond to report tickets.")
            messagesEmbed=discord.Embed(title='Permission', color=modColor)
            messagesEmbed.add_field(name="Delete Messages", value="As a moderator, you have access to delete messages from other members,\
                only delete a message if it should be deleted. Use common sense.")
            nicknameEmbed=discord.Embed(title='Permission', color=modColor)
            nicknameEmbed.add_field(name="Manage Nicknames", value="As a moderator, you have access to manage other user's nicknames to make sure they\
                fit within our server rules.")
            manageThreads=discord.Embed(title='Permission', color=modColor)
            manageThreads.add_field(name="Delete Messages", value="As a moderator, you have access to manage Threads make sure that if they are\
                inactive to close them and if they have inappropriate names, please just set the name to whoever\
                    created the ticket e.g. 'Jzcob2842-Thread'")

            await interaction.response.send_message("Help message sent to DM's!", ephemeral=True)
            await interaction.user.send(embed=embed)
            await interaction.user.send(embed=warnEmbed)
            await interaction.user.send(embed=timeoutEmbed)
            await interaction.user.send(embed=closeEmbed)
            await interaction.user.send(embed=pollsEmbed)
            await interaction.user.send(embed=GticketsEmbed)
            await interaction.user.send(embed=RticketsEmbed)
            await interaction.user.send(embed=messagesEmbed)
            await interaction.user.send(embed=nicknameEmbed)
            await interaction.user.send(embed=manageThreads)
            await interaction.user.send(embed=exampleEmbed)
        except Exception as e:
            print(e)

#Senior Moderator Commands and Permissions
# warn
# timeout
# ban
# unban
# close
# polls
# manage events
# view and respond to general tickets
# view and respond to report tickets
# delete messages from other members
# manage nicknames
# manage threads
    @app_commands.command(name='senior-moderator-help', description="Sends how to use all of the commands and permissions that are given to senior moderators.")
    @app_commands.checks.has_any_role(seniormoderator, managementTeam)
    async def seniormoderatorhelp(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Senior Moderator | Help System", color=srModColor, description="This system shows you how to use all of the commands and\
            permissions you have access to. If you have any other questions about these commands please message anyone on the Management Team!")
        warnEmbed=discord.Embed(title="/warn (user) (reason)",color=srModColor)
        warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
            Our server rules can be found here <#860762802703695913>")
        timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=srModColor)
        timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
        banEmbed=discord.Embed(title="/ban (user) (reason)", color=srModColor)
        banEmbed.add_field(name='Usage', value="Use this command to ban users from the server.")
        unbanEmbed=discord.Embed(title='/unban (user)', color=srModColor)
        unbanEmbed.add_field(name='Usage', value="Use this command to unban users from the server.")
        closeEmbed=discord.Embed(title='/close',color=srModColor)
        closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
        pollsEmbed=discord.Embed(title='/poll (title) (option1) (option2) <option3> <option4>', color=srModColor, description="() =  Required | <> = Not Required")
        pollsEmbed.add_field(name='Usage', value='Use this command to create a poll in chat. Use this reasonably but you can use it whenever, if someone asks to make a poll go ahead.')
        eventsEmbed=discord.Embed(title='Permission', color=srModColor)
        eventsEmbed.add_field(name='Manage Events', value="As a senior moderator, you have access to Manage Server Events.")
        GticketsEmbed=discord.Embed(title='Permission', color=srModColor)
        GticketsEmbed.add_field(name="View General Tickets", value="As a senior moderator, you have access to view and respond to general tickets.")
        RticketsEmbed=discord.Embed(title='Permission', color=srModColor)
        RticketsEmbed.add_field(name="View Report Tickets", value="As a senior moderator, you have access to view and respond to report tickets.")
        messagesEmbed=discord.Embed(title='Permission', color=srModColor)
        messagesEmbed.add_field(name="Delete Messages", value="As a senior moderator, you have access to delete messages from other members,\
            only delete a message if it should be deleted. Use common sense.")
        nicknameEmbed=discord.Embed(title='Permission', color=srModColor)
        nicknameEmbed.add_field(name="Manage Nicknames", value="As a senior moderator, you have access to manage other user's nicknames to make sure they\
                fit within our server rules.")
        manageThreads=discord.Embed(title='Permission', color=srModColor)
        manageThreads.add_field(name="Delete Messages", value="As a senior moderator, you have access to delete messages from other members,\
            only delete a message if it should be deleted. Use common sense.")
        
        try:
            await interaction.response.send_message("Help message sent to DM's!", ephemeral=True)
            await interaction.user.send(embed=embed)
            await interaction.user.send(embed=warnEmbed)
            await interaction.user.send(embed=timeoutEmbed)
            await interaction.user.send(embed=banEmbed)
            await interaction.user.send(embed=unbanEmbed)
            await interaction.user.send(embed=closeEmbed)
            await interaction.user.send(embed=pollsEmbed)
            await interaction.user.send(embed=eventsEmbed)
            await interaction.user.send(embed=GticketsEmbed)
            await interaction.user.send(embed=RticketsEmbed)
            await interaction.user.send(embed=messagesEmbed)
            await interaction.user.send(embed=nicknameEmbed)
            await interaction.user.send(embed=manageThreads)
            await interaction.user.send(embed=exampleEmbed)
        except Exception as e:
            print(e)


#Admin Commands and Permissions
# warn
# timeout
# ban
# close
# polls
# manage roles
# view audit log
# manage events
# mention everyone
# view and respond to general tickets
# view and respond to report tickets
# delete messages from other members
# manage nicknames
# manage threads
    @app_commands.command(name='admin-help',  description="Sends how to use all of the commands and permissions that are given to Administrators.")
    @app_commands.checks.has_any_role(seniorstaff, managementTeam)
    async def adminhelp(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Admin | Help System", color=adminColor, description="This system shows you how to use all of the commands and\
            permissions you have access to. If you have any other questions about these commands please message anyone on the management team!")
        warnEmbed=discord.Embed(title="/warn (user) (reason)",color=adminColor)
        warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
            Our server rules can be found here <#860762802703695913>")
        timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=adminColor)
        timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
        banEmbed=discord.Embed(title="/ban (user) (reason)", color=adminColor)
        banEmbed.add_field(name='Usage', value="Use this command to ban users from the server.")
        unbanEmbed=discord.Embed(title='/unban (user)', color=adminColor)
        unbanEmbed.add_field(name='Usage', value="Use this command to unban users from the server.")    
        closeEmbed=discord.Embed(title='/close',color=adminColor)
        closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
        pollsEmbed=discord.Embed(title='/poll (title) (option1) (option2) <option3> <option4>', color=adminColor, description="() =  Required | <> = Not Required")
        pollsEmbed.add_field(name='Usage', value='Use this command to create a poll in chat. Use this reasonably but you can use it whenever, if someone asks to make a poll go ahead.')
        rolesEmbed=discord.Embed(title='Permission', color=adminColor)
        rolesEmbed.add_field(name='Manage Roles', value='As an admin, you have access to manage roles')
        auditEmbed=discord.Embed(title='Permission', color=adminColor)
        auditEmbed.add_field(name='View Audit Log', value="As an admin, you have access to view the servers audit log.")
        eventsEmbed=discord.Embed(title='Permission', color=adminColor)
        eventsEmbed.add_field(name='Manage Events', value="As an admin, you have access to manage server events.")
        GticketsEmbed=discord.Embed(title='Permission', color=adminColor)
        GticketsEmbed.add_field(name="View General Tickets", value="As an admin, you have access to view and respond to general tickets.")
        RticketsEmbed=discord.Embed(title='Permission', color=adminColor)
        RticketsEmbed.add_field(name="View Report Tickets", value="As an admin, you have access to view and respond to report tickets.")
        messagesEmbed=discord.Embed(title='Permission', color=adminColor)
        messagesEmbed.add_field(name="Delete Messages", value="As an admin, you have access to delete messages from other members,\
            only delete a message if it should be deleted. Use common sense.")
        nicknameEmbed=discord.Embed(title='Permission', color=adminColor)
        nicknameEmbed.add_field(name="Manage Nicknames", value="As an admin, you have access to manage other user's nicknames to make sure they\
                fit within our server rules.")
        manageThreads=discord.Embed(title='Permission', color=adminColor)
        manageThreads.add_field(name="Delete Messages", value="As an admin you have access to delete messages from other members,\
            only delete a message if it should be deleted. Use common sense.")
        

        await interaction.response.send_message("Help message sent to DM's!", ephemeral=True)
        await interaction.user.send(embed=embed)
        await interaction.user.send(embed=warnEmbed)
        await interaction.user.send(embed=timeoutEmbed)
        await interaction.user.send(embed=banEmbed)
        await interaction.user.send(embed=unbanEmbed)
        await interaction.user.send(embed=closeEmbed)
        await interaction.user.send(embed=pollsEmbed)
        await interaction.user.send(embed=eventsEmbed)
        await interaction.user.send(embed=rolesEmbed)
        await interaction.user.send(embed=auditEmbed)
        await interaction.user.send(embed=GticketsEmbed)
        await interaction.user.send(embed=RticketsEmbed)
        await interaction.user.send(embed=messagesEmbed)
        await interaction.user.send(embed=nicknameEmbed)
        await interaction.user.send(embed=manageThreads)
        await interaction.user.send(embed=exampleEmbed)
    
#Manager & Management Commands and Permissions
#everything
    @app_commands.command(name='manager-help', description='Sends how to use all of the commands and permissions given to managers.')
    @app_commands.checks.has_any_role(managementTeam)
    async def managerhelp(self, interaction: discord.Interaction):
        try:
            embed=discord.Embed(title="Manager | Help System", color=managerColor, description="This system shows you how to use all of the commands and\
                permissions you have access to. If you have any other questions about these commands please message anyone on the Management Team!")
            #PUNISHMENTS
            warnEmbed=discord.Embed(title="/warn (user) (reason)", color=managerColor)
            warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
                Our server rules can be found here <#860762802703695913>")
            timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=managerColor)
            timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
            banEmbed=discord.Embed(title="/ban (user) (reason)", color=managerColor)
            banEmbed.add_field(name='Usage', value="Use this command to ban users from the server.")
            unbanEmbed=discord.Embed(title='/unban (user)', color=managerColor)
            unbanEmbed.add_field(name='Usage', value="Use this command to unban users from the server.")    
            #TICKETS
            closeEmbed=discord.Embed(title='/close', color=managerColor)
            closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
            GticketsEmbed=discord.Embed(title='Permission', color=managerColor)
            GticketsEmbed.add_field(name="View General Tickets", value="As a manager, you have access to view and respond to general tickets.")
            RticketsEmbed=discord.Embed(title='Permission', color=managerColor)
            RticketsEmbed.add_field(name="View Report Tickets", value="As a manager, you have access to view and respond to report tickets.")
            AticketsEmbed=discord.Embed(title="Permission", color=managerColor)
            AticketsEmbed.add_field(name="View Application Tickets", value="As a manager, you have access to view and respond to application tickets.")
            #ECONOMY
            addMoneyEmbed=discord.Embed(title="/add-money (user) (amount)", color=managerColor)
            addMoneyEmbed.add_field(name="Usage", value="Use this command to add money to a user.")
            removeMoneyEmbed=discord.Embed(title="/remove-money (user) (where) (amount)", color=managerColor)
            removeMoneyEmbed.add_field(name="Usage", value="Use this command to remove money from a user.")
            #LEVELING
            levelResetEmbed=discord.Embed(title="/reset-levels", color=managerColor)
            levelResetEmbed.add_field(name="Usage", value="Use this command to reset all of the levels in the server.")
            #OTHER COMMANDS
            pollsEmbed=discord.Embed(title='/poll (title) (option1) (option2) <option3> <option4>', color=managerColor, description="() =  Required | <> = Not Required")
            pollsEmbed.add_field(name='Usage', value='Use this command to create a poll in chat. Use this reasonably but you can use it whenever, if someone asks to make a poll go ahead.')
            forceVerifyEmbed=discord.Embed(title="/force-verify (user)", color=managerColor)
            forceVerifyEmbed.add_field(name="Usage", value="Use this command to forcibly verify someone.")
            broadcastEmbed=discord.Embed(title="/broadcast (channel) (title) (message)", color=managerColor)
            broadcastEmbed.add_field(name="Usage", value="Use this command to broadcast a message to the server.")
            infoEmbed=discord.Embed(title="/information (channel)", color=managerColor)
            infoEmbed.add_field(name="Usage", value="Sends the entire information channels embeds to the channel specified")
            genshinInfoEmbed=discord.Embed(title="/genshin-information (channel)", color=managerColor)
            genshinInfoEmbed.add_field(name="Usage", value="Sends the entire genshin information channels embeds to the channel specified")
            #PERMISSIONS
            mentionEveryoneEmbed=discord.Embed(title='Permission', color=managerColor)
            mentionEveryoneEmbed.add_field(name="Mention Everyone", value="As a manager, you have access to mention everyone")
            rolesEmbed=discord.Embed(title='Permission', color=managerColor)
            rolesEmbed.add_field(name='Manage Roles', value='As a manager, you have access to manage roles')
            auditEmbed=discord.Embed(title='Permission', color=managerColor)
            auditEmbed.add_field(name='View Audit Log', value="As a manager, you have access to view the servers audit log.")
            eventsEmbed=discord.Embed(title='Permission', color=managerColor)
            eventsEmbed.add_field(name='Manage Events', value="As a manager, you have access to manage server events.")
            messagesEmbed=discord.Embed(title='Permission', color=managerColor)
            messagesEmbed.add_field(name="Delete Messages", value="As an manager, you have access to delete messages from other members,\
                only delete a message if it should be deleted. Use common sense.")
            nicknameEmbed=discord.Embed(title='Permission', color=managerColor)
            nicknameEmbed.add_field(name="Manage Nicknames", value="As an manager, you have access to manage other user's nicknames to make sure they\
                    fit within our server rules.")
            manageThreads=discord.Embed(title='Permission', color=managerColor)
            manageThreads.add_field(name="Delete Messages", value="As an manager, you have access to delete messages from other members,\
                only delete a message if it should be deleted. Use common sense.")
            #APPLICATIONS
            acceptEmbed=discord.Embed(title="/accept (user)", color=managerColor)
            acceptEmbed.add_field(name="Usage", value="Sends the accepted message to the user.")
            denyEmbed=discord.Embed(title="/deny (user) (reason)", color=managerColor)
            denyEmbed.add_field(name="Usage", value="Sends the denial message to the user.")
            await interaction.response.send_message("Help message sent to DM's!", ephemeral=True)
            #PUNISHMENTS
            await interaction.user.send(embed=embed)
            await interaction.user.send(embed=warnEmbed)
            await interaction.user.send(embed=timeoutEmbed)
            await interaction.user.send(embed=banEmbed)
            await interaction.user.send(embed=unbanEmbed)
            #TICKETS AND ECONOMY AND LEVELING
            await interaction.user.send(embed=closeEmbed)
            await interaction.user.send(embed=addMoneyEmbed)
            await interaction.user.send(embed=removeMoneyEmbed)
            await interaction.user.send(embed=levelResetEmbed)
            #OTHER
            await interaction.user.send(embed=pollsEmbed)
            await interaction.user.send(embed=forceVerifyEmbed)
            await interaction.user.send(embed=broadcastEmbed)
            await interaction.user.send(embed=infoEmbed)
            await interaction.user.send(embed=genshinInfoEmbed)
            await interaction.user.send(embed=acceptEmbed)
            await interaction.user.send(embed=denyEmbed)
            #PERMISSIONS
            await interaction.user.send(embed=eventsEmbed)
            await interaction.user.send(embed=rolesEmbed)
            await interaction.user.send(embed=auditEmbed)
            await interaction.user.send(embed=GticketsEmbed)
            await interaction.user.send(embed=RticketsEmbed)
            await interaction.user.send(embed=AticketsEmbed)
            await interaction.user.send(embed=messagesEmbed)
            await interaction.user.send(embed=nicknameEmbed)
            await interaction.user.send(embed=manageThreads)
            await interaction.user.send(embed=exampleEmbed)
        except Exception as e:
            print(e)

    
async def setup(bot):
    await bot.add_cog(staffhelp(bot), guilds=[discord.Object(id=860752406551461909)])