import discord
import pymongo
import requests
import config
from datetime import timedelta
from datetime import datetime as dt
from discord.ext import commands
from discord import app_commands

currTime = dt.now()
timeFormat = currTime.strftime("%b %d, %Y")
dt_string = currTime.strftime("%m/%d/%Y %H:%M:%S")

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]


##### Roles #####
trialhelper = 860758016764936193
helper = 860758016618266624
moderator = 860758015959498763
seniormoderator = 860758015585812480
seniorstaff = 865054271857885225
staffteam = 860758014386896926
managementTeam = 860758013731274762
#################

class punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED `punishments.py`")
    
####Ban
    @app_commands.command(name='ban' , description="A Weebs Hangout: Ban Command")
    @app_commands.checks.has_any_role(moderator, seniormoderator, seniorstaff)
    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
        try:
            player = user.id
            staff = interaction.user.id
            reason = str(reason)
            isStaff = str(user.top_role)

            playerDB = mycol.find_one({"_id": player}) #Search the user info stored in the data base.

            if reason == None: #Sets the default reason if none is given.
                    reason = "Ha, what a nerd!"
            if playerDB['info']['currently_banned'] == True: #Checks if the user is currently banned.
                await interaction.response.send_message(f"{user} is already banned.",  ephemeral=True)
                return
            else:
                if staff == player: #Checks if the staff member is trying to ban themselves.
                    await interaction.response.send_message("You cannot ban yourself.",  ephemeral=True)
                    return
                elif isStaff == "Staff Team" or isStaff == "Management Team" or isStaff == "Senior Staff" or isStaff == "*": #Checks to see if the person being banned is a staff member.
                        if isStaff == "Management Team" or isStaff == "*":
                            await user.send(f"{interaction.user} tried to ban you just letting you know 🕵️‍♂️")
                        await interaction.response.send_message("That user is a staff member you can't ban them!", ephemeral=True)
                        return
                elif 926163269503299695 == player: #Checks if the bot is trying to be banned.
                    await interaction.response.send_message("You cannot ban me.")
                    return
                else:
                    embed = discord.Embed(
                        title=f'{user} was banned.',
                        color=discord.Color.red()
                    )
                    embed.add_field(name="Staff",value=f"<@{staff}>")
                    embed.add_field(name="Reason",value=f"{reason}")
                    embed.add_field(name="Time", value=f"{dt_string}")
                    embed.set_footer(text=f"ID: {player}")
                    
                    toUserEmbed = discord.Embed(color=discord.Color.red(), title=f"You have been banned from A Weeb's Hangout")
                    toUserEmbed.set_author(name=user, icon_url=user.avatar)
                    toUserEmbed.add_field(name="Reason", value=reason)
                    toUserEmbed.add_field(name="Time", value=dt_string)
                    toUserEmbed.add_field(name="Appeal at", value="https://forms.gle/Q71pTeFg6d1iQ2aaA")
                    toUserEmbed.set_footer(text=f"ID: {player}")

                    await user.send(embed=toUserEmbed)
                    await interaction.response.send_message(embed=embed)
                    await interaction.guild.ban(user)
                    logs = self.bot.get_channel(865078390109634590)
                    await logs.send(embed=embed)
                    mycol.update_one({'_id': player}, {"$set": {"info.currently_banned" : True}})

                    bansList = playerDB['punishments']['bans']
                    bansList.append({f"{timeFormat}": {"Staff": interaction.user.id, "Reason": reason}})
                    mycol.update_one({'_id': player}, {"$set": {"punishments.bans": bansList}})
        except Exception as e:
            print(e)

####Unban
    @app_commands.command(name='unban' , description="A Weebs Hangout: Ban Command")
    @app_commands.checks.has_any_role(moderator, seniormoderator, seniorstaff)
    async def unban(self, interaction: discord.Interaction, user: discord.Member):
        logs = self.bot.get_channel(865078390109634590)
        player = user.id

        playerDB = mycol.find_one({"_id": player})

        if playerDB['info']['currently_banned'] == False: # Checks to see if a user is currently banned.
            await interaction.response.send_message(f"{user} is not banned.",  ephemeral=True)
            return
        else:
            await interaction.guild.unban(user)

            embed = discord.Embed(
                        title=f'{user} was unbanned.',
                        color=discord.Color.green()
                    )
            await interaction.response.send_message(embed=embed)
            await logs.send(embed=embed)
            mycol.update_one({'_id': player}, {"$set": {"info.currently_banned" : False}})

####Timeout
    @app_commands.command(name='timeout' , description="A Weebs Hangout: Timeout Command")
    @app_commands.checks.has_any_role(helper, moderator, seniormoderator, seniorstaff)
    async def timeout(self, interaction: discord.Interaction, user: discord.Member, duration: int, durationtype: str, reason: str):
        try:
            if user.is_timed_out() is True:
                return await interaction.response.send_message("That user is already in timeout.", ephemeral=True)
            player = user.id
            staff = interaction.user.id
            originaldur = duration
            duration = int(duration)
            playerDB = mycol.find_one({"_id": player})
            durations = [ # This is the list of all of the possible duration types
                'minute', 'minutes', 'min',
                'hour', 'hours', 'h',
                'day', 'days', 'd',
                'week', 'weeks', 'w',
                'month', 'm'
            ]
            durType = durationtype.lower() # This is making the string all lowercase.
            isStaff = str(user.top_role)

            if staff == player: # This is checking if the punished player is yourself.
                await interaction.response.send_message("You cannot timeout yourself.",  ephemeral=True)
                return
            elif isStaff == "Staff Team" or isStaff == "Management Team" or isStaff == "Senior Staff" or isStaff == "*": # This is checking if the punished player is a staff member.
                if isStaff == "Management Team" or isStaff == "*": # Now it is checking if the staff member is of high ranking.
                    await user.send(f"{interaction.user} tried to time you out just letting you know 🕵️‍♂️")
                await interaction.response.send_message("That user is a staff member you can't timeout them!", ephemeral=True)
                return
            elif 926163269503299695 == player: # This is checking if the punished player is the bot.
                await interaction.response.send_message("You cannot put me in timeout.")
                return
            if durType in durations: # It passes this if all is correct
                if durType == "minute" or durType == "minutes" or durType == "min" and duration <= 40320: # It enters this if the duration type is minutes.
                    if duration > 1: durType = "minutes"
                    else: durType = "minute"
                    duration *= 60
                    timeoutList = playerDB['punishments']['timeouts']
                    timeoutList.append(({f"{timeFormat}": {"Staff": interaction.user.id,"Length": f"{originaldur} {durType}", "Reason": reason}}))
                    await user.timeout(discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                    logs = self.bot.get_channel(865078390109634590)
                    timeoutEmbed = discord.Embed(
                        title=f"{user} was put in timeout",
                        color=discord.Color.red()
                    )
                    timeoutEmbed.add_field(name="Punished By:", value=f"<@{staff}>", inline= True)
                    timeoutEmbed.add_field(name="Duration:", value=f"{originaldur} {durType}", inline= True)
                    timeoutEmbed.add_field(name="Reason:", value=f"{reason}")
                    await interaction.response.send_message(embed=timeoutEmbed)
                    await logs.send(embed=timeoutEmbed)
                    mycol.update_one({'_id': player}, {"$set": {"punishments.timeouts": timeoutList}})
                elif durType == "hour" or durType == "hours" or durType == "h" and duration <= 672:# It enters this if the duration type is hours.
                    if duration > 1: durType = "hours"
                    else: durType = "hour"
                    duration *= 3600
                    timeoutList = playerDB['punishments']['timeouts']
                    timeoutList.append(({f"{timeFormat}": {"Staff": interaction.user.id,"Length": f"{originaldur} {durType}", "Reason": reason}}))
                    await user.timeout(discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                    logs = self.bot.get_channel(865078390109634590)
                    timeoutEmbed = discord.Embed(
                        title=f"{user} was put in timeout",
                        color=discord.Color.red()
                    )
                    timeoutEmbed.add_field(name="Punished By:", value=f"<@{staff}>", inline= True)
                    timeoutEmbed.add_field(name="Duration:", value=f"{originaldur} {durType}", inline= True)
                    timeoutEmbed.add_field(name="Reason:", value=f"{reason}")
                    await interaction.response.send_message(embed=timeoutEmbed)
                    await logs.send(embed=timeoutEmbed)
                    mycol.update_one({'_id': player}, {"$set": {"punishments.timeouts": timeoutList}})
                elif durType == "day" or durType == "days" or durType == "d" and duration <= 28:# It enters this if the duration type is days.
                    if duration > 1: durType = "days"
                    else: durType = "day"
                    duration *= 86400
                    timeoutList = playerDB['punishments']['timeouts']
                    timeoutList.append(({f"{timeFormat}": {"Staff": interaction.user.id,"Length": f"{originaldur} {durType}", "Reason": reason}}))
                    await user.timeout(discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                    logs = self.bot.get_channel(865078390109634590)
                    timeoutEmbed = discord.Embed(
                        title=f"{user} was put in timeout",
                        color=discord.Color.red()
                    )
                    timeoutEmbed.add_field(name="Punished By:", value=f"<@{staff}>", inline= True)
                    timeoutEmbed.add_field(name="Duration:", value=f"{originaldur} {durType}", inline= True)
                    timeoutEmbed.add_field(name="Reason:", value=f"{reason}")
                    await interaction.response.send_message(embed=timeoutEmbed)
                    await logs.send(embed=timeoutEmbed)
                    mycol.update_one({'_id': player}, {"$set": {"punishments.timeouts": timeoutList}})
                elif durType == "week" or durType == "weeks" or durType == "w" and duration <= 4:# It enters this if the duration type is weeks.
                    if duration > 1: durType = "weeks"
                    else: durType = "week"
                    duration *= 604800
                    timeoutList = playerDB['punishments']['timeouts']
                    timeoutList.append(({f"{timeFormat}": {"Staff": interaction.user.id,"Length": f"{originaldur} {durType}", "Reason": reason}}))
                    await user.timeout(discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                    logs = self.bot.get_channel(865078390109634590)
                    timeoutEmbed = discord.Embed(
                        title=f"{user} was put in timeout",
                        color=discord.Color.red()
                    )
                    timeoutEmbed.add_field(name="Punished By:", value=f"<@{staff}>", inline= True)
                    timeoutEmbed.add_field(name="Duration:", value=f"{originaldur} {durType}", inline= True)
                    timeoutEmbed.add_field(name="Reason:", value=f"{reason}")
                    await interaction.response.send_message(embed=timeoutEmbed)
                    await logs.send(embed=timeoutEmbed)
                    mycol.update_one({'_id': player}, {"$set": {"punishments.timeouts": timeoutList}})
                elif durType == "month" or durType == "m" and duration == 1:# It enters this if the duration type is month.
                    duration = 2.419e+6
                    durType = "month"
                    timeoutList = playerDB['punishments']['timeouts']
                    timeoutList.append(({f"{timeFormat}": {"Staff": interaction.user.id,"Length": f"{originaldur} {durType}", "Reason": reason}}))
                    await user.timeout(discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                    logs = self.bot.get_channel(865078390109634590)
                    timeoutEmbed = discord.Embed(
                        title=f"{user} was put in timeout",
                        color=discord.Color.red()
                    )
                    timeoutEmbed.add_field(name="Punished By:", value=f"<@{staff}>", inline= True)
                    timeoutEmbed.add_field(name="Duration:", value=f"{originaldur} {durType}", inline= True)
                    timeoutEmbed.add_field(name="Reason:", value=f"{reason}")
                    await interaction.response.send_message(embed=timeoutEmbed)
                    await logs.send(embed=timeoutEmbed)
                    mycol.update_one({'_id': player}, {"$set": {"punishments.timeouts": timeoutList}})
                else:
                    embed = discord.Embed(
                        title= "Timeouts can only be up to 1 month.",
                        color= discord.Color.red()
                    )
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = discord.Embed(
                        title= "Invalid duration.",
                        color= discord.Color.red()
                    )
                await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            print(e)
            
####Remove timeout
    @app_commands.command(name='remove-timeout', description="A Weebs Hangout: Remove Timeout Command")
    @app_commands.checks.has_any_role(moderator, seniormoderator, seniorstaff)
    async def remove_timeout(self, interaction: discord.Interaction, user: discord.Member):
        await self.bot.remove_timeout()
        embed = discord.Embed(
            title= f"{user} is no longer in timeout.",
            color= discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)
        logs = self.bot.get_channel(865078390109634590)
        await logs.send(embed=embed)

####Warn
    @app_commands.command(name='warn', description="A Weebs hangout: Warn a user with a given reason.")
    @app_commands.checks.has_any_role(trialhelper, helper, moderator, seniormoderator, seniorstaff)
    async def warn(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        player = user.id
        staff = interaction.user.id
        playerDB = mycol.find_one({"_id": player})
        if staff == player:#Checks to see if you are trying to punish yourself
            await interaction.response.send_message("You cannot warn yourself.",  ephemeral=True)
            return
        elif playerDB['info']['staff'] == True:#Checking if the user is a staff member.
            if playerDB['info']['manager'] ==  True:#Checking if the user is a manager.
                await user.send(f"{interaction.user} tried to warn you just letting you know 🕵️‍♂️")
            await interaction.response.send_message("That user is a staff member you can't warn them!", ephemeral=True)
            return
        elif 926163269503299695 == player:
            await interaction.response.send_message("You cannot warn me.")
            return
        if reason == None:
            reason = "No reason was provided."

        warnList = playerDB['punishments']['timeouts']
        warnList.append(({f"{timeFormat}": {"Staff": interaction.user.id, "Note": reason}}))
        embed = discord.Embed(
            title=f"{user} was warned",
            color=discord.Color.red()
        )
        embed.add_field(name="Staff", value=f"<@{staff}>")
        embed.add_field(name="Reason", value=f"{reason}")
        embed.add_field(name="Time", value=f"{dt_string}")
        embed.set_footer(text=f"ID: {player}")

        playerEmbed = discord.Embed(
            title="You have been warned in A Weeb's Hangout",
            color=discord.Color.red()
        )
        playerEmbed.add_field(name="Reason", value=f"{reason}")
        playerEmbed.add_field(name="Time", value=f"{dt_string}")
        playerEmbed.set_footer(text=f"Your discord ID: {player}")

        await interaction.response.send_message(embed=embed)
        await user.send(embed=playerEmbed)
        logs = self.bot.get_channel(865078390109634590)
        await logs.send(embed=embed)
        mycol.update_one({'_id': player}, {"$set": {"punishments.timeouts": warnList}})

####Set note
    @app_commands.command(name="set-note", description="Set a note on a user.")
    @app_commands.checks.has_any_role(staffteam, seniorstaff)
    async def setNote(self, interaction: discord.Interaction, user: discord.Member, note: str):
        try:
            player = user.id
            staff = interaction.user.id
            playerDB = mycol.find_one({"_id": player})
            noteList = playerDB['punishments']['notes']
            noteList.append(({f"{timeFormat}": {"Staff": interaction.user.id, "Note": note}}))
            mycol.update_one({'_id': player}, {"$set": {"punishments.notes": noteList}})
        except Exception as e:
            print(e)

####Logs
    @app_commands.command(name="logs", description="Check how many punishments a user has.")
    @app_commands.checks.has_any_role(staffteam, seniorstaff)
    async def logs(self, interaction: discord.Interaction, user: discord.Member):
        try:
            player = user.id
            playerDB = mycol.find_one({"_id": player})
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(punishments(bot), guilds=[discord.Object(id=860752406551461909)])