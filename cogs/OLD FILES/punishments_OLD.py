import discord
from discord import app_commands
from discord.ext import commands
from discord import utils
from datetime import datetime, timedelta
import mysql.connector
from config import host, user, password, db, color, footer
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

mydb = mysql.connector.connect(
host = host,
user = user,
password = password,
database = db
)
##### Roles #####
trialhelper = 860758016764936193
helper = 860758016618266624
moderator = 860758015959498763
seniormoderator = 860758015585812480
seniorstaff = 865054271857885225
staffteam = 860758014386896926
managementTeam = 860758013731274762
#################
cursor = mydb.cursor()


class punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: 'punishments.py'")

######## Ban
    @app_commands.command(name='ban' , description="A Weebs Hangout: Ban Command")
    @app_commands.checks.has_any_role(moderator, seniormoderator, seniorstaff)
    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
        player = user.id
        staff = interaction.user.id
        reason = str(reason)
        
        cursor.execute(f"SELECT bans FROM punishments WHERE player = {player}")
        punishDB = cursor.fetchone()
        cursor.execute(f"SELECT player FROM bans WHERE player = {player}")
        checkDB = cursor.fetchall()
        isStaff = str(user.top_role)

        if staff == player:
            await interaction.response.send_message("You cannot ban yourself.",  ephemeral=True)
            return
        elif isStaff == "Staff Team" or isStaff == "Management Team" or isStaff == "Senior Staff" or isStaff == "*":
                if isStaff == "Management Team" or isStaff == "*":
                    await user.send(f"{interaction.user} tried to ban you just letting you know 🕵️‍♂️")
                await interaction.response.send_message("That user is a staff member you can't ban them!", ephemeral=True)
                return
        elif 926163269503299695 == player:
            await interaction.response.send_message("You cannot ban me.")
            return
        if reason == None:
            reason = "Ha, what a nerd!"

        if punishDB == []:
            cursor.execute(f"INSERT INTO punishments (player, bans, warns, timeouts) VALUES ({player}, 1, 0, 0)")
            mydb.commit()
            mydb.reconnect()
        
            
        if checkDB == []:
            punishRow = int(punishDB[0])
            punishRow = 1 + punishRow
            cursor.execute(f"UPDATE punishments SET bans = {punishRow} WHERE player = {player}")
            sql = "INSERT INTO bans (player, staff, reason, time) VALUES (%s, %s, %s, NOW())"
            val = (player, staff, reason)
            
            try:
                cursor.execute(sql, val)
                mydb.commit()
            except:
                await interaction.response.send_message('Did not send to the DB!')

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

        else:
            for row in checkDB:
                playerRow = row[0]
                if playerRow == checkDB[0][0]:
                    await interaction.response.send_message(f"<@{player}> is already banned.")
                    return
                else:
                    punishRow = int(punishDB[0])
                    punishRow = 1 + punishRow
                    cursor.execute(f"UPDATE punishments SET bans = {punishRow} WHERE player = {player}")
                    sql = "INSERT INTO bans (player, staff, reason, time) VALUES (%s, %s, %s, NOW())"
                    val = (player, staff, reason)
                    cursor.execute(f"UPDATE")

                    try:
                        cursor.execute(sql, val)
                        mydb.commit()
                    except:
                        await interaction.response.send_message('Did not send to the DB!')

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

######## Unban
    @app_commands.command(name='unban', description="Unbans the player specified.")
    @app_commands.checks.has_any_role(moderator, seniormoderator, seniorstaff)
    async def unban(self, interaction: discord.Interaction, user: discord.Member):
        player = user.id
        cursor.execute(f"SELECT player FROM bans WHERE player = {player}")
        checkDB = cursor.fetchall()
        if checkDB is None:
            await interaction.response.send_message("That user has not been banned yet.") #Message if no one has been banned yet.
        else:
            cursor.execute(f"SELECT player FROM bans WHERE player = {player}")
            x = cursor.fetchone()
            try:
                p = x[0]
            except:
                print("Did not work.")
            if p is None:
                await interaction.response.send_message(f"<@{player}> is not banned.") #Nessage if the specified user is not banned.
            else:
                cursor.execute(f"DELETE FROM bans WHERE player = {player}")
                mydb.commit()
                embed = discord.Embed(
                    title=f'{user} was unbanned.',
                    color=discord.Color.green()
                )
                await interaction.response.send_message(embed=embed)
                await interaction.guild.unban(user)
                logs = self.bot.get_channel(865078390109634590)
                await logs.send(embed=embed)

######## Timeout
    @app_commands.command(name='timeout' , description="A Weebs Hangout: Timeout Command")
    @app_commands.checks.has_any_role(helper, moderator, seniormoderator, seniorstaff)
    async def timeout(self, interaction: discord.Interaction, user: discord.Member, duration: int, durationtype: str, reason: str):
        try:
            if user.is_timed_out is True:
                return await interaction.response.send_message("That user is already in timeout.")
            staff = interaction.user.id
            player = user.id
            originaldur = duration
            duration = int(duration)
            print(duration)
            cursor.execute(f"SELECT timeouts FROM punishments WHERE player = {player}")
            checkDB = cursor.fetchall()
            durations = [
                'minute', 'minutes', 'min',
                'hour', 'hours', 'h',
                'day', 'days', 'd',
                'week', 'weeks', 'w',
                'month', 'm'
            ]
            durType = durationtype.lower()
            isStaff = str(user.top_role)
            if staff == player:
                await interaction.response.send_message("You cannot timeout yourself.",  ephemeral=True)
                return
            elif isStaff == "Staff Team" or isStaff == "Management Team" or isStaff == "Senior Staff" or isStaff == "*":
                if isStaff == "Management Team" or isStaff == "*":
                    await user.send(f"{interaction.user} tried to time you out just letting you know 🕵️‍♂️")
                await interaction.response.send_message("That user is a staff member you can't timeout them!", ephemeral=True)
                return
            elif 926163269503299695 == player:
                await interaction.response.send_message("You cannot put me in timeout.")
                return
            if checkDB == []:
                if durType in durations:
                    if durType == "minute" or durType == "minutes" or durType == "min" and duration <= 40320:
                        if duration > 1: durType = "minutes"
                        else: durType = "minute"
                        duration *= 60
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
                    elif durType == "hour" or durType == "hours" or durType == "h" and duration <= 672:
                        if duration > 1: durType = "hours"
                        else: durType = "hour"
                        duration *= 3600
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
                    elif durType == "day" or durType == "days" or durType == "d" and duration <= 28:
                        if duration > 1: durType = "days"
                        else: durType = "day"
                        duration *= 86400
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
                    elif durType == "week" or durType == "weeks" or durType == "w" and duration <= 4:
                        if duration > 1: durType = "weeks"
                        else: durType = "week"
                        duration *= 604800
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
                    elif durType == "month" or durType == "m" and duration == 1:
                        duration = 2.419e+6
                        durType = "month"
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
                try:
                    cursor.execute(f"INSERT INTO punishments (player, bans, warns, timeouts) VALUES ({player}, 0, 0, 1)")
                    mydb.commit()
                except Exception as e:
                    print(e)
            else:
                for row in checkDB:
                    playerRow = int(row[0])
                    playerRow = 1 + playerRow
                    try:
                        cursor.execute(f"UPDATE punishments SET timeouts = {playerRow} WHERE player = {player}")
                        mydb.commit()
                    except Exception as e:
                        print(e)
                    if durType in durations:
                        if durType == "minute" or durType == "minutes" or durType == "min" and duration <= 40320:
                            if duration > 1: durType = "minutes"
                            else: durType = "minute"
                            duration *= 60
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
                        elif durType == "hour" or durType == "hours" or durType == "h" and duration <= 672:
                            if duration > 1: durType = "hours"
                            else: durType = "hour"
                            duration *= 3600
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
                        elif durType == "day" or durType == "days" or durType == "d" and duration <= 28:
                            if duration > 1: durType = "days"
                            else: durType = "day"
                            duration *= 86400
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
                        elif durType == "week" or durType == "weeks" or durType == "w" and duration <= 4:
                            if duration > 1: durType = "weeks"
                            else: durType = "week"
                            duration *= 604800
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
                        elif durType == "month" or durType == "m" and duration == 1:
                            duration = 2.419e+6
                            durType = "month"
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
######## Warn
    @app_commands.command(name='warn', description="A Weebs hangout: Warn a user with a given reason.")
    @app_commands.checks.has_any_role(trialhelper, helper, moderator, seniormoderator, seniorstaff)
    async def warn(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        player = user.id
        staff = interaction.user.id
        reason = str(reason)
        cursor.execute(f"SELECT warns FROM punishments WHERE player = {player}")
        punishDB = cursor.fetchone()
        cursor.execute(f"SELECT player FROM warns WHERE player = {player}")
        checkDB = cursor.fetchall()
        isStaff = str(user.top_role)

        if staff == player:
            await interaction.response.send_message("You cannot warn yourself.",  ephemeral=True)
            return
        elif isStaff == "Staff Team" or isStaff == "Management Team" or isStaff == "Senior Staff" or isStaff == "*":
            if isStaff == "Management Team" or isStaff == "*":
                await user.send(f"{interaction.user} tried to warn you just letting you know 🕵️‍♂️")
            await interaction.response.send_message("That user is a staff member you can't warn them!", ephemeral=True)
            return
        elif 926163269503299695 == player:
            await interaction.response.send_message("You cannot warn me.")
            return
        if reason == None:
            reason = "No reason was provided."

        if punishDB == []:
                    cursor.execute(f"INSERT INTO punishments (player, bans, warns, timeouts) VALUES ({player}, 0, 1, 0)")
                    mydb.commit()
                    mydb.reconnect()
        if not checkDB:
            punishRow = int(punishDB[0])
            punishRow = 1 + punishRow
            print(punishRow)
            cursor.execute(f"UPDATE punishments SET warns = {punishRow} WHERE player = {player}")
            sql = "INSERT INTO warns (player, staff, reason, time) VALUES (%s, %s, %s, NOW())"
            val = (player, staff, reason)
            
            try:
                cursor.execute(sql, val)
                mydb.commit()
            except:
                await interaction.response.send_message("Did not send to the DB!")
                print(mysql.connector.errors.Error)

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
        else:
            punishRow = int(punishDB[0])
            punishRow = 1 + punishRow
            print(punishRow)
            cursor.execute(f"UPDATE punishments SET warns = {punishRow} WHERE player = {player}")
            sql = "INSERT INTO warns (player, staff, reason, time) VALUES (%s, %s, %s, NOW())"
            val = (player, staff, reason)
            try:
                cursor.execute(sql, val)
                mydb.commit()
            except:
                await interaction.response.send_message("Did not send to the DB!")
                print(mysql.connector.errors.Error)

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

    @app_commands.command(name="logs", description="Check how many punishments a user has.")
    @app_commands.checks.has_any_role(staffteam, seniorstaff)
    async def logs(self, interaction: discord.Interaction, user: discord.Member):
        try:
            player = user.id
            cursor.execute(f"SELECT player FROM punishments WHERE player = {player}")
            punishDB = cursor.fetchall()
            
            

            if punishDB == []:
                cursor.execute(f"INSERT INTO punishments (player, bans, warns, timeouts) VALUES ({player}, 0, 0, 0)")
                mydb.commit()
                return await interaction.response.send_message(f"That user does not have any punishments.")
            else:
                cursor.execute(f"SELECT bans FROM punishments WHERE player = {player}")
                bans = cursor.fetchone()
                cursor.execute(f"SELECT warns FROM punishments WHERE player = {player}")
                warns = cursor.fetchone()
                cursor.execute(f"SELECT timeouts FROM punishments WHERE player = {player}")
                timeouts = cursor.fetchone()
                bansRow = int(bans[0])
                warnsRow = int(warns[0])
                timeoutRow = int(timeouts[0])

                embed = discord.Embed(color=color, title=f"{user}'s Punishments")
                embed.add_field(name="Bans", value=bansRow, inline=True)
                embed.add_field(name="Warns", value=warnsRow, inline=True)
                embed.add_field(name="Timeouts", value=timeoutRow, inline=True)
                cursor.execute(f"SELECT player, staff, note FROM notes WHERE player = {player}")
                notesDB = cursor.fetchall()
                count = 0
                if notesDB == []:
                    note = "User has no notes."
                    embed.add_field(name="Notes", value=f"{note}")
                else:
                    for table in notesDB:
                        count += 1
                        note = table[2]
                        staff = self.bot.get_user(int(table[1]))
                        embed.add_field(name=f"Note #{count}. | By: {staff.name}", value=f"{note}", inline=False)
                embed.set_footer(text=footer)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)
    
    @app_commands.command(name="set-note", description="Set a note on a user.")
    @app_commands.checks.has_any_role(staffteam, seniorstaff)
    async def setNote(self, interaction: discord.Interaction, user: discord.Member, note: str):
        try:
            player = user.id
            staff = interaction.user.id
            cursor.execute(f"SELECT player, staff, note FROM notes WHERE player = {player}")
            notesDB = cursor.fetchall()
            cursor.execute(f'INSERT INTO notes (player, staff, note) VALUES ({player}, {staff}, "{note}")')
            mydb.commit()
            return await interaction.response.send_message("Note added successfully.")
        except Exception as e:
            print(e)
    
    '''
    @app_commands.command(name="remove-note", description="Removes a note on a user.")
    @app_commands.checks.has_any_role(managementTeam)
    async def removeNote(self, interaction: discord.Interaction, user: discord.Member, number: int=None):
        player = user.id
        cursor.execute(f"SELECT player, staff, note FROM notes WHERE player = {player}")
        notesDB = cursor.fetchall()
        if notesDB == []:
            return await interaction.response.send_message("That user does not have any notes.")
        else:
            for table in notesDB:
                return'''


async def setup(bot):
    await bot.add_cog(punishments(bot), guilds=[discord.Object(id=860752406551461909)])