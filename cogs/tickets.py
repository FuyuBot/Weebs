import discord
import config
from discord import app_commands, utils
from discord.ext import commands
import mysql.connector
from config import host, user, password, db

mydb = mysql.connector.connect(
host = host,
user = user,
password = password,
database = db
)
cursor = mydb.cursor()

######### Roles ###########
trialhelper = 860758016764936193
helper = 860758016618266624
moderator = 860758015959498763
seniormoderator = 860758015585812480
seniorstaff = 865054271857885225
managementTeam = 860758013731274762
staffTeam = 860758014386896926
###########################
class SelectMenu(discord.ui.Select):
    def __init__(self):
        menu = [
            discord.SelectOption(label="Staff App", description="If you have any questions related to the staff application."),
            discord.SelectOption(label="Report", description="Report someone for breaking one of our server rules."),
            discord.SelectOption(label="Ticket", description="Use this if you want to make a ticket regarding anything else.")
        ]
        super().__init__(placeholder="Select your ticket.", max_values=1, min_values=1, options=menu)

    async def callback(self, interaction: discord.Interaction):
        staffAppTicket = utils.get(interaction.guild.text_channels, name = f"staffapp-{interaction.user.name.lower()}{interaction.user.discriminator}")
        reportTicket = utils.get(interaction.guild.text_channels, name = f"report-{interaction.user.name.lower()}{interaction.user.discriminator}")
        otherTicket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name.lower()}{interaction.user.discriminator}")
        if staffAppTicket is not None: await interaction.response.send_message(f"You already have a staff app ticket open at {staffAppTicket.mention}.", ephemeral=True)
        elif reportTicket is not None: await interaction.response.send_message(f"You already have a report ticket open at {reportTicket.mention}.", ephemeral=True)
        elif otherTicket is not None: await interaction.response.send_message(f"You already have a ticket open at {otherTicket.mention}.", ephemeral=True)
        else:
            overwritesStaff = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
                interaction.guild.get_role(managementTeam): discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True, read_message_history = True),
                interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
            }
            overwritesReport = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
                interaction.guild.get_role(moderator): discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True, read_message_history = True),
                interaction.guild.get_role(seniormoderator): discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True, read_message_history = True),
                interaction.guild.get_role(seniorstaff): discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True, read_message_history = True),
                interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
            }
            overwritesOther = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
                interaction.guild.get_role(staffTeam): discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True, read_message_history = True),
                interaction.guild.get_role(seniorstaff): discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True, read_message_history = True),
                interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
            }
            
            staffCategory = discord.utils.get(interaction.guild.categories, id= 1022942174058397806)
            reportCategory = discord.utils.get(interaction.guild.categories, id= 1022942452585340928)
            category = discord.utils.get(interaction.guild.categories, id= 1022942720391647330)
            if self.values[0] == "Staff App":
                cursor.execute(f"SELECT id FROM applicants WHERE id = {interaction.user.id}")
                checkDB = cursor.fetchall()
                if checkDB == []:
                    channelStaffApps = await interaction.guild.create_text_channel(\
                        name=f"staffapp-{interaction.user.name.lower()}{interaction.user.discriminator}"\
                            , overwrites=overwritesStaff, reason=f"Staff App ticket for {interaction.user}"\
                                , category= staffCategory)
                    await interaction.response.send_message(f"Your ticket has been created.", ephemeral=True)
                    embed = discord.Embed(
                        title= f"{interaction.user}",
                        color=0x2699C6
                    )
                    embed.set_footer(text= f"User's ID: {interaction.user.id}")
                    embed.add_field(name="Staff Application Submitted:", value="❎")
                    await channelStaffApps.send(f"<@&{managementTeam}>, {interaction.user.mention} has created a ticket.",embed=embed)
                else:
                    for row in checkDB:
                        playerRow = row[0]
                        if playerRow == checkDB[0][0]:
                            channelStaffApps = await interaction.guild.create_text_channel(name=f"staffapp-{interaction.user.name.lower()}{interaction.user.discriminator}", overwrites=overwritesStaff, reason=f"Staff App ticket for {interaction.user}", category= staffCategory)
                            await interaction.response.send_message(f"Your ticket has been created.", ephemeral=True)
                            embed = discord.Embed(
                                title= f"{interaction.user}",
                                color=0x2699C6
                            )
                            embed.add_field(name="Staff Application Submitted:", value="✅")
                            embed.set_footer(text= f"User's ID: {interaction.user.id}")
                            await channelStaffApps.send(f"<@&{managementTeam}>, {interaction.user.mention} has created a ticket.",embed=embed)
                
            elif self.values[0] == "Report":
                channelReason = await interaction.guild.create_text_channel(name=f"report-{interaction.user.name.lower()}{interaction.user.discriminator}", overwrites=overwritesReport, reason=f"Report ticket for {interaction.user}", category= reportCategory)
                await channelReason.send(f"<@${staffTeam}<@${seniorstaff}>,\n{interaction.user.mention} has created a ticket.\n\nWhat would you like to report?")
                await interaction.response.send_message(f"Your ticket has been created.", ephemeral=True)
            elif self.values[0] == "Ticket":
                channelOther = await interaction.guild.create_text_channel(name=f"ticket-{interaction.user.name.lower()}{interaction.user.discriminator}", overwrites=overwritesOther, reason=f"Ticket for {interaction.user}", category= category)
                await channelOther.send(f"<@${staffTeam}>,\n{interaction.user.mention} has created a ticket.\n\nHow can we help you today?")
                await interaction.response.send_message(f"Your ticket has been created.", ephemeral=True)

class SelectView(discord.ui.View):
    try:
        def __init__(self, *, timeout = 60):
            super().__init__(timeout=timeout)
            self.add_item(SelectMenu())
    except Exception as e:
            print(e)



class tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `tickets.py`")
    
    @app_commands.command(name='ticket', description="This command will allow you to make a ticket.")
    async def ticket(self, interaction: discord.Interaction):
        await interaction.response.send_message("Choose a ticket type.", view=SelectView(), ephemeral=True)
        print(f"{SelectMenu.values[0]}")
    
    @app_commands.command(name='close', description="Close the ticket!, this will also send a transcript to Management.")
    @app_commands.checks.has_any_role(staffTeam, seniorstaff)
    async def close(self, interaction: discord.Interaction):
        if "staffapp-" in interaction.channel.name or "report-" in interaction.channel.name or "ticket-" in interaction.channel.name:
            embed = discord.Embed(title="Are you sure you want to close this ticket?", color=0x2699C6)
            await interaction.response.send_message(embed=embed, view=Confirm(), ephemeral=True)
        else: await interaction.response.send_message("This isn't a ticket!", ephemeral=True)

class Confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label= "Confirm", style= discord.ButtonStyle.red, custom_id= 'confirm')
    async def confirm_button(self, interaction: discord.Interaction, button):
        try: 
            ticketLogs = interaction.client.get_channel(1022980124909518898)
            await ticketLogs.send(f"`{interaction.channel.name}` was closed by `{interaction.user}`")
            await interaction.channel.delete()
        except Exception as e:
            print(e)
    

async def setup(bot):
    await bot.add_cog(tickets(bot), guilds=[discord.Object(id=config.weebsHangout)])