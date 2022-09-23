import discord
from discord import app_commands
from discord.ext import commands
from discord import utils
from datetime import datetime, date, timedelta, time
import mysql.connector
from config import host, user, password, db
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

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
        cursor.execute(f"SELECT player FROM bans WHERE player = {player}")
        checkDB = cursor.fetchall()

        if staff == player:
            await interaction.response.send_message("You cannot ban yourself.",  ephemeral=True)
            return
        elif 926163269503299695 == player:
            await interaction.response.send_message("You cannot ban me.")
            return
        if reason == None:
            reason = "Ha, what a nerd!"

        if checkDB == []:
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
            await interaction.response.send_message(embed=embed)
            await interaction.guild.ban(user)

        else:
            for row in checkDB:
                playerRow = row[0]
                if playerRow == checkDB[0][0]:
                    await interaction.response.send_message(f"<@{player}> is already banned.")
                    return
                else:
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
                    await interaction.response.send_message(embed=embed)
                    await interaction.guild.ban(user)
                    logs = self.bot.get_channel(865078390109634590)
                    await logs.send(embed=embed)


######## UnBan
    @app_commands.command(name='unban', description="A Weebs Hangout: UnBan Command")
    @app_commands.checks.has_any_role(moderator, seniormoderator, seniorstaff)
    async def unban(self, interaction: discord.Interaction, user: discord.Member):
        player = user.id
        cursor.execute(f"SELECT player FROM bans WHERE player = {player}")
        checkDB = cursor.fetchall()
        if checkDB == []:
            await interaction.response.send_message("Nobody has been banned yet.")
        else:
            for row in checkDB:
                playerRow = row[0]
                if playerRow != checkDB[0][0]:
                    await interaction.response.send_message(f"<@{player}> is not banned.")
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


######## TimeOut
    @app_commands.command(name='timeout' , description="A Weebs Hangout: Timeout Command")
    @app_commands.checks.has_any_role(helper, moderator, seniormoderator, seniorstaff)
    async def timeout(self, interaction: discord.Interaction, user: discord.Member, duration: str=None, durationtype: str=None, *, reason: str=None):
        staff = interaction.user.id
        originaldur = duration
        duration = int(duration)

        durations = [
            'minute', 'minutes', 'min',
            'hour', 'hours', 'h',
            'day', 'days', 'd',
            'week', 'weeks', 'w',
            'month', 'm'
        ]

        durType = durationtype.lower()
        timeoutEmbed = discord.Embed(
            title=f"{user} was put in timeout",
            color=discord.Color.red()
        )
        timeoutEmbed.add_field(name="Punished By:", value=f"<@{staff}>", inline= True)
        timeoutEmbed.add_field(name="Duration:", value=f"{originaldur} {durType}.", inline= True)
        timeoutEmbed.add_field(name="Reason:", value=f"{reason}")

        if durType in durations:
            if durType == "minute" or durType == "minutes" or durType == "min" and duration <= 40320:
                duration *= 60
                await user.timeout(until= discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                await interaction.response.send_message(embed=timeoutEmbed)
                logs = self.bot.get_channel(865078390109634590)
                await logs.send(embed=timeoutEmbed)
            elif durType == "hour" or durType == "hours" or durType == "h" and duration <= 672:
                duration *= 3600
                await user.timeout(until= discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                await interaction.response.send_message(embed=timeoutEmbed)
                logs = self.bot.get_channel(865078390109634590)
                await logs.send(embed=timeoutEmbed)
            elif durType == "day" or durType == "days" or durType == "d" and duration <= 28:
                duration *= 86400
                await user.timeout(until= discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                await interaction.response.send_message(embed=timeoutEmbed)
                logs = self.bot.get_channel(865078390109634590)
                await logs.send(embed=timeoutEmbed)
            elif durType == "week" or durType == "weeks" or durType == "w" and duration <= 4:
                duration *= 604800
                await user.timeout(until= discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                await interaction.response.send_message(embed=timeoutEmbed)
                logs = self.bot.get_channel(865078390109634590)
                await logs.send(embed=timeoutEmbed)
            elif durType == "month" or durType == "m" and duration == 1:
                duration = 2.419e+6
                await user.timeout(until= discord.utils.utcnow() + timedelta(seconds= duration), reason= reason)
                await interaction.response.send_message(embed=timeoutEmbed)
                logs = self.bot.get_channel(865078390109634590)
                await logs.send(embed=timeoutEmbed)
            else:
                embed = discord.Embed(
                    title= "Timeouts can only be up to 1 month.",
                    color= discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                    title= "Invalid duration.",
                    color= discord.Color.red()
                )
            await interaction.response.send_message(embed=embed)



    @app_commands.command(name='remove_timeout', description="A Weebs Hangout: Remove Timeout Command")
    @app_commands.checks.has_any_role(moderator, seniormoderator, seniorstaff)
    async def remove_timeout(self, interaction: discord.Interaction, user: discord.Member):
        await user.remove_timeout()
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
    async def warn(self, interaction: discord.Interaction, user: discord.Member, *, reason: str=None):
        player = user.id
        staff = interaction.user.id
        reason = str(reason)
        cursor.execute(f"SELECT player FROM warns WHERE player = {player}")
        checkDB = cursor.fetchall()

        if staff == player:
            await interaction.response.send_message("You cannot warn yourself.",  ephemeral=True)
        elif 926163269503299695 == player:
            await interaction.response.send_message("You cannot warn me.")
            return
        if reason == None:
            reason = "No reason was provided."

        if not checkDB:
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
            embed.add_field(name="Reason", value=f"{reason}")
            embed.add_field(name="Time", value=f"{dt_string}")
            embed.set_footer(text=f"Your discord ID: {player}")
            await interaction.response.send_message(embed=embed)
            await user.send(embed=playerEmbed)
        else:
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

async def setup(bot):
    await bot.add_cog(punishments(bot), guilds=[discord.Object(id=860752406551461909)])