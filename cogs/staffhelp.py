from audioop import add
from doctest import Example
from logging.config import valid_ident
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

    @app_commands.command(name='trial-help', description="Sends how to use all of the commands and permissions given to Trial Helpers.")
    @app_commands.checks.has_any_role(trialhelper, managementTeam)
    async def trialhelp(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Trial Helper | Help System",color=trialColor,description="This system shows you how to use all the commands and\
            permissions you have access to. If you have any other questions about these commands please message anyone on the Management Team!")
        warnEmbed=discord.Embed(title="/warn (user) (reason)", color=trialColor)
        warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules. Our server\
            rules can be found here <#860762802703695913>")
        closeEmbed=discord.Embed(title='/close',color=trialColor)
        closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
        ticketsEmbed=discord.Embed(title='Permission', color=trialColor)
        ticketsEmbed.add_field(name="View General Tickets", value="As a Trial Helper you have access to view and respond to general tickets.")
        messagesEmbed=discord.Embed(title='Permission', color=trialColor)
        messagesEmbed.add_field(name="Delete Messages", value="As a Trial Helper you have access to delete messages from other members, only delete\
            message if it should be deleted. Use common sense.")
        
        await interaction.response.send_message("Help Message sent to DM's!", ephemeral=True)
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
    @app_commands.command(name='helper-help', description="Sends how to use all of the of the commands and permissions given to Helpers")
    @app_commands.checks.has_any_role(helper, managementTeam)
    async def helperhelp(self, interaction: discord.Interaction):
        try:
            embed=discord.Embed(title="Helper | Help System",color=helperColor,description="This system shows you how to use all of the commands and\
                permissions you have access to. If you have any other questions about these commands please message anyone on the Management Team!")
            warnEmbed=discord.Embed(title="/warn (user) (reason)",color=helperColor)
            warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
                Our server rules can be found here <#860762802703695913>")
            timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=helperColor)
            timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
            closeEmbed=discord.Embed(title='/close',color=helperColor)
            closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
            ticketsEmbed=discord.Embed(title='Permission', color=helperColor)
            ticketsEmbed.add_field(name="View General Tickets", value="As a Helper you have access to view and respond to general tickets.")
            messagesEmbed=discord.Embed(title='Permission', color=helperColor)
            messagesEmbed.add_field(name="Delete Messages", value="As a Helper you have access to delete messages from other members,\
                only delete message if it should be deleted. Use common sense.")
            nicknameEmbed=discord.Embed(title='Permission', color=helperColor)
            nicknameEmbed.add_field(name="Manage Nicknames", value="As a Helper you have access to manage other peoples nicknames to make sure they fit\
                within our server rules.")
            
            await interaction.response.send_message("Help Message sent to DM's!", ephemeral=True)
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
# close
# polls
# view and respond to general tickets
# view and respond to report tickets
# delete messages from other members
# manage nicknames
# manage threads
    @app_commands.command(name='moderator-help', description="Sends how to use all of the commands and permissions given to Moderators")
    @app_commands.checks.has_any_role(moderator, managementTeam)
    async def moderatorhelp(self, interaction: discord.Interaction):
        try:
            embed=discord.Embed(title="Moderator | Help System", color=modColor, description="This system shows you how to use all of the commands\
                given to you by me, Fuyu! If you have any other questions about these commands please message anyone on the Management Team!")
            warnEmbed=discord.Embed(title="/warn (user) (reason)",color=modColor)
            warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
                Our server rules can be found here <#860762802703695913>")
            timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=modColor)
            timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
            closeEmbed=discord.Embed(title='/close',color=modColor)
            closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
            pollsEmbed=discord.Embed(title='/poll (title) (option1) (option2) <option3> <option4>', color=modColor, description="() =  Required | <> = Not Required")
            pollsEmbed.add_field(name='Usage', value='Use this command to create a poll in chat. Use this reasonably but you can use it whenever, if someone asks to make a poll go ahead.')
            GticketsEmbed=discord.Embed(title='Permission', color=modColor)
            GticketsEmbed.add_field(name="View General Tickets", value="As a Moderator you have access to view and respond to general tickets.")
            RticketsEmbed=discord.Embed(title='Permission', color=modColor)
            RticketsEmbed.add_field(name="View Report Tickets", value="As a Moderator you have access to view and respond to report tickets.")
            messagesEmbed=discord.Embed(title='Permission', color=modColor)
            messagesEmbed.add_field(name="Delete Messages", value="As a Moderator you have access to delete messages from other members,\
                only delete message if it should be deleted. Use common sense.")
            nicknameEmbed=discord.Embed(title='Permission', color=modColor)
            nicknameEmbed.add_field(name="Manage Nicknames", value="As a Moderator you have access to manage other peoples nicknames to make sure they\
                fit within our server rules.")
            manageThreads=discord.Embed(title='Permission', color=modColor)
            manageThreads.add_field(name="Delete Messages", value="As a Moderator you have access to manage Threads make sure that if they are\
                inactive to close them and if they have inappropriate names, please just set the name to whoever\
                    created the ticket e.g. 'Jzcob2842-Thread'")

            await interaction.response.send_message("Help Message sent to DM's!", ephemeral=True)
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
# close
# polls
# manage events
# view and respond to general tickets
# view and respond to report tickets
# delete messages from other members
# manage nicknames
# manage threads
    @app_commands.command(name='senior-moderator-help', description="Sends how to use all of the commands and permissions given to Moderators")
    @app_commands.checks.has_any_role(seniormoderator, managementTeam)
    async def seniormoderatorhelp(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Senior Moderator | Help System", color=srModColor, description="This system shows you how to use all of the\
            commands given to you by me, Fuyu! If you have any other questions about these commands please message anyone on the Management Team!")
        warnEmbed=discord.Embed(title="/warn (user) (reason)",color=srModColor)
        warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
            Our server rules can be found here <#860762802703695913>")
        timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=srModColor)
        timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
        closeEmbed=discord.Embed(title='/close',color=srModColor)
        closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
        pollsEmbed=discord.Embed(title='/poll (title) (option1) (option2) <option3> <option4>', color=srModColor, description="() =  Required | <> = Not Required")
        pollsEmbed.add_field(name='Usage', value='Use this command to create a poll in chat. Use this reasonably but you can use it whenever, if someone asks to make a poll go ahead.')
        eventsEmbed=discord.Embed(title='Permission', color=srModColor)
        eventsEmbed.add_field(name='Manage Events', value="As a Senior Moderator you have access to Manage Server Events.")
        GticketsEmbed=discord.Embed(title='Permission', color=srModColor)
        GticketsEmbed.add_field(name="View General Tickets", value="As a Senior Moderator you have access to view and respond to general tickets.")
        RticketsEmbed=discord.Embed(title='Permission', color=srModColor)
        RticketsEmbed.add_field(name="View Report Tickets", value="As a Senior Moderator you have access to view and respond to report tickets.")
        messagesEmbed=discord.Embed(title='Permission', color=srModColor)
        messagesEmbed.add_field(name="Delete Messages", value="As a Senior Moderator you have access to delete messages from other members,\
            only delete message if it should be deleted. Use common sense.")
        nicknameEmbed=discord.Embed(title='Permission', color=srModColor)
        nicknameEmbed.add_field(name="View General Tickets", value="As a Senior Moderator you have access to view and respond to general tickets.")
        manageThreads=discord.Embed(title='Permission', color=srModColor)
        manageThreads.add_field(name="Delete Messages", value="As a Senior Moderator you have access to delete messages from other members,\
            only delete message if it should be deleted. Use common sense.")
        

        await interaction.user.send("Help Message sent to DM's!", ephemeral=True)
        await interaction.user.send(embed=embed)
        await interaction.user.send(embed=warnEmbed)
        await interaction.user.send(embed=timeoutEmbed)
        await interaction.user.send(embed=closeEmbed)
        await interaction.user.send(embed=pollsEmbed)
        await interaction.user.send(embed=eventsEmbed)
        await interaction.user.send(embed=GticketsEmbed)
        await interaction.user.send(embed=RticketsEmbed)
        await interaction.user.send(embed=messagesEmbed)
        await interaction.user.send(embed=nicknameEmbed)
        await interaction.user.send(embed=manageThreads)
        await interaction.user.send(embed=exampleEmbed)


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
    @app_commands.command(name='admin-help',  description="Sends how to use all of the commands and permissions given to Administrators.")
    @app_commands.checks.has_any_role(seniorstaff, managementTeam)
    async def adminhelp(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Admin | Help System", color=adminColor, description="This system shows you how to use all of the\
            commands given to you by me, Fuyu! If you have any other questions about these commands please message anyone on the Management Team!")
        warnEmbed=discord.Embed(title="/warn (user) (reason)",color=adminColor)
        warnEmbed.add_field(name="Usage:", value="This command is used to give a user a warning for breaking one of our server rules.\
            Our server rules can be found here <#860762802703695913>")
        timeoutEmbed=discord.Embed(title="/timeout (user) (duration) (durationType) (reason)", color=adminColor)
        timeoutEmbed.add_field(name="Usage", value="This command is used to put a user in timeout")
        closeEmbed=discord.Embed(title='/close',color=adminColor)
        closeEmbed.add_field(name='Usage', value="Use this command to close tickets once you make sure that everything is all set in the ticket.")
        pollsEmbed=discord.Embed(title='/poll (title) (option1) (option2) <option3> <option4>', color=adminColor, description="() =  Required | <> = Not Required")
        pollsEmbed.add_field(name='Usage', value='Use this command to create a poll in chat. Use this reasonably but you can use it whenever, if someone asks to make a poll go ahead.')
        rolesEmbed=discord.Embed(title='Permission', color=adminColor)
        rolesEmbed.add_field(name='Manage Roles', value='As an Admin you have access to Manage Roles')
        auditEmbed=discord.Embed(title='Permission', color=adminColor)
        auditEmbed.add_field(name='View Audit Log', value="As an Admin you have access to view the servers audit log.")
        eventsEmbed=discord.Embed(title='Permission', color=adminColor)
        eventsEmbed.add_field(name='Manage Events', value="As an Admin you have access to Manage Server Events.")
        GticketsEmbed=discord.Embed(title='Permission', color=adminColor)
        GticketsEmbed.add_field(name="View General Tickets", value="As an Admin you have access to view and respond to general tickets.")
        RticketsEmbed=discord.Embed(title='Permission', color=adminColor)
        RticketsEmbed.add_field(name="View Report Tickets", value="As an Admin you have access to view and respond to report tickets.")
        messagesEmbed=discord.Embed(title='Permission', color=adminColor)
        messagesEmbed.add_field(name="Delete Messages", value="As an Admin you have access to delete messages from other members,\
            only delete message if it should be deleted. Use common sense.")
        nicknameEmbed=discord.Embed(title='Permission', color=adminColor)
        nicknameEmbed.add_field(name="View General Tickets", value="As an Admin you have access to view and respond to general tickets.")
        manageThreads=discord.Embed(title='Permission', color=adminColor)
        manageThreads.add_field(name="Delete Messages", value="As an Admin you have access to delete messages from other members,\
            only delete message if it should be deleted. Use common sense.")
        

        await interaction.response.send_message("Help Message sent to DM's!", ephemeral=True)
        await interaction.user.send(embed=embed)
        await interaction.user.send(embed=warnEmbed)
        await interaction.user.send(embed=timeoutEmbed)
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
    
    @app_commands.command(name='manager-help', description='Sends how to use all of the commands and permissions given to Managers.')
    @app_commands.checks.has_any_role(managementTeam)
    async def managerhelp(self, interaction: discord.Interaction):
        return

    
async def setup(bot):
    await bot.add_cog(staffhelp(bot), guilds=[discord.Object(id=860752406551461909)])